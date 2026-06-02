import random
from datetime import datetime, timedelta
from data.recetas import RECETAS

class MenuGenerator:
    def __init__(self, dias=15, personas=2):
        self.dias = dias
        self.personas = personas
        self.menu = []
        self.historial_desayunos = []
        self.historial_almuerzos = []
        self.historial_cenas = []
        self.max_repeticion = 7
    
    def generar_menu(self):
        self.menu = []
        for dia in range(1, self.dias + 1):
            desayuno = self._seleccionar_comida("desayunos", self.historial_desayunos)
            almuerzo = self._seleccionar_comida("almuerzos", self.historial_almuerzos)
            cena = self._seleccionar_comida("cenas", self.historial_cenas)
            
            dia_menu = {
                "dia": dia,
                "fecha": (datetime.now() + timedelta(days=dia-1)).strftime("%d/%m/%Y"),
                "fecha_iso": (datetime.now() + timedelta(days=dia-1)).strftime("%Y-%m-%d"),
                "desayuno": desayuno,
                "almuerzo": almuerzo,
                "cena": cena,
                "resumen_nutricional": self._calcular_resumen_dia(desayuno, almuerzo, cena)
            }
            self.menu.append(dia_menu)
        return self.menu
    
    def _seleccionar_comida(self, categoria, historial):
        recetas_disponibles = RECETAS[categoria]
        recetas_filtradas = [r for r in recetas_disponibles if r["nombre"] not in historial]
        
        if not recetas_filtradas:
            historial.clear()
            recetas_filtradas = recetas_disponibles
        
        receta_seleccionada = random.choice(recetas_filtradas)
        historial.append(receta_seleccionada["nombre"])
        if len(historial) > self.max_repeticion:
            historial.pop(0)
        return receta_seleccionada
    
    def _calcular_resumen_dia(self, desayuno, almuerzo, cena):
        return {
            "calorias_totales": (
                desayuno["informacion_nutricional"]["calorias"] +
                almuerzo["informacion_nutricional"]["calorias"] +
                cena["informacion_nutricional"]["calorias"]
            ),
            "proteinas_totales": (
                desayuno["informacion_nutricional"]["proteinas"] +
                almuerzo["informacion_nutricional"]["proteinas"] +
                cena["informacion_nutricional"]["proteinas"]
            ),
            "carbohidratos_totales": (
                desayuno["informacion_nutricional"]["carbohidratos"] +
                almuerzo["informacion_nutricional"]["carbohidratos"] +
                cena["informacion_nutricional"]["carbohidratos"]
            )
        }
    
    def get_todas_las_recetas(self):
        recetas_usadas = []
        for dia in self.menu:
            for comida in ["desayuno", "almuerzo", "cena"]:
                if dia[comida] not in recetas_usadas:
                    recetas_usadas.append(dia[comida])
        return recetas_usadas
