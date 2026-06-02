from collections import defaultdict

class InventoryManager:
    def __init__(self, menu):
        self.menu = menu
        self.inventario_necesario = self._calcular_inventario_total()
        self.inventario_actual = {}
        self.categorias_productos = {
            "Proteinas": ["gallina", "pechuga_pollo", "carne_mechar", "bistec_res", 
                         "filete_pescado", "atun", "huevo"],
            "Lacteos": ["queso_fresco", "queso_parmesano", "mantequilla", "yogurt", "leche"],
            "Vegetales": ["tomate", "cebolla", "cebolla_larga", "lechuga", "zanahoria",
                         "brocoli", "espinaca", "champiñones", "aji", "cilantro", "ajo",
                         "pimenton", "pepino", "zapallo"],
            "Frutas": ["aguacate", "banano", "fresas", "limon"],
            "Granos y Cereales": ["arroz", "lentejas", "frijol_negro", "avena",
                                 "pan_integral", "arepa", "tortilla_harina", "arvejas"],
            "Tuberculos": ["papa", "yuca", "platano_verde", "platano_maduro", "mazorca"],
            "Frutos secos": ["nueces", "semillas_chia"],
            "Condimentos": ["sal", "azucar", "comino", "canela", "oregano", "miel"],
            "Aceites": ["aceite", "aceite_oliva"]
        }
    
    def _calcular_inventario_total(self):
        inventario = defaultdict(lambda: {"cantidad": 0, "unidad": "", "tipo": ""})
        for dia in self.menu:
            for comida in ["desayuno", "almuerzo", "cena"]:
                for ingrediente, datos in dia[comida]["ingredientes"].items():
                    inventario[ingrediente]["cantidad"] += datos["cantidad"]
                    inventario[ingrediente]["unidad"] = datos["unidad"]
                    inventario[ingrediente]["tipo"] = datos["tipo"]
        return dict(inventario)
    
    def actualizar_inventario_actual(self, inventario_dict):
        self.inventario_actual = inventario_dict
    
    def generar_lista_compras(self):
        lista_compras = {}
        for ingrediente, datos_necesarios in self.inventario_necesario.items():
            necesario = datos_necesarios["cantidad"]
            tengo = self.inventario_actual.get(ingrediente, 0)
            faltante = max(0, necesario - tengo)
            if faltante > 0:
                lista_compras[ingrediente] = {
                    "cantidad": round(faltante, 1),
                    "unidad": datos_necesarios["unidad"],
                    "tipo": datos_necesarios["tipo"]
                }
        return lista_compras
    
    def organizar_por_categorias(self, lista_compras):
        compras_organizadas = {}
        for categoria, productos in self.categorias_productos.items():
            productos_en_categoria = {}
            for producto in productos:
                if producto in lista_compras:
                    productos_en_categoria[producto] = lista_compras[producto]
            if productos_en_categoria:
                compras_organizadas[categoria] = productos_en_categoria
        return compras_organizadas
    
    def get_resumen_inventario(self):
        total_productos = len(self.inventario_necesario)
        productos_completos = sum(
            1 for p, datos in self.inventario_necesario.items()
            if self.inventario_actual.get(p, 0) >= datos["cantidad"]
        )
        return {
            "total_productos": total_productos,
            "productos_completos": productos_completos,
            "porcentaje_completado": (productos_completos / total_productos * 100) if total_productos > 0 else 0
        }
