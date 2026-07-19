"""
Scraper de precios de supermercados colombianos.
Éxito, Jumbo, Olímpica (Selenium) + referencia D1/Ara.
"""

import json
import os
import re
import time
from datetime import datetime
from typing import Callable, Dict, List, Optional

import requests
from bs4 import BeautifulSoup

from utils.producto_catalogo import PRESENTACIONES, PRODUCTOS_BUSQUEDA

PRODUCTO_TIMEOUT = 15


class SupermarketScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-CO,es;q=0.9",
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.productos_busqueda = PRODUCTOS_BUSQUEDA
        self.presentaciones = PRESENTACIONES
        self.cache_file = "data/precios_supermercados.json"
        self.cache_duration = 24
        self._driver = None
        self._selenium_disponible = None

    def __del__(self):
        self._cerrar_driver()

    def _cerrar_driver(self):
        if self._driver is not None:
            try:
                self._driver.quit()
            except Exception:
                pass
            self._driver = None

    def _selenium_ok(self) -> bool:
        if self._selenium_disponible is not None:
            return self._selenium_disponible
        try:
            from selenium import webdriver  # noqa: F401
            self._selenium_disponible = True
        except ImportError:
            self._selenium_disponible = False
        return self._selenium_disponible

    def _get_driver(self):
        if self._driver is not None:
            return self._driver
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument(f"user-agent={self.headers['User-Agent']}")
        service = Service(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=service, options=options)
        self._driver.set_page_load_timeout(PRODUCTO_TIMEOUT)
        return self._driver

    @staticmethod
    def _parse_precio(texto: str) -> Optional[float]:
        if not texto:
            return None
        nums = re.findall(r"[\d.,]+", texto.replace("$", "").strip())
        if not nums:
            return None
        valor = nums[0].replace(".", "").replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            return None

    def normalizar_precio_paquete(self, producto: str, precio_paquete: float) -> float:
        """Convierte precio de empaque a precio unitario (COP/kg, COP/L o COP/unidad)."""
        info = self.presentaciones.get(producto, {"tipo": "peso"})
        tipo = info.get("tipo", "peso")

        if tipo == "peso":
            gramos = info.get("gramos_por_paquete")
            if gramos:
                return (precio_paquete / gramos) * 1000
            return precio_paquete

        if tipo == "volumen":
            ml = info.get("ml_por_paquete")
            if ml:
                return (precio_paquete / ml) * 1000
            return precio_paquete

        unidades = info.get("unidades_por_paquete", 1)
        return precio_paquete / unidades

    def _buscar_con_selenium(self, url: str, supermercado: str) -> List[Dict]:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait

        resultados = []
        driver = self._get_driver()
        try:
            driver.get(url)
            WebDriverWait(driver, PRODUCTO_TIMEOUT).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            time.sleep(2)
            html = driver.page_source
        except Exception:
            return resultados

        soup = BeautifulSoup(html, "html.parser")
        selectores = [
            ("article", {"class": re.compile(r"product", re.I)}),
            ("div", {"data-testid": re.compile(r"product", re.I)}),
            ("li", {"class": re.compile(r"product", re.I)}),
            ("div", {"class": re.compile(r"product-card|product-item|vtex-product", re.I)}),
        ]
        productos = []
        for tag, attrs in selectores:
            productos = soup.find_all(tag, attrs)
            if productos:
                break

        for prod in productos[:5]:
            try:
                nombre_elem = (
                    prod.find("h2") or prod.find("h3") or prod.find("h4")
                    or prod.find("span", class_=re.compile(r"name|title", re.I))
                )
                nombre = nombre_elem.get_text(strip=True) if nombre_elem else ""

                precio_elem = (
                    prod.find("span", class_=re.compile(r"price|selling", re.I))
                    or prod.find("div", class_=re.compile(r"price", re.I))
                    or prod.find("span", {"data-testid": re.compile(r"price", re.I)})
                )
                if not precio_elem:
                    continue
                precio = self._parse_precio(precio_elem.get_text())
                if precio and precio > 0:
                    resultados.append({
                        "producto": nombre,
                        "precio_paquete": precio,
                        "supermercado": supermercado,
                        "url": url,
                    })
            except Exception:
                continue

        if not resultados:
            for match in re.finditer(r"\$\s*([\d.,]+)", html):
                precio = self._parse_precio(match.group(1))
                if precio and 100 < precio < 500000:
                    resultados.append({
                        "producto": "",
                        "precio_paquete": precio,
                        "supermercado": supermercado,
                        "url": url,
                    })
                    break

        return resultados

    def _buscar_con_requests(self, url: str, supermercado: str) -> List[Dict]:
        resultados = []
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code != 200:
                return resultados
            soup = BeautifulSoup(response.content, "html.parser")
            for prod in soup.find_all(["article", "div", "li"], limit=20):
                clases = " ".join(prod.get("class", []))
                if "product" not in clases.lower() and prod.get("data-testid") != "product":
                    continue
                precio_elem = prod.find("span", class_=re.compile(r"price", re.I))
                if not precio_elem:
                    continue
                precio = self._parse_precio(precio_elem.get_text())
                if precio and precio > 0:
                    nombre_elem = prod.find(["h2", "h3", "span"])
                    resultados.append({
                        "producto": nombre_elem.get_text(strip=True) if nombre_elem else "",
                        "precio_paquete": precio,
                        "supermercado": supermercado,
                        "url": url,
                    })
        except Exception:
            pass
        return resultados[:3]

    def _buscar_en_tienda(self, producto: str, base_url: str, supermercado: str) -> Optional[Dict]:
        query = self.productos_busqueda.get(producto, producto.replace("_", " "))
        url = f"{base_url}{query.replace(' ', '%20')}"

        resultados = []
        if self._selenium_ok():
            try:
                resultados = self._buscar_con_selenium(url, supermercado)
            except Exception:
                self._cerrar_driver()
                resultados = self._buscar_con_requests(url, supermercado)
        else:
            resultados = self._buscar_con_requests(url, supermercado)

        if not resultados:
            return None

        mejor = min(resultados, key=lambda x: x["precio_paquete"])
        precio_unitario = self.normalizar_precio_paquete(producto, mejor["precio_paquete"])
        return {
            "producto": mejor.get("producto") or query,
            "precio": round(precio_unitario, 2),
            "precio_paquete": mejor["precio_paquete"],
            "supermercado": supermercado,
            "url": url,
        }

    def buscar_en_exito(self, producto: str) -> Optional[Dict]:
        return self._buscar_en_tienda(producto, "https://www.exito.com/s?q=", "Éxito")

    def buscar_en_jumbo(self, producto: str) -> Optional[Dict]:
        return self._buscar_en_tienda(
            producto,
            "https://www.tiendasjumbo.co/supermercado/s?q=",
            "Jumbo",
        )

    def buscar_en_olimpica(self, producto: str) -> Optional[Dict]:
        return self._buscar_en_tienda(producto, "https://www.olimpica.com/s?q=", "Olímpica")

    def buscar_en_d1(self, producto: str) -> Optional[Dict]:
        precios_d1 = {
            "tomate": 2500, "cebolla": 1800, "lechuga": 1800, "zanahoria": 1800,
            "papa": 1500, "platano_verde": 1000, "aguacate": 3000, "banano": 1800,
            "limon": 500, "huevo": 13500, "arroz": 3200, "lentejas": 2500,
            "frijol_negro": 3200, "frijol_rojo": 3200, "avena": 2500, "arepa": 1800,
            "aceite": 4500, "sal": 1200, "pan_integral": 4000, "leche": 2900,
            "muslo_pollo": 13000, "pechuga_pollo": 17000, "yogurt_griego": 3500,
        }
        if producto not in precios_d1:
            return None
        precio_unitario = self.normalizar_precio_paquete(producto, precios_d1[producto])
        return {
            "producto": self.productos_busqueda.get(producto, producto),
            "precio": round(precio_unitario, 2),
            "precio_paquete": precios_d1[producto],
            "supermercado": "D1",
            "url": "https://www.tiendasd1.com",
        }

    def buscar_en_ara(self, producto: str) -> Optional[Dict]:
        precios_ara = {
            "tomate": 2800, "cebolla": 2000, "papa": 1600, "zanahoria": 1900,
            "aguacate": 3200, "huevo": 14400, "arroz": 3500, "lentejas": 2800,
            "aceite": 4800, "leche": 2800, "arepa": 2000, "pan_integral": 4200,
        }
        if producto not in precios_ara:
            return None
        precio_unitario = self.normalizar_precio_paquete(producto, precios_ara[producto])
        return {
            "producto": self.productos_busqueda.get(producto, producto),
            "precio": round(precio_unitario, 2),
            "precio_paquete": precios_ara[producto],
            "supermercado": "Ara",
            "url": "https://www.tiendasara.com",
        }

    def comparar_precios_producto(
        self,
        producto: str,
        on_progress: Optional[Callable[[str], None]] = None,
    ) -> Dict:
        if on_progress:
            on_progress(producto)

        buscadores = [
            self.buscar_en_exito,
            self.buscar_en_jumbo,
            self.buscar_en_olimpica,
            self.buscar_en_d1,
            self.buscar_en_ara,
        ]
        resultados = []
        for buscar in buscadores:
            try:
                resultado = buscar(producto)
                if resultado:
                    resultados.append(resultado)
            except Exception:
                continue
            time.sleep(0.5)

        if resultados:
            resultados.sort(key=lambda x: x["precio"])
            mejor = resultados[0]
            peor = resultados[-1]
            return {
                "producto": producto,
                "resultados": resultados,
                "mejor_opcion": {
                    "supermercado": mejor["supermercado"],
                    "precio": mejor["precio"],
                },
                "rango_precios": {
                    "minimo": mejor["precio"],
                    "maximo": peor["precio"],
                    "promedio": sum(r["precio"] for r in resultados) / len(resultados),
                },
                "ahorro_potencial": peor["precio"] - mejor["precio"],
            }

        return {"producto": producto, "resultados": [], "error": "No se encontraron resultados"}

    def _calcular_costo_item(self, precio_unitario: float, datos: Dict) -> float:
        cantidad = datos["cantidad"]
        tipo = datos["tipo"]
        if tipo in ("peso", "volumen"):
            return (precio_unitario * cantidad) / 1000
        return precio_unitario * cantidad

    def calcular_costo_total_optimizado(
        self,
        lista_compras: Dict,
        on_progress: Optional[Callable[[str], None]] = None,
    ) -> Dict:
        resultado_final = {
            "total_optimizado": 0,
            "desglose": {},
            "por_supermercado": {},
            "ahorro_total": 0,
        }
        total_supermercados = {}

        for producto, datos in lista_compras.items():
            comparacion = self.comparar_precios_producto(producto, on_progress=on_progress)
            if not comparacion.get("resultados"):
                continue

            mejor = comparacion["mejor_opcion"]
            superm = mejor["supermercado"]
            costo = self._calcular_costo_item(mejor["precio"], datos)

            if superm not in total_supermercados:
                total_supermercados[superm] = 0
            total_supermercados[superm] += costo

            resultado_final["desglose"][producto] = {
                "mejor_precio": mejor["precio"],
                "supermercado": superm,
                "cantidad": datos["cantidad"],
                "costo_total": round(costo, 2),
            }
            resultado_final["total_optimizado"] += costo
            resultado_final["ahorro_total"] += comparacion.get("ahorro_potencial", 0)

        resultado_final["total_optimizado"] = round(resultado_final["total_optimizado"], 2)
        resultado_final["ahorro_total"] = round(resultado_final["ahorro_total"], 2)
        resultado_final["por_supermercado"] = total_supermercados
        return resultado_final

    def guardar_cache(self, datos: Dict):
        try:
            os.makedirs("data", exist_ok=True)
            datos["timestamp"] = datetime.now().isoformat()
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando caché: {e}")

    def cargar_cache(self) -> Optional[Dict]:
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                timestamp = datetime.fromisoformat(datos.get("timestamp", "2000-01-01"))
                horas = (datetime.now() - timestamp).total_seconds() / 3600
                if horas < self.cache_duration:
                    return datos
        except Exception as e:
            print(f"Error cargando caché: {e}")
        return None
