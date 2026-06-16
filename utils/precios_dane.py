import json
import os
from datetime import datetime

class PreciosActualizados:
    def __init__(self):
        self.cache_file = "data/precios_cache.json"
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
        return self._obtener_precios_semanales()
    
    def _obtener_precios_semanales(self):
        precios = {
            "espinazo_cerdo": 9000, "pechuga_pollo": 18500, "muslo_pollo": 14000,
            "alitas_pollo": 12000, "menudencias_pollo": 6000,
            "carne_mechar": 22000, "bistec_res": 24000, "filete_pescado": 26000,
            "atun": 5000, "huevo": 550, "jamon": 15000, "carne_molida": 16000,
            "chicharron": 18000, "salchichas": 12000, "salchicha": 8000,
            "higado_res": 8000, "pezuña_res": 10000, "chuleta_cerdo": 18000,
            "chorizo": 14000, "tocineta": 16000,
            "queso_fresco": 10000, "queso_parmesano": 15000,
            "mantequilla": 16000, "yogurt": 3500, "leche": 3200,
            "crema_leche": 8000, "cuajada": 7000,
            "tomate": 3500, "cebolla": 2800, "cebolla_larga": 2000,
            "lechuga": 2500, "zanahoria": 2200, "brocoli": 3500,
            "espinaca": 2500, "champiñones": 8000, "aji": 3000,
            "cilantro": 1000, "ajo": 12000, "pimenton": 3500,
            "pepino": 2000, "zapallo": 2500, "arvejas": 3000,
            "aguacate": 5000, "banano": 2500, "fresas": 7000, "limon": 500,
            "arroz": 4000, "lentejas": 3500, "frijol_negro": 4500,
            "avena": 3500, "pan_integral": 6000, "arepa": 2000,
            "tortilla_harina": 4500, "cereal": 8000, "harina": 3000,
            "pasta": 4000, "pan_hamburguesa": 3000, "granola": 9000,
            "mermelada": 6000,
            "papa": 2200, "yuca": 2500, "platano_verde": 1500,
            "platano_maduro": 1800, "mazorca": 1500,
            "semillas_chia": 8000,
            "sal": 1500, "azucar": 3000, "comino": 2000,
            "canela": 2500, "oregano": 1500, "miel": 10000,
            "chocolate_polvo": 12000, "salsa_bbq": 8000,
            "aceite": 5500, "aceite_oliva": 18000
        }
        return precios
    
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