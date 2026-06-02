"""
Scraper de precios de supermercados colombianos
Éxito, Jumbo, D1, Ara, Alkosto, Olímpica
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import streamlit as st
import json
import os
import re
from typing import Dict, Optional, List
import time

class SupermarketScraper:
    """
    Clase para obtener precios actualizados de supermercados online
    """
    
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "es-CO,es;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
        
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        
        # Mapeo de productos para búsqueda
        self.productos_busqueda = {
            "tomate": "tomate chonto",
            "cebolla": "cebolla cabezona blanca",
            "cebolla_larga": "cebolla larga",
            "lechuga": "lechuga batavia",
            "zanahoria": "zanahoria fresca",
            "brocoli": "brocoli fresco",
            "espinaca": "espinaca fresca",
            "champiñones": "champiñones frescos",
            "papa": "papa pastusa",
            "yuca": "yuca fresca",
            "platano_verde": "platano verde",
            "platano_maduro": "platano maduro",
            "mazorca": "mazorca fresca",
            "aguacate": "aguacate hass",
            "banano": "banano fresco",
            "fresas": "fresas frescas",
            "limon": "limon tahiti",
            "pechuga_pollo": "pechuga pollo fresca",
            "gallina": "gallina entera",
            "carne_mechar": "carne para mechar",
            "bistec_res": "bistec res",
            "filete_pescado": "filete pescado",
            "atun": "atun en lata",
            "huevo": "huevos AA",
            "queso_fresco": "queso campesino",
            "queso_parmesano": "queso parmesano",
            "mantequilla": "mantequilla con sal",
            "yogurt": "yogurt natural",
            "leche": "leche entera",
            "arroz": "arroz blanco",
            "lentejas": "lentejas secas",
            "frijol_negro": "frijol negro",
            "avena": "avena en hojuelas",
            "pan_integral": "pan integral tajado",
            "arepa": "arepa blanca",
            "tortilla_harina": "tortillas de harina",
            "nueces": "nueces sin cascara",
            "semillas_chia": "semillas de chia",
            "aceite": "aceite vegetal",
            "aceite_oliva": "aceite oliva extra virgen",
            "miel": "miel de abejas",
            "pimenton": "pimenton rojo",
            "pepino": "pepino fresco",
            "aji": "aji dulce",
            "cilantro": "cilantro fresco",
            "ajo": "ajo fresco",
            "oregano": "oregano seco",
            "canela": "canela en polvo",
            "comino": "comino en polvo",
            "sal": "sal de mesa",
            "arvejas": "arvejas verdes",
            "zapallo": "zapallo fresco"
        }
        
        self.cache_file = "data/precios_supermercados.json"
        self.cache_duration = 24  # horas
        
    def buscar_en_exito(self, producto: str) -> Optional[Dict]:
        """
        Busca precio en el Éxito
        """
        try:
            query = self.productos_busqueda.get(producto, producto)
            url = f"https://www.exito.com/s?q={query.replace(' ', '%20')}"
            
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Buscar precios (actualizar selectores según la página)
                productos = soup.find_all("article", {"class": "product-item"})
                
                if not productos:
                    # Intentar otros selectores
                    productos = soup.find_all("div", {"data-testid": "product"})
                
                resultados = []
                for prod in productos[:3]:  # Tomar primeros 3 resultados
                    try:
                        # Nombre del producto
                        nombre_elem = prod.find("h3") or prod.find("span", {"class": "product-name"})
                        nombre = nombre_elem.text.strip() if nombre_elem else ""
                        
                        # Precio
                        precio_elem = prod.find("span", {"class": "price"}) or \
                                     prod.find("span", {"data-testid": "price"})
                        
                        if precio_elem:
                            precio_text = precio_elem.text.strip()
                            # Extraer números del precio
                            precio_nums = re.findall(r'[\d,.]+', precio_text)
                            if precio_nums:
                                precio = float(precio_nums[0].replace('.', '').replace(',', '.'))
                                
                                resultados.append({
                                    "producto": nombre,
                                    "precio": precio,
                                    "supermercado": "Éxito",
                                    "url": url
                                })
                    except:
                        continue
                
                if resultados:
                    # Devolver el más barato
                    return min(resultados, key=lambda x: x["precio"])
                    
        except Exception as e:
            print(f"Error buscando en Éxito: {e}")
        
        return None
    
    def buscar_en_jumbo(self, producto: str) -> Optional[Dict]:
        """
        Busca precio en Jumbo Colombia
        """
        try:
            query = self.productos_busqueda.get(producto, producto)
            url = f"https://www.tiendasjumbo.co/supermercado/s?q={query.replace(' ', '%20')}"
            
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Buscar productos
                productos = soup.find_all("div", {"class": "product-item"}) or \
                           soup.find_all("li", {"class": "product"})
                
                resultados = []
                for prod in productos[:3]:
                    try:
                        nombre_elem = prod.find("h2") or prod.find("span", {"class": "name"})
                        nombre = nombre_elem.text.strip() if nombre_elem else ""
                        
                        precio_elem = prod.find("span", {"class": "price"}) or \
                                     prod.find("div", {"class": "price"})
                        
                        if precio_elem:
                            precio_text = precio_elem.text.strip()
                            precio_nums = re.findall(r'[\d,.]+', precio_text)
                            if precio_nums:
                                precio = float(precio_nums[0].replace('.', '').replace(',', '.'))
                                resultados.append({
                                    "producto": nombre,
                                    "precio": precio,
                                    "supermercado": "Jumbo",
                                    "url": url
                                })
                    except:
                        continue
                
                if resultados:
                    return min(resultados, key=lambda x: x["precio"])
                    
        except Exception as e:
            print(f"Error buscando en Jumbo: {e}")
        
        return None
    
    def buscar_en_d1(self, producto: str) -> Optional[Dict]:
        """
        Obtiene precios de Tiendas D1
        Nota: D1 no tiene ecommerce, usamos precios de referencia
        """
        # Precios de referencia D1 (actualizados semanalmente)
        precios_d1 = {
            "tomate": 2500, "cebolla": 1800, "lechuga": 1800,
            "zanahoria": 1800, "papa": 1500, "platano_verde": 1000,
            "aguacate": 3000, "banano": 1800, "limon": 500,
            "huevo": 450, "arroz": 3200, "lentejas": 2500,
            "frijol_negro": 3200, "avena": 2500, "arepa": 1800,
            "aceite": 4500, "sal": 1200, "pan_integral": 4000
        }
        
        if producto in precios_d1:
            return {
                "producto": self.productos_busqueda.get(producto, producto),
                "precio": precios_d1[producto],
                "supermercado": "D1",
                "url": "https://www.tiendasd1.com"
            }
        return None
    
    def buscar_en_ara(self, producto: str) -> Optional[Dict]:
        """
        Precios de referencia Tiendas Ara
        """
        precios_ara = {
            "tomate": 2800, "cebolla": 2000, "papa": 1600,
            "zanahoria": 1900, "aguacate": 3200, "huevo": 480,
            "arroz": 3500, "lentejas": 2800, "aceite": 4800,
            "leche": 2800, "arepa": 2000
        }
        
        if producto in precios_ara:
            return {
                "producto": self.productos_busqueda.get(producto, producto),
                "precio": precios_ara[producto],
                "supermercado": "Ara",
                "url": "https://www.tiendasara.com"
            }
        return None
    
    def buscar_en_olimpica(self, producto: str) -> Optional[Dict]:
        """
        Busca precio en Olímpica
        """
        try:
            query = self.productos_busqueda.get(producto, producto)
            url = f"https://www.olimpica.com/s?q={query.replace(' ', '%20')}"
            
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                productos = soup.find_all("div", {"class": "product"})[:3]
                resultados = []
                
                for prod in productos:
                    try:
                        nombre = prod.find("h3").text.strip() if prod.find("h3") else ""
                        precio_text = prod.find("span", {"class": "price"}).text.strip()
                        precio_nums = re.findall(r'[\d,.]+', precio_text)
                        if precio_nums:
                            precio = float(precio_nums[0].replace('.', '').replace(',', '.'))
                            resultados.append({
                                "producto": nombre,
                                "precio": precio,
                                "supermercado": "Olímpica",
                                "url": url
                            })
                    except:
                        continue
                
                if resultados:
                    return min(resultados, key=lambda x: x["precio"])
                    
        except Exception as e:
            print(f"Error buscando en Olímpica: {e}")
        
        return None
    
    def comparar_precios_producto(self, producto: str) -> Dict:
        """
        Compara precios de un producto en diferentes supermercados
        """
        resultados = []
        
        # Buscar en todos los supermercados
        with st.spinner(f"Buscando {producto} en supermercados..."):
            exito = self.buscar_en_exito(producto)
            if exito:
                resultados.append(exito)
            
            jumbo = self.buscar_en_jumbo(producto)
            if jumbo:
                resultados.append(jumbo)
            
            d1 = self.buscar_en_d1(producto)
            if d1:
                resultados.append(d1)
            
            ara = self.buscar_en_ara(producto)
            if ara:
                resultados.append(ara)
            
            olimpica = self.buscar_en_olimpica(producto)
            if olimpica:
                resultados.append(olimpica)
        
        if resultados:
            # Ordenar por precio
            resultados.sort(key=lambda x: x["precio"])
            
            mejor = resultados[0]
            peor = resultados[-1]
            
            return {
                "producto": producto,
                "resultados": resultados,
                "mejor_opcion": {
                    "supermercado": mejor["supermercado"],
                    "precio": mejor["precio"]
                },
                "rango_precios": {
                    "minimo": mejor["precio"],
                    "maximo": peor["precio"],
                    "promedio": sum(r["precio"] for r in resultados) / len(resultados)
                },
                "ahorro_potencial": peor["precio"] - mejor["precio"]
            }
        
        return {
            "producto": producto,
            "resultados": [],
            "error": "No se encontraron resultados"
        }
    
    def calcular_costo_total_optimizado(self, lista_compras: Dict) -> Dict:
        """
        Calcula el costo total buscando el mejor precio en cada supermercado
        """
        resultado_final = {
            "total_optimizado": 0,
            "desglose": {},
            "por_supermercado": {},
            "ahorro_total": 0
        }
        
        total_supermercados = {}
        
        for producto, datos in lista_compras.items():
            comparacion = self.comparar_precios_producto(producto)
            
            if comparacion.get("resultados"):
                mejor = comparacion["mejor_opcion"]
                
                # Acumular por supermercado
                superm = mejor["supermercado"]
                if superm not in total_supermercados:
                    total_supermercados[superm] = 0
                
                costo = mejor["precio"] * datos["cantidad"]
                total_supermercados[superm] += costo
                
                resultado_final["desglose"][producto] = {
                    "mejor_precio": mejor["precio"],
                    "supermercado": superm,
                    "cantidad": datos["cantidad"],
                    "costo_total": round(costo, 2)
                }
                
                resultado_final["total_optimizado"] += costo
                resultado_final["ahorro_total"] += comparacion.get("ahorro_potencial", 0)
        
        resultado_final["total_optimizado"] = round(resultado_final["total_optimizado"], 2)
        resultado_final["ahorro_total"] = round(resultado_final["ahorro_total"], 2)
        resultado_final["por_supermercado"] = total_supermercados
        
        return resultado_final
    
    def guardar_cache(self, datos: Dict):
        """Guarda resultados en caché"""
        try:
            os.makedirs("data", exist_ok=True)
            datos["timestamp"] = datetime.now().isoformat()
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando caché: {e}")
    
    def cargar_cache(self) -> Optional[Dict]:
        """Carga resultados desde caché si son recientes"""
        try:
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    
                    timestamp = datetime.fromisoformat(datos.get("timestamp", "2000-01-01"))
                    horas_transcurridas = (datetime.now() - timestamp).total_seconds() / 3600
                    
                    if horas_transcurridas < self.cache_duration:
                        return datos
        except Exception as e:
            print(f"Error cargando caché: {e}")
        return None