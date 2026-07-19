from collections import defaultdict
import json
import math
import os


INVENTARIO_FILE = "data/inventario_usuario.json"

PROTEINAS_CONGELABLES = {
    "espinazo_cerdo", "pechuga_pollo", "muslo_pollo", "alitas_pollo",
    "menudencias_pollo", "carne_mechar", "bistec_res", "filete_pescado",
    "carne_molida", "chicharron", "pezuña_res", "chuleta_cerdo",
    "costilla_cerdo", "empanadas_carne", "carimañolas",
}


class InventoryManager:
    CATEGORIAS_PERECEDEROS = ("Frutas", "Vegetales", "Tuberculos", "Lacteos")
    PERECEDEROS_ADICIONALES = {
        "jamon", "tocineta", "chorizo", "salchicha", "salchichas",
    }

    def __init__(self, menu):
        self.menu = menu
        self.inventario_necesario = self._calcular_inventario_total()
        self.inventario_actual = self._cargar_inventario()
        self.categorias_productos = {
            "Proteinas": [
                "espinazo_cerdo", "pechuga_pollo", "muslo_pollo", "alitas_pollo",
                "menudencias_pollo", "carne_mechar", "bistec_res", "filete_pescado",
                "atun", "huevo", "jamon", "carne_molida", "chicharron",
                "salchichas", "salchicha", "pezuña_res", "costilla_cerdo",
                "chuleta_cerdo", "chorizo", "tocineta",
                "empanadas_carne", "carimañolas",
            ],
            "Lacteos": [
                "queso_fresco", "queso_parmesano", "mantequilla",
                "leche", "crema_leche", "yogurt_griego",
            ],
            "Vegetales": [
                "tomate", "cebolla", "cebolla_larga", "lechuga", "zanahoria",
                "espinaca", "champiñones", "aji", "cilantro", "ajo",
                "pepino", "zapallo", "arvejas",
            ],
            "Frutas": ["aguacate", "banano", "fresas", "limon"],
            "Granos y Cereales": [
                "arroz", "lentejas", "frijol_negro", "frijol_rojo", "avena",
                "pan_integral", "arepa", "tortilla_harina", "cereal", "harina",
                "pasta", "pan_hamburguesa", "granola", "mermelada",
            ],
            "Tuberculos": [
                "papa", "papa_francesa", "yuca", "platano_verde",
                "platano_maduro", "mazorca",
            ],
            "Condimentos": [
                "sal", "azucar", "comino", "canela", "oregano", "miel",
                "pimienta", "paprika", "polvo_hornear",
                "chocolate_polvo", "salsa_bbq", "crema_champinones_sobre",
            ],
            "Aceites": ["aceite", "aceite_oliva"],
        }

    def get_ingredientes_perecederos(self):
        perecederos = set()
        for categoria in self.CATEGORIAS_PERECEDEROS:
            perecederos.update(self.categorias_productos.get(categoria, []))
        perecederos.update(self.PERECEDEROS_ADICIONALES)
        return perecederos

    def _calcular_inventario_rango(self, dia_inicio, dia_fin):
        inventario = defaultdict(lambda: {"cantidad": 0, "unidad": "", "tipo": ""})
        for dia in self.menu:
            if not (dia_inicio <= dia["dia"] <= dia_fin):
                continue
            for comida in ["desayuno", "almuerzo", "cena"]:
                for ingrediente, datos in dia[comida]["ingredientes"].items():
                    inventario[ingrediente]["cantidad"] += datos["cantidad"]
                    inventario[ingrediente]["unidad"] = datos["unidad"]
                    inventario[ingrediente]["tipo"] = datos["tipo"]
        return dict(inventario)

    def _calcular_inventario_total(self):
        if not self.menu:
            return {}
        return self._calcular_inventario_rango(
            self.menu[0]["dia"],
            self.menu[-1]["dia"],
        )

    def get_productos_para_formulario(self):
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

    def _cargar_inventario(self):
        if not os.path.exists(INVENTARIO_FILE):
            return {}
        try:
            with open(INVENTARIO_FILE, "r", encoding="utf-8") as f:
                return self._normalizar_inventario(json.load(f))
        except Exception:
            return {}

    def _normalizar_inventario(self, inventario):
        if not isinstance(inventario, dict):
            return {}
        normalizado = {}
        for ingrediente, cantidad in inventario.items():
            if ingrediente not in self.inventario_necesario:
                continue
            try:
                valor = float(cantidad)
            except (TypeError, ValueError):
                continue
            if not math.isfinite(valor) or valor < 0:
                continue
            normalizado[ingrediente] = round(valor, 1)
        return normalizado

    def _guardar_inventario(self):
        try:
            os.makedirs("data", exist_ok=True)
            with open(INVENTARIO_FILE, "w", encoding="utf-8") as f:
                json.dump(self.inventario_actual, f, indent=2)
            return True
        except Exception:
            return False

    def actualizar_inventario_actual(self, inventario_dict):
        self.inventario_actual = self._normalizar_inventario(inventario_dict)
        return self._guardar_inventario()

    def _generar_lista_desde_inventario(self, inventario, filtro=None, excluir=None):
        lista_compras = {}
        for ingrediente, datos_necesarios in inventario.items():
            if filtro is not None and ingrediente not in filtro:
                continue
            if excluir is not None and ingrediente in excluir:
                continue
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

    def generar_lista_compras(self):
        return self._generar_lista_desde_inventario(self.inventario_necesario)

    def generar_lista_compras_quincenal(self):
        perecederos = self.get_ingredientes_perecederos()
        return self._generar_lista_desde_inventario(
            self.inventario_necesario,
            excluir=perecederos,
        )

    def generar_listas_compras_semanales(self):
        perecederos = self.get_ingredientes_perecederos()
        saldo = {
            ingrediente: float(cantidad)
            for ingrediente, cantidad in self.inventario_actual.items()
        }

        def generar_semana(inventario):
            compras = {}
            for ingrediente, datos in inventario.items():
                if ingrediente not in perecederos:
                    continue
                necesario = datos["cantidad"]
                disponible = saldo.get(ingrediente, 0)
                usado = min(necesario, disponible)
                saldo[ingrediente] = disponible - usado
                faltante = necesario - usado
                if faltante > 0:
                    compras[ingrediente] = {
                        "cantidad": round(faltante, 1),
                        "unidad": datos["unidad"],
                        "tipo": datos["tipo"],
                    }
            return compras

        return {
            "semana_1": generar_semana(self._calcular_inventario_rango(1, 7)),
            "semana_2": generar_semana(self._calcular_inventario_rango(8, 15)),
        }

    def generar_porciones_congelacion(self):
        """Agrupa porciones congelables y descuenta existencias del total a comprar."""
        porciones = {}
        for dia in self.menu:
            for comida in ("desayuno", "almuerzo", "cena"):
                receta = dia[comida]
                for ingrediente, datos in receta["ingredientes"].items():
                    if ingrediente not in PROTEINAS_CONGELABLES:
                        continue
                    grupo = porciones.setdefault(
                        ingrediente,
                        {
                            "usos": [],
                            "total_necesario": 0,
                            "unidad": datos["unidad"],
                        },
                    )
                    grupo["usos"].append({
                        "dia": dia["dia"],
                        "comida": comida,
                        "cantidad": datos["cantidad"],
                        "unidad": datos["unidad"],
                        "receta": receta["nombre"],
                    })
                    grupo["total_necesario"] += datos["cantidad"]

        for ingrediente, grupo in porciones.items():
            disponible = self.inventario_actual.get(ingrediente, 0)
            grupo["faltante_comprar"] = round(
                max(0, grupo["total_necesario"] - disponible),
                1,
            )
            grupo["total_necesario"] = round(grupo["total_necesario"], 1)
        return porciones

    def organizar_por_categorias(self, lista_compras, categorias=None):
        compras_organizadas = {}
        categorizados = set()
        cats = categorias or self.categorias_productos
        for categoria, productos in cats.items():
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

    def organizar_perecederos(self, lista_compras):
        cats = {
            k: v for k, v in self.categorias_productos.items()
            if k in self.CATEGORIAS_PERECEDEROS or k == "Proteinas"
        }
        return self.organizar_por_categorias(lista_compras, categorias=cats)

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
