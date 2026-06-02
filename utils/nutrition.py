class NutritionCalculator:
    def __init__(self, persona1_nombre, persona1_peso, persona2_nombre, persona2_peso):
        self.persona1 = {"nombre": persona1_nombre, "peso": persona1_peso}
        self.persona2 = {"nombre": persona2_nombre, "peso": persona2_peso}
        self.p1_calorias_mantencion = self._calcular_calorias_mantencion(persona1_peso, "hombre")
        self.p2_calorias_mantencion = self._calcular_calorias_mantencion(persona2_peso, "mujer")
    
    def _calcular_calorias_mantencion(self, peso, sexo):
        if sexo == "hombre":
            return round(peso * 25)
        return round(peso * 23)
    
    def analizar_menu(self, menu):
        calorias_diarias = []
        proteinas_diarias = []
        for dia in menu:
            resumen = dia["resumen_nutricional"]
            calorias_diarias.append(resumen["calorias_totales"])
            proteinas_diarias.append(resumen["proteinas_totales"])
        promedio_calorias = sum(calorias_diarias) / len(calorias_diarias)
        promedio_proteinas = sum(proteinas_diarias) / len(proteinas_diarias)
        return {
            "promedio_calorias": round(promedio_calorias),
            "promedio_proteinas": round(promedio_proteinas),
            "calorias_min": min(calorias_diarias),
            "calorias_max": max(calorias_diarias),
            "recomendaciones": self._generar_recomendaciones(promedio_calorias)
        }
    
    def _generar_recomendaciones(self, promedio_calorias):
        recomendaciones = []
        if promedio_calorias > self.p1_calorias_mantencion:
            recomendaciones.append(f"Las calorias superan la meta de {self.persona1['nombre']}")
        else:
            recomendaciones.append(f"Calorias dentro del rango para {self.persona1['nombre']}")
        return recomendaciones
    
    def get_metas_personalizadas(self):
        return {
            "persona1": {
                "nombre": self.persona1["nombre"],
                "peso": self.persona1["peso"],
                "calorias_mantencion": self.p1_calorias_mantencion,
                "rango_calorias": f"{self.p1_calorias_mantencion - 200} - {self.p1_calorias_mantencion + 200}"
            },
            "persona2": {
                "nombre": self.persona2["nombre"],
                "peso": self.persona2["peso"],
                "calorias_mantencion": self.p2_calorias_mantencion,
                "rango_calorias": f"{self.p2_calorias_mantencion - 200} - {self.p2_calorias_mantencion + 200}"
            }
        }