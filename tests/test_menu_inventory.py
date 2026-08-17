import pytest

from data.inventory import InventoryManager, PROTEINAS_CONGELABLES
from data.menu_fijo import DIAS_PLAN, MENU_DIAS
from data.menu_generator import MenuGenerator
from data.recetas import RECETAS, get_receta_por_id, get_todas_recetas
from utils.precios import obtener_precios_respaldo
from utils.producto_catalogo import PRESENTACIONES, PRODUCTOS_BUSQUEDA


CAMBIOS_ESPERADOS = {
    "des_08": "Huevos revueltos con arepa",
    "des_01": "Huevo y salchichas",
    "des_02": "Huevos en cacerola",
    "des_12": "Arepa rellena de queso fresco",
    "des_13": "Carimañolas",
    "des_15": "Arepa con huevos pericos",
    "des_14": "Frutas con yogur griego",
    "alm_07": "Sancocho de costilla de res",
    "alm_10": "Costilla de cerdo con arroz y ensalada",
    "alm_05": "Pescado a la plancha con ensalada y platano",
    "alm_06": "Chicharron con yuca frita y ensalada",
    "cen_03": "Wrap de jamon",
    "cen_04": "Platano maduro con queso fresco",
    "cen_05": "Yuca frita con huevo",
    "cen_07": "Empanadas de trigo",
    "cen_08": "Crema de champiñones",
    "cen_09": "Tortilla con huevo napolitano",
    "cen_10": "Sopa Ajinomen",
    "cen_12": "Crema de champiñones de sobre",
    "cen_02": "Wrap de jamon y queso",
    "cen_13": "Empanadas de maiz",
    "cen_14": "Empanadas mixtas de trigo y maiz",
}


def test_menu_fijo_usa_45_recetas_validas_y_unicas():
    ids = [
        entrada[comida]
        for entrada in MENU_DIAS
        for comida in ("desayuno", "almuerzo", "cena")
    ]
    assert len(MENU_DIAS) == DIAS_PLAN == 15
    assert [entrada["dia"] for entrada in MENU_DIAS] == list(range(1, 16))
    assert len(ids) == len(set(ids)) == 45
    assert all(get_receta_por_id(receta_id) for receta_id in ids)


@pytest.mark.parametrize(("receta_id", "nombre"), CAMBIOS_ESPERADOS.items())
def test_sustituciones_del_menu(receta_id, nombre):
    assert get_receta_por_id(receta_id)["nombre"] == nombre


def test_sustituciones_eliminan_ingredientes_anteriores():
    ingredientes_antiguos = {
        "des_08": {"pan_integral", "tomate"},
        "des_01": {"arepa", "aguacate", "tomate", "cebolla_larga", "cilantro"},
        "des_12": {"empanadas_carne", "limon"},
        "des_14": {"arepa", "pechuga_pollo", "aguacate"},
        "alm_01": {"tomate"},
        "alm_02": {"pimenton"},
        "alm_04": {"pimenton"},
        "alm_05": {"tomate"},
        "alm_06": {"tomate", "cebolla"},
        "alm_07": {"espinazo_cerdo"},
        "alm_08": {"pimenton"},
        "alm_09": {"tomate", "cebolla"},
        "alm_10": {"higado_res", "tomate"},
        "alm_15": {"pimenton"},
        "cen_03": {"champiñones", "huevo"},
        "cen_04": {"pechuga_pollo", "aguacate", "tortilla_harina", "tomate"},
        "cen_05": {"zapallo", "zanahoria", "papa", "crema_leche"},
        "cen_07": {"arepa", "atun", "aguacate", "tomate", "cebolla", "limon", "cilantro"},
        "cen_08": {"pasta", "tomate", "zanahoria", "aceite_oliva", "queso_parmesano", "oregano"},
        "cen_09": {"picado_pollo", "zanahoria", "papa"},
        "cen_10": {"pechuga_pollo", "aguacate"},
        "cen_12": {"filete_pescado"},
        "cen_02": {"lentejas"},
        "cen_13": {"menudencias_pollo", "papa", "zanahoria", "pimenton"},
        "cen_14": {"muslo_pollo", "arroz", "harina", "huevo", "jamon"},
        "cen_15": {"pimenton"},
    }
    for receta_id, eliminados in ingredientes_antiguos.items():
        ingredientes = set(get_receta_por_id(receta_id)["ingredientes"])
        assert eliminados.isdisjoint(ingredientes), receta_id


def test_sazon_revisada_incluye_condimentos_clave():
    esperados = {
        "des_03": {"canela"},
        "alm_02": {"laurel"},
        "alm_03": {"oregano"},
        "alm_06": {"ajo", "paprika", "pimienta"},
        "alm_08": {"tomate", "laurel"},
        "alm_15": {"achiote", "cilantro"},
        "cen_01": {"ajo", "mostaza", "salsa_inglesa"},
        "cen_08": {"pimienta", "nuez_moscada"},
        "cen_12": {"pimienta"},
        "cen_15": {"comino", "pimienta"},
    }
    for receta_id, condimentos in esperados.items():
        ingredientes = set(get_receta_por_id(receta_id)["ingredientes"])
        assert condimentos <= ingredientes, receta_id


