import json
import os
from datetime import datetime
from typing import Callable, Dict, List, Optional

from utils.scraper import SupermarketScraper

FACTORES_CIUDAD = {
    "Bogota": 1.0,
    "Medellin": 0.95,
    "Cali": 0.93,
    "Barranquilla": 0.97,
    "Cartagena": 1.02,
    "Bucaramanga": 0.92,
    "Pereira": 0.94,
}

CACHE_FILE = "data/precios_vivos.json"
CACHE_HOURS = 24


def obtener_precios_respaldo() -> Dict[str, float]:
    return {
        "espinazo_cerdo": 9000, "pechuga_pollo": 18500, "picado_pollo": 10000,
        "muslo_pollo": 6000,
        "alitas_pollo": 12000, "menudencias_pollo": 6000,
        "carne_mechar": 22000, "bistec_res": 24000, "filete_pescado": 26000,
        "atun": 31250, "huevo": 550, "jamon": 15000, "carne_molida": 16000,
        "chicharron": 18000, "salchichas": 12000, "salchicha": 16000,
        "higado_res": 8000, "pezuña_res": 4000, "chuleta_cerdo": 18000,
        "costilla_cerdo": 19000,
        "chorizo": 3500, "tocineta": 16000,
        "empanadas_carne": 2500, "carimañolas": 3000,
        "empanadas_trigo": 3000, "empanadas_maiz": 2500,
        "costilla_res": 14000,
        "queso_fresco": 10000, "queso_mozarella": 15000, "queso_parmesano": 15000,
        "mantequilla": 16000, "leche": 3200,
        "crema_leche": 8000, "yogurt_griego": 26667,
        "tomate": 3500, "cebolla": 2800, "cebolla_larga": 2000,
        "lechuga": 5000, "zanahoria": 2200, "brocoli": 3500,
        "espinaca": 2500, "champiñones": 8000, "aji": 3000,
        "cilantro": 1000, "ajo": 12000, "pimenton": 3500,
        "pepino": 2000, "zapallo": 2500, "arvejas": 3000,
        "aguacate": 5000, "banano": 600, "fresas": 7000, "limon": 500,
        "manzana": 4000,
        "arroz": 4000, "lentejas": 3500, "frijol_negro": 4500, "frijol_rojo": 4500,
        "avena": 3500, "pan_integral": 6000, "arepa": 2000,
        "tortilla_harina": 4500, "cereal": 8000, "harina": 3000,
        "pasta": 4000, "pan_hamburguesa": 3000, "granola": 9000,
        "mermelada": 6000,
        "papa": 2200, "papa_francesa": 8000, "yuca": 2500, "platano_verde": 1500,
        "platano_maduro": 1800, "mazorca": 1500,
        "semillas_chia": 8000,
        "sal": 1500, "azucar": 3000, "comino": 2000,
        "canela": 2500, "oregano": 1500, "pimienta": 45000,
        "paprika": 50000,
        "laurel": 120000, "achiote": 40000, "nuez_moscada": 120000,
        "mostaza": 18000, "salsa_inglesa": 35000,
        "miel": 20000,
        "chocolate_polvo": 12000, "salsa_bbq": 8000,
        "crema_champinones_sobre": 4500,
        "ajinomen": 2500,
        "aceite": 5500, "aceite_oliva": 18000,
    }


