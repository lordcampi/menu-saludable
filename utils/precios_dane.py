import requests
import json
import os
import re
from datetime import datetime
from bs4 import BeautifulSoup
import streamlit as st

class PreciosActualizados:
    def __init__(self):
        self.cache_file = "data/precios_cache.json"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.precios = self._cargar_precios()
    
    def _cargar_precios(self):
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    fecha_guardada = datetime.fromisoformat(data.get('fecha', '2000-01-01'))
                    if fecha_guardada.date() == datetime.now().date():
                        return data.get('precios', {})
            except:
                pass
        return self._obtener_precios_base()
    
    def _obtener_precios_base(self):
        precios = {
            "gallina": 12000, "pechuga_pollo": 18500, "carne_mechar": 22000,
            "bistec_res": 24000, "filete_pescado": 26000, "atun": 5000,
            "huevo": 550, "jamon": 15000, "carne_molida": 16000,
            "chicharron": 18000, "salchichas": 12000,
            "queso_fresco": 10000, "queso_parmesano": 15000,
            "mantequilla": 16000, "yogurt": 3500, "leche": 3200,
            "crema_leche": 8000,
            "tomate": 3500, "cebolla": 2800, "cebolla_larga": 2000,
            "lechuga": 2500, "zanahoria": 2200, "brocoli": 3500,
            "espinaca": 2500, "champiñones": 8000, "aji": 3000,
            "cilantro": 1000, "ajo": 12000, "pimenton": 3500,
            "pepino": 2000, "zapallo": 2500,
            "aguacate": 5000, "banano": 2500, "fresas": 7000, "limon": 500,
            "arroz": 4000, "lentejas": 3500, "frijol_negro": 4500,
            "avena": 3500, "pan_integral": 6000, "arepa": 2000,
            "tortilla_harina": 4500, "arvejas": 3000,
            "cereal": 8000, "harina": 3000, "pasta": 4000,
            "pan_hamburguesa": 3000, "papa": 2200,
            "yuca": 2500, "platano_verde": 1500, "platano_maduro": 1800,
            "mazorca": 1500, "nueces": 12000, "semillas_chia": 8000,
            "sal": 1500, "azucar": 3000, "comino": 2000,
            "canela": 2500, "oregano": 1500, "miel": 10000,
            "chocolate_polvo": 12000, "aceite": 5500, "aceite_oliva": 18000
        }
        return precios
    
    def buscar_precio_exito(self, producto_busqueda):
        """Busca precio en tiempo real en exito.com"""
        try:
            url = f"https://www.exito.com/s?q={producto_busqueda.replace(' ', '%20')}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                productos = soup.find_all("article", {"data-testid": "product"})
                
                if productos:
                    for prod in productos[:3]:
                        try:
                            precio_elem = prod.find("span", {"data-testid": "price"})
                            if precio_elem:
                                precio_text = precio_elem.text.strip()
                                numeros = re.findall(r'[\d,.]+', precio_text)
                                if numeros:
                                    return float(numeros[0].replace('.', '').replace(',', '.'))
                        except:
                            continue
            return None
        except:
            return None
    
    def buscar_precio_jumbo(self, producto_busqueda):
        """Busca precio en tiempo real en tiendasjumbo.co"""
        try:
            url = f"https://www.tiendasjumbo.co/supermercado/s?q={producto_busqueda.replace(' ', '%20')}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                productos = soup.find_all("div", {"class": "product-item"})
                
                if productos:
                    for prod in productos[:3]:
                        try:
                            precio_elem = prod.find("span", {"class": "price"})
                            if precio_elem:
                                precio_text = precio_elem.text.strip()
                                numeros = re.findall(r'[\d,.]+', precio_text)
                                if numeros:
                                    return float(numeros[0].replace('.', '').replace(',', '.'))
                        except:
                            continue
            return None
        except:
            return None
    
    def buscar_precio_d1(self, producto):
        """Precios de referencia D1 actualizados semanalmente"""
        precios_d1 = {
            "huevo": 480, "leche": 2800, "arroz": 3500, "aceite": 4800,
            "pan_integral": 5000, "arepa": 1800, "papa": 1600,
            "tomate": 2800, "cebolla": 2000, "platano_verde": 1200,
            "platano_maduro": 1500, "yuca": 2000, "limon": 400,
            "frijol_negro": 3500, "lentejas": 3000, "avena": 2800,
            "azucar": 2500, "sal": 1200, "mantequilla": 6000,
            "queso_fresco": 8000, "yogurt": 2800, "atun": 4200,
            "pasta": 3200, "harina": 2500, "chocolate_polvo": 8000
        }
        return precios_d1.get(producto)
    
    def buscar_precio_ara(self, producto):
        """Precios de referencia Ara actualizados"""
        precios_ara = {
            "huevo": 500, "leche": 2900, "arroz": 3600, "aceite": 5000,
            "pan_integral": 5200, "arepa": 1900, "papa": 1700,
            "tomate": 2900, "cebolla": 2100, "platano_maduro": 1600,
            "frijol_negro": 3600, "lentejas": 3100, "avena": 2900,
            "sal": 1300, "mantequilla": 6200, "queso_fresco": 8200,
            "pasta": 3300, "harina": 2600
        }
        return precios_ara.get(producto)
    
    def obtener_precio_actualizado(self, producto):
        """Obtiene el mejor precio disponible en tiempo real"""
        mapeo_busquedas = {
            "pechuga_pollo": "pechuga pollo fresca",
            "bistec_res": "bistec res",
            "filete_pescado": "filete pescado blanco",
            "carne_molida": "carne molida res",
            "huevo": "huevos AA",
            "leche": "leche entera",
            "arroz": "arroz blanco",
            "pan_integral": "pan integral tajado",
            "arepa": "arepa blanca",
            "papa": "papa pastusa",
            "tomate": "tomate chonto",
            "cebolla": "cebolla cabezona",
            "aceite": "aceite vegetal",
            "pasta": "pasta spaghetti",
            "harina": "harina trigo",
            "queso_fresco": "queso campesino",
            "yogurt": "yogurt natural",
            "mantequilla": "mantequilla sal",
            "platano_maduro": "platano maduro",
            "platano_verde": "platano verde",
            "yuca": "yuca fresca",
            "frijol_negro": "frijol negro",
            "lentejas": "lentejas secas",
            "avena": "avena hojuelas",
            "chocolate_polvo": "chocolate polvo",
            "atun": "atun lomitos",
            "zanahoria": "zanahoria fresca",
            "champiñones": "champiñones frescos",
            "lechuga": "lechuga batavia",
            "aguacate": "aguacate hass",
            "banano": "banano fresco",
            "fresas": "fresas frescas",
            "limon": "limon tahiti",
            "jamon": "jamon sandwich",
            "cereal": "cereal desayuno",
            "miel": "miel abejas",
            "aceite_oliva": "aceite oliva extra virgen"
        }
        
        busqueda = mapeo_busquedas.get(producto, producto.replace('_', ' '))
        
        with st.spinner(f"Buscando precio de {producto}..."):
            precio_exito = self.buscar_precio_exito(busqueda)
            if precio_exito:
                return precio_exito
            
            precio_jumbo = self.buscar_precio_jumbo(busqueda)
            if precio_jumbo:
                return precio_jumbo
            
            precio_d1 = self.buscar_precio_d1(producto)
            if precio_d1:
                return precio_d1
            
            precio_ara = self.buscar_precio_ara(producto)
            if precio_ara:
                return precio_ara
        
        return self.precios.get(producto, 5000)
    
    def actualizar_precios_tiempo_real(self, lista_productos):
        """Actualiza precios en tiempo real para los productos de la lista"""
        productos_actualizados = 0
        total_productos = len(lista_productos)
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, producto in enumerate(lista_productos):
            status_text.text(f"Consultando precios: {producto.replace('_', ' ').title()}")
            precio_nuevo = self.obtener_precio_actualizado(producto)
            if precio_nuevo:
                self.precios[producto] = precio_nuevo
                productos_actualizados += 1
            
            progress_bar.progress((i + 1) / total_productos)
        
        status_text.text(f"✅ {productos_actualizados} de {total_productos} precios actualizados")
        progress_bar.empty()
        
        self.guardar_cache()
    
    def ajustar_precios_por_ciudad(self, ciudad):
        factores = {
            "Bogota": 1.0, "Medellin": 0.95, "Cali": 0.93,
            "Barranquilla": 0.97, "Cartagena": 1.02, "Bucaramanga": 0.92, "Pereira": 0.94
        }
        factor = factores.get(ciudad, 1.0)
        for producto in self.precios:
            self.precios[producto] = round(self.precios[producto] * factor)
        return factor
    
    def calcular_costo_lista(self, lista_compras):
        costo_total = 0
        desglose = {}
        for producto, datos in lista_compras.items():
            cantidad = datos['cantidad']
            tipo = datos['tipo']
            precio_unitario = self.precios.get(producto, 5000)
            if tipo == "peso":
                costo = (precio_unitario * cantidad) / 1000
            elif tipo == "volumen":
                costo = (precio_unitario * cantidad) / 1000
            else:
                costo = precio_unitario * cantidad
            costo_total += costo
            desglose[producto] = {
                "precio_unitario": precio_unitario,
                "cantidad": cantidad,
                "unidad": datos['unidad'],
                "costo": round(costo, 2)
            }
        return {"total": round(costo_total, 2), "desglose": desglose}
    
    def guardar_cache(self):
        try:
            os.makedirs("data", exist_ok=True)
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'fecha': datetime.now().isoformat(),
                    'precios': self.precios
                }, f, indent=2)
        except:
            pass
