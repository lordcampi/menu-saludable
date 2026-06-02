def _obtener_precios_base(self):
    """
    Precios base actualizados (promedio mercado colombiano)
    Precios en pesos colombianos por KG, LITRO o UNIDAD
    """
    precios = {
        # Proteínas (precio por kg o unidad)
        "gallina": 12000,
        "pechuga_pollo": 18500,
        "carne_mechar": 22000,
        "bistec_res": 24000,
        "filete_pescado": 26000,
        "atun": 5000,
        "huevo": 550,
        "jamon": 15000,
        "carne_molida": 16000,
        "chicharron": 18000,
        "salchichas": 12000,
        
        # Lácteos (precio por kg o litro)
        "queso_fresco": 10000,
        "queso_parmesano": 15000,
        "mantequilla": 16000,
        "yogurt": 3500,
        "leche": 3200,
        "crema_leche": 8000,
        
        # Vegetales (precio por kg)
        "tomate": 3500,
        "cebolla": 2800,
        "cebolla_larga": 2000,
        "lechuga": 2500,
        "zanahoria": 2200,
        "brocoli": 3500,
        "espinaca": 2500,
        "champiñones": 8000,
        "aji": 3000,
        "cilantro": 1000,
        "ajo": 12000,
        "pimenton": 3500,
        "pepino": 2000,
        "zapallo": 2500,
        
        # Frutas (precio por kg o unidad)
        "aguacate": 5000,
        "banano": 2500,
        "fresas": 7000,
        "limon": 500,
        
        # Granos y cereales (precio por kg o paquete)
        "arroz": 4000,
        "lentejas": 3500,
        "frijol_negro": 4500,
        "avena": 3500,
        "pan_integral": 6000,
        "arepa": 2000,
        "tortilla_harina": 4500,
        "arvejas": 3000,
        "cereal": 8000,
        "harina": 3000,
        "pasta": 4000,
        "pan_hamburguesa": 3000,
        
        # Tubérculos (precio por kg o unidad)
        "papa": 2200,
        "yuca": 2500,
        "platano_verde": 1500,
        "platano_maduro": 1800,
        "mazorca": 1500,
        
        # Frutos secos (precio por kg)
        "nueces": 12000,
        "semillas_chia": 8000,
        
        # Condimentos y otros
        "sal": 1500,
        "azucar": 3000,
        "comino": 2000,
        "canela": 2500,
        "oregano": 1500,
        "miel": 10000,
        "chocolate_polvo": 12000,
        
        # Aceites (precio por litro)
        "aceite": 5500,
        "aceite_oliva": 18000,
    }
    
    return precios