class GestorPrecios:
    def __init__(self):
        self.cache_file = CACHE_FILE
        self.precios: Dict[str, Dict] = {}
        self.fecha_consulta: Optional[str] = None
        self.ciudad: str = "Bogota"
        self.scraper = SupermarketScraper()
        self._respaldo = obtener_precios_respaldo()

    def _cache_valido(self) -> bool:
        if not os.path.exists(self.cache_file):
            return False
        try:
            with open(self.cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            fecha = datetime.fromisoformat(data.get("fecha", "2000-01-01"))
            horas = (datetime.now() - fecha).total_seconds() / 3600
            return horas < CACHE_HOURS
        except Exception:
            return False

    def _cargar_cache(self) -> Dict[str, Dict]:
        try:
            with open(self.cache_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.fecha_consulta = data.get("fecha")
            return data.get("precios", {})
        except Exception:
            return {}

    def guardar_cache(self):
        try:
            os.makedirs("data", exist_ok=True)
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump({
                    "fecha": datetime.now().isoformat(),
                    "precios": self.precios,
                }, f, indent=2, ensure_ascii=False)
            self.fecha_consulta = datetime.now().isoformat()
        except Exception:
            pass

    def _aplicar_factor_ciudad(self, precio: float, ciudad: str) -> int:
        factor = FACTORES_CIUDAD.get(ciudad, 1.0)
        return round(precio * factor)

    def _precio_con_ciudad(self, info: Dict, ciudad: str) -> int:
        base = info.get("precio_base", info.get("precio_unitario", 5000))
        return self._aplicar_factor_ciudad(base, ciudad)

    def _entrada_respaldo(self, producto: str) -> Dict:
        base = self._respaldo.get(producto, 5000)
        return {
            "precio_base": base,
            "fuente": "respaldo",
            "supermercado": None,
            "confianza": "media" if producto in self._respaldo else "baja",
            "fecha_consulta": None,
        }

    def _entrada_desde_scrape(self, comparacion: Dict) -> Dict:
        mejor = comparacion["mejor_opcion"]
        supermercados = [r["supermercado"] for r in comparacion.get("resultados", [])]
        es_referencia = mejor["supermercado"] in ("D1", "Ara")
        return {
            "precio_base": mejor["precio"],
            "fuente": "scrape" if not es_referencia else "referencia",
            "supermercado": mejor["supermercado"],
            "confianza": "alta" if not es_referencia else "media",
            "fecha_consulta": datetime.now().isoformat(),
            "supermercados_consultados": supermercados,
        }

    def preparar_precios(self, lista_compras: Dict, ciudad: str) -> Dict[str, Dict]:
        """Carga caché vigente o respaldo sin consultar supermercados."""
        self.ciudad = ciudad
        productos = list(lista_compras.keys())
        if self._cache_valido():
            self.precios = self._cargar_cache()
        else:
            self.precios = {}
        for producto in productos:
            if producto not in self.precios:
                self.precios[producto] = self._entrada_respaldo(producto)
        return self.precios

    def obtener_precios(
        self,
        lista_compras: Dict,
        ciudad: str,
        forzar_actualizacion: bool = False,
        on_progress: Optional[Callable[[str], None]] = None,
    ) -> Dict[str, Dict]:
        self.ciudad = ciudad
        productos = list(lista_compras.keys())

        if not forzar_actualizacion and self._cache_valido():
            cache = self._cargar_cache()
            productos_a_buscar = [p for p in productos if p not in cache]
            self.precios = dict(cache)
        else:
            if not forzar_actualizacion and self._cache_valido():
                self.precios = self._cargar_cache()
                productos_a_buscar = [p for p in productos if p not in self.precios]
            else:
                self.precios = {}
                productos_a_buscar = list(productos)

        if forzar_actualizacion:
            productos_a_buscar = list(productos)

        for producto in productos_a_buscar:
            comparacion = self.scraper.comparar_precios_producto(
                producto, on_progress=on_progress
            )
            if comparacion.get("resultados"):
                self.precios[producto] = self._entrada_desde_scrape(comparacion)
            else:
                self.precios[producto] = self._entrada_respaldo(producto)

        for producto in productos:
            if producto not in self.precios:
                self.precios[producto] = self._entrada_respaldo(producto)

        self.guardar_cache()
        return self.precios

    def ajustar_precios_por_ciudad(self, ciudad: str):
        self.ciudad = ciudad
        return FACTORES_CIUDAD.get(ciudad, 1.0)

    def calcular_costo_lista(self, lista_compras: Dict) -> Dict:
        costo_total = 0
        desglose = {}
        for producto, datos in lista_compras.items():
            info = self.precios.get(producto) or self._entrada_respaldo(producto)
            precio_unitario = self._precio_con_ciudad(info, self.ciudad)
            cantidad = datos["cantidad"]
            tipo = datos["tipo"]
            if tipo in ("peso", "volumen"):
                costo = (precio_unitario * cantidad) / 1000
            else:
                costo = precio_unitario * cantidad
            costo_total += costo
            desglose[producto] = {
                "precio_unitario": precio_unitario,
                "cantidad": cantidad,
                "unidad": datos["unidad"],
                "costo": round(costo, 2),
                "fuente": info.get("fuente", "respaldo"),
                "supermercado": info.get("supermercado"),
                "confianza": info.get("confianza", "baja"),
            }
        return {"total": round(costo_total, 2), "desglose": desglose}

    def resumen_fuentes(self, lista_compras: Dict) -> Dict:
        productos = list(lista_compras.keys())
        en_vivo = 0
        respaldo = 0
        supermercados = set()
        for producto in productos:
            info = self.precios.get(producto, {})
            fuente = info.get("fuente", "respaldo")
            if fuente in ("scrape", "cache", "referencia"):
                en_vivo += 1
            else:
                respaldo += 1
            if info.get("supermercado"):
                supermercados.add(info["supermercado"])
        return {
            "total_productos": len(productos),
            "precios_vivos": en_vivo,
            "precios_respaldo": respaldo,
            "fecha_consulta": self.fecha_consulta,
            "supermercados": sorted(supermercados),
        }

    def cargar_respaldo_completo(self):
        for producto in self._respaldo:
            self.precios[producto] = self._entrada_respaldo(producto)

    def calcular_costo_receta(self, ingredientes: Dict) -> Dict:
        return self.calcular_costo_lista(ingredientes)
