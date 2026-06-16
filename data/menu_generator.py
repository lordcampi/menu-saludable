import copy

from data.recetas import get_receta_por_id
from data.menu_fijo import MENU_DIAS, DIAS_PLAN


class MenuGenerator:
    def __init__(self, dias=DIAS_PLAN, personas=2):
        self.dias = dias
        self.personas = personas
        self.menu = []

    def cargar_menu_fijo(self):
        self.menu = []
        for entrada in MENU_DIAS:
            self.menu.append(self._construir_dia(entrada))
        return self.menu

    def _construir_dia(self, entrada):
        overrides = entrada.get("overrides", {})
        desayuno = self._obtener_receta(entrada["desayuno"], overrides.get("desayuno"))
        almuerzo = self._obtener_receta(entrada["almuerzo"], overrides.get("almuerzo"))
        cena = self._obtener_receta(entrada["cena"], overrides.get("cena"))
        return {
            "dia": entrada["dia"],
            "desayuno": desayuno,
            "almuerzo": almuerzo,
            "cena": cena,
            "resumen_nutricional": self._calcular_resumen_dia(desayuno, almuerzo, cena),
        }

    def _obtener_receta(self, receta_id, overrides=None):
        receta = copy.deepcopy(get_receta_por_id(receta_id))
        if not receta:
            raise ValueError(f"Receta no encontrada: {receta_id}")
        if overrides:
            for ingrediente, datos in overrides.items():
                if ingrediente in receta["ingredientes"]:
                    receta["ingredientes"][ingrediente].update(datos)
                else:
                    receta["ingredientes"][ingrediente] = datos
        return receta

    def _calcular_resumen_dia(self, desayuno, almuerzo, cena):
        return {
            "calorias_totales": (
                desayuno["informacion_nutricional"]["calorias"]
                + almuerzo["informacion_nutricional"]["calorias"]
                + cena["informacion_nutricional"]["calorias"]
            ),
            "proteinas_totales": (
                desayuno["informacion_nutricional"]["proteinas"]
                + almuerzo["informacion_nutricional"]["proteinas"]
                + cena["informacion_nutricional"]["proteinas"]
            ),
            "carbohidratos_totales": (
                desayuno["informacion_nutricional"]["carbohidratos"]
                + almuerzo["informacion_nutricional"]["carbohidratos"]
                + cena["informacion_nutricional"]["carbohidratos"]
            ),
        }

    def get_todas_las_recetas(self):
        recetas_usadas = []
        vistos = set()
        for dia in self.menu:
            for comida in ["desayuno", "almuerzo", "cena"]:
                receta = dia[comida]
                if receta["id"] not in vistos:
                    vistos.add(receta["id"])
                    recetas_usadas.append(receta)
        return recetas_usadas
