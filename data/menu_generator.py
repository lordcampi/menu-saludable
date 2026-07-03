import copy
import math

from data.recetas import get_receta_por_id
from data.menu_fijo import MENU_DIAS, DIAS_PLAN
from data.hogar import get_factor_escalado, get_nombres_activos


class MenuGenerator:
    def __init__(self, dias=DIAS_PLAN):
        self.dias = dias
        self.menu = []
        self.factor_escalado = get_factor_escalado()

    def cargar_menu_fijo(self):
        """Carga el menú fijo de 15 días escalando ingredientes dinámicamente."""
        self.factor_escalado = get_factor_escalado()
        self.menu = []
        for entrada in MENU_DIAS:
            self.menu.append(self._construir_dia(entrada))
        return self.menu

    def _escalar_ingredientes(self, ingredientes: dict) -> dict:
        """
        Escala todas las cantidades por el factor de consumo actual.

        - tipo 'unidad': redondea hacia arriba (math.ceil) porque no existen
          fracciones de unidades (ej: 2.5 arepas → 3, 3.8 huevos → 4).
        - tipo 'peso' y 'volumen': redondeo estándar a 1 decimal
          (ej: 300g carne × 1.25 = 375.0g).
        """
        if self.factor_escalado == 1.0:
            return ingredientes
        escalados = {}
        for ing, datos in ingredientes.items():
            cantidad_original = datos["cantidad"]
            cantidad_cruda = cantidad_original * self.factor_escalado
            tipo = datos.get("tipo", "peso")
            if tipo == "unidad":
                cantidad_escalada = math.ceil(cantidad_cruda)
            else:
                cantidad_escalada = round(cantidad_cruda, 1)
            escalados[ing] = {**datos, "cantidad": cantidad_escalada}
        return escalados

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
        receta_original = get_receta_por_id(receta_id)
        if not receta_original:
            raise ValueError(f"Receta no encontrada: {receta_id}")
        receta = copy.deepcopy(receta_original)

        # Aplicar overrides del menú fijo (ej: cambio de plátano maduro)
        if overrides:
            for ingrediente, datos in overrides.items():
                if ingrediente in receta["ingredientes"]:
                    receta["ingredientes"][ingrediente].update(datos)
                else:
                    receta["ingredientes"][ingrediente] = datos

        # Escalar ingredientes por factor de consumo dinámico
        receta["ingredientes"] = self._escalar_ingredientes(receta["ingredientes"])

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
