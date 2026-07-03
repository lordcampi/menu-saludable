"""Calculadora nutricional con soporte para N miembros del hogar."""

from typing import Any, Dict, List, Optional

from data.hogar import cargar_miembros, get_miembros_activos


class NutritionCalculator:
    """Calculadora nutricional para un hogar con N miembros activos."""

    def __init__(self, miembros: Optional[List[Dict[str, Any]]] = None):
        """
        Inicializa la calculadora con los miembros del hogar.

        Args:
            miembros: Lista de miembros del hogar. Si es None, se cargan desde hogar.py.
        """
        if miembros is None:
            miembros = cargar_miembros()
        self.miembros = miembros
        self.activos = get_miembros_activos(miembros)
        self._calcular_calorias()

    def _calcular_calorias(self):
        """Calcula calorías de mantenimiento para todos los miembros activos."""
        self.calorias_por_miembro: Dict[str, Dict[str, Any]] = {}
        for miembro in self.activos:
            sexo = miembro.get("sexo", "mujer")
            peso_ref = miembro.get("peso_objetivo", miembro["peso"])
            if sexo == "hombre":
                calorias = round(peso_ref * 25)
            else:
                calorias = round(peso_ref * 23)
            self.calorias_por_miembro[miembro["id"]] = {
                "nombre": miembro["nombre"],
                "peso": miembro["peso"],
                "altura": miembro["altura"],
                "objetivo": miembro.get("objetivo", "mantener"),
                "peso_objetivo": peso_ref,
                "calorias_mantencion": calorias,
                "rango_calorias": f"{calorias - 200} - {calorias + 200}",
            }

    def get_metas_personalizadas(self) -> Dict[str, Dict[str, Any]]:
        """Retorna metas calóricas para todos los miembros activos."""
        return dict(self.calorias_por_miembro)

    def get_calorias_mantencion_por_nombre(self, nombre: str) -> int:
        """Busca calorías de mantención por nombre del miembro."""
        for meta in self.calorias_por_miembro.values():
            if meta["nombre"] == nombre:
                return meta["calorias_mantencion"]
        return 2000  # fallback seguro

    def analizar_menu(self, menu: List[Dict]) -> Dict[str, Any]:
        """
        Analiza un menú completo y retorna métricas agregadas.

        Args:
            menu: Lista de días, cada uno con resumen_nutricional.

        Returns:
            Diccionario con promedios, rangos y recomendaciones.
        """
        if not menu:
            return {
                "promedio_calorias": 0,
                "promedio_proteinas": 0,
                "calorias_min": 0,
                "calorias_max": 0,
                "recomendaciones": ["No hay menú para analizar."],
            }

        calorias_diarias = []
        proteinas_diarias = []
        for dia in menu:
            resumen = dia.get("resumen_nutricional", {})
            calorias_diarias.append(resumen.get("calorias_totales", 0))
            proteinas_diarias.append(resumen.get("proteinas_totales", 0))

        promedio_calorias = sum(calorias_diarias) / len(calorias_diarias)
        promedio_proteinas = sum(proteinas_diarias) / len(proteinas_diarias)

        return {
            "promedio_calorias": round(promedio_calorias),
            "promedio_proteinas": round(promedio_proteinas),
            "calorias_min": min(calorias_diarias),
            "calorias_max": max(calorias_diarias),
            "recomendaciones": self._generar_recomendaciones(promedio_calorias),
        }

    def _generar_recomendaciones(self, promedio_calorias: float) -> List[str]:
        """
        Genera recomendaciones para todos los miembros activos.

        Compara el promedio de calorías del menú con la meta de cada miembro.
        """
        recomendaciones = []
        for meta in self.calorias_por_miembro.values():
            nombre = meta["nombre"]
            objetivo = meta.get("objetivo", "mantener")
            calorias_meta = meta["calorias_mantencion"]

            if promedio_calorias > calorias_meta:
                if objetivo == "bajar_peso":
                    recomendaciones.append(
                        f"⚠️ El promedio ({round(promedio_calorias)} kcal/día) supera la meta "
                        f"de {nombre} para bajar de peso ({calorias_meta} kcal/día)."
                    )
                else:
                    recomendaciones.append(
                        f"El promedio ({round(promedio_calorias)} kcal/día) supera "
                        f"la meta de mantenimiento de {nombre} ({calorias_meta} kcal/día)."
                    )
            else:
                recomendaciones.append(
                    f"✓ Calorías dentro del rango para {nombre} "
                    f"(meta: {calorias_meta} kcal/día, objetivo: {objetivo})."
                )

        return recomendaciones