def test_recetas_tienen_estructura_completa():
    recetas = get_todas_recetas()
    assert len(recetas) == 45
    assert len({receta["id"] for receta in recetas}) == 45

    for categoria, recetas_categoria in RECETAS.items():
        assert len(recetas_categoria) == 15, categoria
        for receta in recetas_categoria:
            assert receta["nombre"].strip()
            assert receta["tiempo_preparacion"].strip()
            assert receta["dificultad"] in {"facil", "media", "dificil"}
            assert len(receta["preparacion"]) >= 4
            assert receta["ingredientes"]
            for datos in receta["ingredientes"].values():
                assert datos["cantidad"] > 0
                assert datos["tipo"] in {"peso", "volumen", "unidad"}
                assert datos["unidad"] in {"gr", "ml", "unidades", "sobres", "paquete"}
            assert set(receta["informacion_nutricional"]) == {
                "calorias", "proteinas", "carbohidratos", "grasas", "fibra"
            }
            assert all(
                valor >= 0
                for valor in receta["informacion_nutricional"].values()
            )


def test_ingredientes_tienen_categoria_catalogo_busqueda_y_precio():
    inventario = InventoryManager([])
    respaldo = obtener_precios_respaldo()
    tipos = {}

    for receta in get_todas_recetas():
        for ingrediente, datos in receta["ingredientes"].items():
            tipos.setdefault(ingrediente, set()).add(datos["tipo"])

    for ingrediente, tipos_receta in tipos.items():
        categorias = [
            categoria
            for categoria, productos in inventario.categorias_productos.items()
            if ingrediente in productos
        ]
        assert len(categorias) == 1, (ingrediente, categorias)
        assert ingrediente in PRESENTACIONES
        assert ingrediente in PRODUCTOS_BUSQUEDA
        assert ingrediente in respaldo
        assert tipos_receta == {PRESENTACIONES[ingrediente]["tipo"]}


def test_ingredientes_retirados_no_aparecen_en_el_sistema():
    retirados = {"polvo_hornear", "salsa_rosada"}
    inventario = InventoryManager([])
    respaldo = obtener_precios_respaldo()
    ingredientes = {
        ingrediente
        for receta in get_todas_recetas()
        for ingrediente in receta["ingredientes"]
    }
    preparaciones = " ".join(
        paso.lower()
        for receta in get_todas_recetas()
        for paso in receta["preparacion"]
    )

    assert retirados.isdisjoint(ingredientes)
    assert "polvo de hornear" not in preparaciones
    assert "salsa rosada" not in preparaciones
    assert retirados.isdisjoint(PRESENTACIONES)
    assert retirados.isdisjoint(PRODUCTOS_BUSQUEDA)
    assert retirados.isdisjoint(respaldo)
    assert all(
        retirados.isdisjoint(productos)
        for productos in inventario.categorias_productos.values()
    )


def _comida_con(ingredientes):
    return {
        "nombre": "Prueba",
        "ingredientes": ingredientes,
    }


def _dia(dia, ingredientes):
    comida = _comida_con(ingredientes)
    return {
        "dia": dia,
        "desayuno": comida,
        "almuerzo": _comida_con({}),
        "cena": _comida_con({}),
    }


def test_existencias_perecederas_no_se_reutilizan_en_dos_semanas():
    tomate = {"tomate": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}}
    inventario = InventoryManager([_dia(1, tomate), _dia(8, tomate)])
    inventario.inventario_actual = {"tomate": 8}

    semanas = inventario.generar_listas_compras_semanales()

    assert semanas["semana_1"]["tomate"]["cantidad"] == 2
    assert semanas["semana_2"]["tomate"]["cantidad"] == 10


def test_inventario_descarta_valores_invalidos_y_productos_obsoletos():
    inventario = InventoryManager([
        _dia(1, {"tomate": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}})
    ])

    normalizado = inventario._normalizar_inventario({
        "tomate": "4.26",
        "producto_obsoleto": 20,
        "cantidad_negativa": -1,
        "cantidad_infinita": float("inf"),
    })

    assert normalizado == {"tomate": 4.3}


def test_bloques_de_compra_suman_el_deficit_total():
    inventario = InventoryManager(MenuGenerator(dias=DIAS_PLAN).cargar_menu_fijo())
    inventario.inventario_actual = {}
    bloques = [inventario.generar_lista_compras_quincenal()]
    bloques.extend(inventario.generar_listas_compras_semanales().values())

    acumulado = {}
    for bloque in bloques:
        for ingrediente, datos in bloque.items():
            acumulado[ingrediente] = acumulado.get(ingrediente, 0) + datos["cantidad"]

    assert set(acumulado) == set(inventario.inventario_necesario)
    for ingrediente, datos in inventario.inventario_necesario.items():
        assert acumulado[ingrediente] == pytest.approx(datos["cantidad"])


def test_congelacion_incluye_costilla_y_excluye_refrigerados():
    inventario = InventoryManager(MenuGenerator(dias=DIAS_PLAN).cargar_menu_fijo())
    inventario.inventario_actual = {"costilla_cerdo": 100}
    porciones = inventario.generar_porciones_congelacion()

    assert "costilla_cerdo" in PROTEINAS_CONGELABLES
    assert {"empanadas_carne", "carimañolas", "empanadas_trigo", "empanadas_maiz"} <= PROTEINAS_CONGELABLES
    assert "costilla_res" in PROTEINAS_CONGELABLES
    assert "costilla_cerdo" in porciones
    assert "costilla_res" in porciones
    assert porciones["costilla_cerdo"]["faltante_comprar"] == pytest.approx(
        max(0, porciones["costilla_cerdo"]["total_necesario"] - 100)
    )
    assert {"jamon", "huevo", "atun"}.isdisjoint(porciones)


def test_menu_generator_limita_dias_y_escala_nutricion():
    generador = MenuGenerator(dias=1)
    generador.factor_escalado = 1.25
    nutricion = generador._escalar_nutricion({
        "calorias": 100,
        "proteinas": 10,
    })

    assert nutricion == {"calorias": 125.0, "proteinas": 12.5}
    assert len(generador.cargar_menu_fijo()) == 1
    with pytest.raises(ValueError):
        MenuGenerator(dias=0)
