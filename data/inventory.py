from collections import defaultdict


class InventoryManager:
    def __init__(self, menu):
        self.menu = menu
        self.inventario_necesario = self._calcular_inventario_total()
        self.inventario_actual = {}
        self.categorias_productos = {
            "Proteinas": [
                "espinazo_cerdo", "pechuga_pollo", "muslo_pollo", "alitas_pollo",
                "menudencias_pollo", "carne_mechar", "bistec_res", "filete_pescado",
                "atun", "huevo", "jamon", "carne_molida", "chicharron",
                "salchichas", "salchicha", "higado_res", "pezuña_res",
                "chuleta_cerdo", "chorizo", "tocineta",
                "empanadas_carne", "carimañolas",
            ],
            "Lacteos": [
                "queso_fresco", "queso_parmesano", "mantequilla",
                "leche", "crema_leche", "yogurt_griego", "yogurt_natural",
            ],
            "Vegetales": [
                "tomate", "cebolla", "cebolla_larga", "lechuga", "zanahoria",
                "espinaca", "champiñones", "aji", "cilantro", "ajo",
                "pepino", "zapallo", "arvejas",
            ],
            "Frutas": ["aguacate", "banano", "fresas", "limon"],
            "Granos y Cereales": [
                "arroz", "lentejas", "frijol_negro", "avena", "pan_integral",
                "arepa", "tortilla_harina", "cereal", "harina", "pasta",
                "pan_hamburguesa", "granola", "mermelada",
            ],
            "Tuberculos": [
                "papa", "papa_francesa", "yuca", "platano_verde",
                "platano_maduro", "mazorca",
            ],
            "Condimentos": [
                "sal", "azucar", "comino", "canela", "oregano", "miel",
                "chocolate_polvo", "salsa_bbq",
            ],
            "Aceites": ["aceite", "aceite_oliva"],
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

    def get_productos_para_formulario(self):
        """Solo ingredientes que aparecen en el menu de 15 dias."""
        categorizados = set()
        por_categoria = {}
        for categoria, productos in self.categorias_productos.items():
            en_menu = [p for p in productos if p in self.inventario_necesario]
            if en_menu:
                por_categoria[categoria] = en_menu
                categorizados.update(en_menu)
        otros = sorted(p for p in self.inventario_necesario if p not in categorizados)
        if otros:
            por_categoria["Otros"] = otros
        return por_categoria

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
                    "tipo": datos_necesarios["tipo"],
                }
        return lista_compras

    def organizar_por_categorias(self, lista_compras):
        compras_organizadas = {}
        categorizados = set()
        for categoria, productos in self.categorias_productos.items():
            productos_en_categoria = {
                p: lista_compras[p] for p in productos if p in lista_compras
            }
            if productos_en_categoria:
                compras_organizadas[categoria] = productos_en_categoria
                categorizados.update(productos_en_categoria)
        otros = {p: d for p, d in lista_compras.items() if p not in categorizados}
        if otros:
            compras_organizadas["Otros"] = otros
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
            "porcentaje_completado": (productos_completos / total_productos * 100) if total_productos > 0 else 0,
        }
