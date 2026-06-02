"""
Base de datos de recetas para el planificador de comidas
"""

RECETAS = {
    "desayunos": [
        {
            "id": "des_01",
            "nombre": "Arepas con huevo y aguacate",
            "categoria": "desayuno",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "huevo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "aguacate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta que esten doradas",
                "Freir los huevos con un poco de aceite",
                "Cortar el aguacate en tajadas",
                "Picar tomate y cilantro finamente",
                "Servir la arepa con huevo, aguacate y la mezcla de tomate y cilantro"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 18, "carbohidratos": 42, "grasas": 16, "fibra": 6
            },
            "tags": ["colombiano", "tradicional"]
        },
        {
            "id": "des_02",
            "nombre": "Huevos pericos con pan integral",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 3, "unidad": "unidades", "tipo": "unidad"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "cebolla_larga": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "pan_integral": {"cantidad": 4, "unidad": "rebanadas", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Picar tomate y cebolla finamente",
                "Batir los huevos",
                "Sofreir tomate y cebolla en aceite",
                "Agregar huevos batidos y revolver",
                "Servir con pan integral tostado"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 20, "carbohidratos": 35, "grasas": 14, "fibra": 5
            },
            "tags": ["colombiano", "rapido"]
        },
        {
            "id": "des_03",
            "nombre": "Avena con frutas y nueces",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "avena": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "leche": {"cantidad": 400, "unidad": "ml", "tipo": "volumen"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "nueces": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "miel": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Cocinar la avena con leche a fuego medio por 10 min",
                "Revolver constantemente hasta espesar",
                "Cortar banano y fresas en rodajas",
                "Servir la avena y decorar con frutas y nueces",
                "Agregar miel al gusto"
            ],
            "informacion_nutricional": {
                "calorias": 400, "proteinas": 15, "carbohidratos": 58, "grasas": 12, "fibra": 7
            },
            "tags": ["saludable", "energetico"]
        },
        {
            "id": "des_04",
            "nombre": "Tostadas francesas con fruta",
            "categoria": "desayuno",
            "tiempo_preparacion": "20 min",
            "dificultad": "media",
            "ingredientes": {
                "pan_integral": {"cantidad": 4, "unidad": "rebanadas", "tipo": "unidad"},
                "huevo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "canela": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "fresas": {"cantidad": 150, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Batir huevos con leche y canela",
                "Remojar las rebanadas de pan en la mezcla",
                "Derretir mantequilla en sarten",
                "Dorar las tostadas por ambos lados",
                "Servir con fresas frescas"
            ],
            "informacion_nutricional": {
                "calorias": 370, "proteinas": 16, "carbohidratos": 48, "grasas": 14, "fibra": 5
            },
            "tags": ["especial"]
        },
        {
            "id": "des_05",
            "nombre": "Batido verde energetico",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "espinaca": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "yogurt": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "miel": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "semillas_chia": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "hielo": {"cantidad": 100, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar bien las espinacas",
                "Pelar y cortar los bananos",
                "Licuar todos los ingredientes",
                "Servir inmediatamente",
                "Decorar con semillas de chia"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 12, "carbohidratos": 52, "grasas": 8, "fibra": 8
            },
            "tags": ["saludable", "detox"]
        },
        {
            "id": "des_06",
            "nombre": "Arepas con queso y tomate",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "queso_fresco": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "oregano": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Asar las arepas hasta dorar",
                "Cortar tomate en rodajas",
                "Rallar el queso fresco",
                "Colocar queso y tomate sobre la arepa",
                "Espolvorear oregano y servir"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 14, "carbohidratos": 40, "grasas": 15, "fibra": 4
            },
            "tags": ["colombiano", "vegetariano"]
        },
        {
            "id": "des_07",
            "nombre": "Huevos revueltos con vegetales",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 3, "unidad": "unidades", "tipo": "unidad"},
                "pimenton": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "champiñones": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Picar pimenton, cebolla y champiñones",
                "Saltear vegetales en aceite",
                "Batir los huevos con sal",
                "Agregar huevos a los vegetales",
                "Revolver hasta cocinar completamente"
            ],
            "informacion_nutricional": {
                "calorias": 310, "proteinas": 22, "carbohidratos": 12, "grasas": 18, "fibra": 3
            },
            "tags": ["proteina", "rapido"]
        }
    ],
    "almuerzos": [
        {
            "id": "alm_01",
            "nombre": "Sancocho colombiano de gallina",
            "categoria": "almuerzo",
            "tiempo_preparacion": "1 hora 30 min",
            "dificultad": "media",
            "ingredientes": {
                "gallina": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "yuca": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "platano_verde": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "mazorca": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "cebolla_larga": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 5, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar la gallina en presas",
                "Hervir en agua con sal y cebolla por 45 min",
                "Pelar y cortar papa, yuca y platano",
                "Agregar verduras y mazorca al caldo",
                "Cocinar hasta que todo este tierno",
                "Servir caliente con cilantro picado"
            ],
            "informacion_nutricional": {
                "calorias": 550, "proteinas": 35, "carbohidratos": 52, "grasas": 18, "fibra": 8
            },
            "tags": ["colombiano", "tradicional", "familiar"]
        },
        {
            "id": "alm_02",
            "nombre": "Pabellon criollo venezolano",
            "categoria": "almuerzo",
            "tiempo_preparacion": "1 hora",
            "dificultad": "media",
            "ingredientes": {
                "carne_mechar": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "frijol_negro": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "platano_maduro": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "aji": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar el arroz normalmente",
                "Freir platano maduro en tajadas",
                "Cocinar frijoles con alinos",
                "Cocinar carne mechada con cebolla y aji",
                "Servir todo por separado en el plato"
            ],
            "informacion_nutricional": {
                "calorias": 580, "proteinas": 30, "carbohidratos": 68, "grasas": 20, "fibra": 10
            },
            "tags": ["venezolano", "tradicional", "completo"]
        },
        {
            "id": "alm_03",
            "nombre": "Pollo guisado con verduras",
            "categoria": "almuerzo",
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "brocoli": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar pechuga en cubos",
                "Picar cebolla y tomate",
                "Sofreir cebolla y tomate",
                "Agregar pollo y cocinar 15 min",
                "Agregar zanahoria y brocoli",
                "Cocinar hasta que este tierno"
            ],
            "informacion_nutricional": {
                "calorias": 480, "proteinas": 40, "carbohidratos": 22, "grasas": 24, "fibra": 6
            },
            "tags": ["saludable", "balanceado", "proteina"]
        },
        {
            "id": "alm_04",
            "nombre": "Pescado al horno con vegetales",
            "categoria": "almuerzo",
            "tiempo_preparacion": "40 min",
            "dificultad": "media",
            "ingredientes": {
                "filete_pescado": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar el pescado con limon y ajo",
                "Cortar papas y zanahorias en rodajas",
                "Colocar en bandeja para horno",
                "Rociar con aceite de oliva",
                "Hornear a 180C por 25-30 minutos"
            ],
            "informacion_nutricional": {
                "calorias": 450, "proteinas": 38, "carbohidratos": 35, "grasas": 16, "fibra": 5
            },
            "tags": ["saludable", "omega3", "horneado"]
        },
        {
            "id": "alm_05",
            "nombre": "Lentejas guisadas con arroz",
            "categoria": "almuerzo",
            "tiempo_preparacion": "1 hora",
            "dificultad": "media",
            "ingredientes": {
                "lentejas": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Lavar lentejas y remojar por 1 hora",
                "Picar cebolla, tomate y zanahoria",
                "Sofreir vegetales, agregar lentejas",
                "Cubrir con agua y agregar comino",
                "Cocinar hasta que esten tiernas",
                "Cocinar arroz aparte y servir juntos"
            ],
            "informacion_nutricional": {
                "calorias": 500, "proteinas": 28, "carbohidratos": 72, "grasas": 10, "fibra": 12
            },
            "tags": ["vegetariano", "fibra", "economico"]
        },
        {
            "id": "alm_06",
            "nombre": "Bistec a la plancha con ensalada",
            "categoria": "almuerzo",
            "tiempo_preparacion": "30 min",
            "dificultad": "facil",
            "ingredientes": {
                "bistec_res": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar bistec con sal y limon",
                "Cocinar a la plancha 4 min por lado",
                "Lavar y cortar lechuga",
                "Cortar tomate y aguacate",
                "Preparar ensalada y aderezar con aceite"
            ],
            "informacion_nutricional": {
                "calorias": 520, "proteinas": 42, "carbohidratos": 15, "grasas": 32, "fibra": 7
            },
            "tags": ["proteina", "bajo_en_carbohidratos", "rapido"]
        },
        {
            "id": "alm_07",
            "nombre": "Arroz con pollo y verduras",
            "categoria": "almuerzo",
            "tiempo_preparacion": "45 min",
            "dificultad": "media",
            "ingredientes": {
                "arroz": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "pechuga_pollo": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "arvejas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "pimenton": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 70, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 25, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Cocinar pollo y desmenuzar",
                "Picar todas las verduras",
                "Sofreir verduras en aceite",
                "Agregar arroz y agua",
                "Incorporar pollo desmenuzado",
                "Cocinar hasta que el arroz este listo"
            ],
            "informacion_nutricional": {
                "calorias": 540, "proteinas": 36, "carbohidratos": 62, "grasas": 16, "fibra": 5
            },
            "tags": ["completo", "familiar", "balanceado"]
        }
    ],
    "cenas": [
        {
            "id": "cen_01",
            "nombre": "Ensalada Cesar con pollo",
            "categoria": "cena",
            "tiempo_preparacion": "25 min",
            "dificultad": "facil",
            "ingredientes": {
                "lechuga": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "queso_parmesano": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Lavar y cortar lechuga",
                "Cocinar pechuga a la plancha",
                "Hacer crutones con pan integral",
                "Preparar aderezo con limon y aceite",
                "Mezclar todo y agregar queso parmesano"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 32, "carbohidratos": 20, "grasas": 18, "fibra": 4
            },
            "tags": ["ligero", "proteina", "rapido"]
        },
        {
            "id": "cen_02",
            "nombre": "Sopa de lentejas",
            "categoria": "cena",
            "tiempo_preparacion": "45 min",
            "dificultad": "facil",
            "ingredientes": {
                "lentejas": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar lentejas y dejar en remojo",
                "Picar verduras",
                "Cocinar lentejas con verduras",
                "Agregar comino y condimentos",
                "Cocinar hasta que lentejas esten tiernas"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 22, "carbohidratos": 48, "grasas": 4, "fibra": 10
            },
            "tags": ["ligero", "vegetariano", "reconfortante"]
        },
        {
            "id": "cen_03",
            "nombre": "Tortilla de verduras",
            "categoria": "cena",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 4, "unidad": "unidades", "tipo": "unidad"},
                "espinaca": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "champiñones": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Saltear champiñones y cebolla",
                "Agregar espinacas",
                "Batir huevos con sal",
                "Mezclar todo y cocinar en sarten",
                "Cocinar hasta que cuaje por ambos lados"
            ],
            "informacion_nutricional": {
                "calorias": 300, "proteinas": 24, "carbohidratos": 8, "grasas": 18, "fibra": 3
            },
            "tags": ["ligero", "bajo_en_carbohidratos", "rapido"]
        },
        {
            "id": "cen_04",
            "nombre": "Wrap de pollo con aguacate",
            "categoria": "cena",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "tortilla_harina": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "yogurt": {"cantidad": 50, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Cocinar pechuga a la plancha y cortar en tiras",
                "Machacar aguacate",
                "Picar tomate y lechuga",
                "Armar wrap con todos los ingredientes",
                "Agregar yogurt como aderezo"
            ],
            "informacion_nutricional": {
                "calorias": 420, "proteinas": 30, "carbohidratos": 32, "grasas": 20, "fibra": 7
            },
            "tags": ["ligero", "practico", "balanceado"]
        },
        {
            "id": "cen_05",
            "nombre": "Crema de verduras",
            "categoria": "cena",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "zapallo": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "mantequilla": {"cantidad": 15, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar todas las verduras",
                "Cocinar en agua hasta que esten tiernas",
                "Licuar con leche y mantequilla",
                "Volver a calentar y sazonar",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 290, "proteinas": 8, "carbohidratos": 42, "grasas": 10, "fibra": 5
            },
            "tags": ["ligero", "reconfortante", "vegetariano"]
        },
        {
            "id": "cen_06",
            "nombre": "Pescado a la plancha con ensalada",
            "categoria": "cena",
            "tiempo_preparacion": "25 min",
            "dificultad": "facil",
            "ingredientes": {
                "filete_pescado": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "pepino": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Sazonar pescado con limon y sal",
                "Cocinar en plancha 3-4 min por lado",
                "Cortar verduras para ensalada",
                "Aderezar con aceite de oliva",
                "Servir pescado sobre la ensalada"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 34, "carbohidratos": 10, "grasas": 18, "fibra": 4
            },
            "tags": ["ligero", "omega3", "saludable"]
        },
        {
            "id": "cen_07",
            "nombre": "Arepas rellenas con atun",
            "categoria": "cena",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "atun": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Asar las arepas",
                "Mezclar atun con cebolla y limon",
                "Cortar aguacate y tomate",
                "Abrir arepas y rellenar con atun",
                "Servir con aguacate y tomate al lado"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 28, "carbohidratos": 35, "grasas": 14, "fibra": 5
            },
            "tags": ["ligero", "colombiano", "rapido"]
        }
    ]
}
