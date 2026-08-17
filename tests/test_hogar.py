import json

import data.hogar as hogar
import data.menu_generator as menu_generator
from utils.nutrition import NutritionCalculator


def _miembros_con_activos(*ids_activos):
    activos = set(ids_activos)
    return [
        {**miembro, "activo": miembro["id"] in activos}
        for miembro in hogar.MIEMBROS_DEFAULT
    ]


def test_carlos_copia_perfil_y_consumo_de_julian():
    julian = hogar.get_miembro_por_id("julian", hogar.MIEMBROS_DEFAULT)
    carlos = hogar.get_miembro_por_id("carlos", hogar.MIEMBROS_DEFAULT)

    assert carlos is not None
    assert carlos["activo"] is False
    for campo in (
        "edad", "peso", "sexo", "altura", "objetivo", "factor_consumo"
    ):
        assert carlos[campo] == julian[campo]


def test_persistencia_antigua_conserva_carlos_inactivo(tmp_path, monkeypatch):
    archivo = tmp_path / "hogar.json"
    archivo.write_text(
        json.dumps({"activos": {"julian": True, "annmar": True, "nilsa": False}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(hogar, "PERSISTENCIA_FILE", str(archivo))

    carlos = hogar.get_miembro_por_id("carlos")

    assert carlos["activo"] is False


def test_activar_carlos_persiste_sin_alterar_otros(tmp_path, monkeypatch):
    archivo = tmp_path / "hogar.json"
    monkeypatch.setattr(hogar, "PERSISTENCIA_FILE", str(archivo))

    assert hogar.set_miembro_activo("carlos", True) is True

    estados = json.loads(archivo.read_text(encoding="utf-8"))["activos"]
    assert estados == {
        "julian": True,
        "annmar": True,
        "carlos": True,
        "nilsa": False,
    }
    assert hogar.get_miembro_por_id("carlos")["activo"] is True


def test_set_miembro_inexistente_no_persiste(tmp_path, monkeypatch):
    archivo = tmp_path / "hogar.json"
    monkeypatch.setattr(hogar, "PERSISTENCIA_FILE", str(archivo))

    assert hogar.set_miembro_activo("desconocido", True) is False
    assert not archivo.exists()


def test_factores_de_escalado_para_combinaciones_del_hogar():
    assert hogar.get_factor_escalado(
        _miembros_con_activos("julian", "annmar")
    ) == 1.0
    assert hogar.get_factor_escalado(
        _miembros_con_activos("julian", "annmar", "nilsa")
    ) == 1.25
    assert hogar.get_factor_escalado(
        _miembros_con_activos("julian", "annmar", "carlos")
    ) == 1.5
    assert hogar.get_factor_escalado(
        _miembros_con_activos("julian", "annmar", "carlos", "nilsa")
    ) == 1.75


def test_carlos_activo_tiene_misma_meta_que_julian():
    miembros = _miembros_con_activos("julian", "annmar", "carlos")
    metas = NutritionCalculator(miembros).get_metas_personalizadas()

    assert metas["carlos"]["calorias_mantencion"] == 2000
    assert (
        metas["carlos"]["calorias_mantencion"]
        == metas["julian"]["calorias_mantencion"]
    )


def test_menu_completo_escala_ingredientes_y_nutricion_con_carlos(monkeypatch):
    monkeypatch.setattr(menu_generator, "get_factor_escalado", lambda: 1.5)

    desayuno = menu_generator.MenuGenerator(dias=1).cargar_menu_fijo()[0]["desayuno"]

    assert desayuno["ingredientes"]["huevo"]["cantidad"] == 5
    assert desayuno["ingredientes"]["arepa"]["cantidad"] == 3
    assert desayuno["informacion_nutricional"]["calorias"] == 495
