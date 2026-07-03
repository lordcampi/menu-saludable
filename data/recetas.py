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
            "nombre": "Huevos pericos con arepa",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 3, "unidad": "unidades", "tipo": "unidad"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "cebolla_larga": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Picar tomate y cebolla finamente",
                "Batir los huevos",
                "Sofreir tomate y cebolla en aceite",
                "Agregar huevos batidos y revolver",
                "Servir con arepas asadas"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 20, "carbohidratos": 35, "grasas": 14, "fibra": 5
            },
            "tags": ["colombiano", "rapido"]
        },
        {
            "id": "des_03",
            "nombre": "Avena fria con frutas",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "avena": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "leche": {"cantidad": 300, "unidad": "ml", "tipo": "volumen"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "miel": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Mezclar la avena con leche fria",
                "Dejar reposar 5 minutos",
                "Cortar banano y fresas en rodajas",
                "Agregar frutas a la avena",
                "Endulzar con miel al gusto"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 14, "carbohidratos": 55, "grasas": 10, "fibra": 7
            },
            "tags": ["saludable", "rapido", "sin_coccion"]
        },
        {
            "id": "des_04",
            "nombre": "Panqueques con fruta",
            "categoria": "desayuno",
            "tiempo_preparacion": "20 min",
            "dificultad": "media",
            "ingredientes": {
                "harina": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "huevo": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "leche": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "azucar": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Mezclar harina, huevo, leche y azucar",
                "Batir hasta obtener mezcla homogenea",
                "Calentar sarten con mantequilla",
                "Verter porciones y cocinar hasta dorar",
                "Servir con banano en rodajas"
            ],
            "informacion_nutricional": {
                "calorias": 420, "proteinas": 15, "carbohidratos": 55, "grasas": 16, "fibra": 3
            },
            "tags": ["especial", "fin_de_semana"]
        },
        {
            "id": "des_05",
            "nombre": "Cereal con frutas y leche",
            "categoria": "desayuno",
            "tiempo_preparacion": "5 min",
            "dificultad": "facil",
            "ingredientes": {
                "cereal": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "leche": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Servir el cereal en un tazon",
                "Agregar leche fria",
                "Cortar frutas y agregar encima",
                "Mezclar y disfrutar"
            ],
            "informacion_nutricional": {
                "calorias": 340, "proteinas": 11, "carbohidratos": 52, "grasas": 9, "fibra": 5
            },
            "tags": ["rapido", "sin_coccion"]
        },
        {
            "id": "des_06",
            "nombre": "Tortilla de huevo con jamon y queso",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 3, "unidad": "unidades", "tipo": "unidad"},
                "jamon": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Batir los huevos con sal",
                "Picar jamon en cuadritos",
                "Calentar sarten con aceite",
                "Verter huevos, agregar jamon y queso",
                "Cocinar hasta que cuaje"
            ],
            "informacion_nutricional": {
                "calorias": 340, "proteinas": 28, "carbohidratos": 5, "grasas": 24, "fibra": 0
            },
            "tags": ["proteina", "rapido"]
        },
        {
            "id": "des_07",
            "nombre": "Arepas con queso y jamon",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "queso_fresco": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "jamon": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta dorar",
                "Rallar el queso fresco",
                "Picar jamon en tiras",
                "Abrir arepas y rellenar con queso y jamon",
                "Calentar en sarten con mantequilla hasta derretir queso"
            ],
            "informacion_nutricional": {
                "calorias": 370, "proteinas": 20, "carbohidratos": 38, "grasas": 16, "fibra": 3
            },
            "tags": ["colombiano", "rapido"]
        },
        {
            "id": "des_08",
            "nombre": "Frutas picadas con yogurt griego",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "yogurt_griego": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "miel": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "granola": {"cantidad": 20, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar fresas en mitades",
                "Pelar y cortar banano en rodajas",
                "Servir yogurt griego en tazon",
                "Agregar frutas encima",
                "Decorar con granola y miel"
            ],
            "informacion_nutricional": {
                "calorias": 310, "proteinas": 12, "carbohidratos": 48, "grasas": 8, "fibra": 5
            },
            "tags": ["saludable", "rapido", "sin_coccion"]
        },
        {
            "id": "des_09",
            "nombre": "Chocolate frio con pan",
            "categoria": "desayuno",
            "tiempo_preparacion": "5 min",
            "dificultad": "facil",
            "ingredientes": {
                "leche": {"cantidad": 400, "unidad": "ml", "tipo": "volumen"},
                "chocolate_polvo": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Licuar leche con chocolate en polvo",
                "Servir frio en vaso",
                "Tostar pan y untar con mantequilla",
                "Acompanar el chocolate con el pan"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 12, "carbohidratos": 48, "grasas": 12, "fibra": 4
            },
            "tags": ["rapido", "colombiano"]
        },
        {
            "id": "des_10",
            "nombre": "Tostada aguacate y jamon",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "jamon": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Tostar el pan integral hasta que este dorado",
                "Machacar el aguacate con limon y sal",
                "Untar el aguacate sobre las tostadas",
                "Colocar jamon encima",
                "Servir inmediatamente"
            ],
            "informacion_nutricional": {
                "calorias": 360, "proteinas": 16, "carbohidratos": 32, "grasas": 18, "fibra": 6
            },
            "tags": ["rapido", "saludable"]
        },
        {
            "id": "des_11",
            "nombre": "Tostadas de arroz con mermelada y queso fresco",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "mermelada": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 120, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Tostar ligeramente el pan integral",
                "Untar mermelada en una tostada",
                "Colocar queso fresco encima (cuajada/queso fresco es lo mismo)",
                "Repetir con la segunda tostada",
                "Servir al momento"
            ],
            "informacion_nutricional": {
                "calorias": 390, "proteinas": 14, "carbohidratos": 48, "grasas": 14, "fibra": 4
            },
            "tags": ["rapido", "dulce"]
        },
        {
            "id": "des_12",
            "nombre": "Empanadas de carne desayuno",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "empanadas_carne": {"cantidad": 6, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Comprar empanadas de carne ya hechas",
                "Pincelar muy poco aceite (opcional)",
                "Calentar en Air Fryer 8 min a 180 C hasta dorar",
                "Servir con limon al gusto"
            ],
            "informacion_nutricional": {
                "calorias": 420, "proteinas": 18, "carbohidratos": 45, "grasas": 20, "fibra": 3
            },
            "tags": ["colombiano", "tradicional"]
        },
        {
            "id": "des_13",
            "nombre": "Carimañola de carne",
            "categoria": "desayuno",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "carimañolas": {"cantidad": 4, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Comprar carimañolas de carne ya hechas",
                "Pincelar muy poco aceite (opcional)",
                "Calentar en Air Fryer 10 min a 190 C hasta dorar",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 450, "proteinas": 16, "carbohidratos": 48, "grasas": 22, "fibra": 3
            },
            "tags": ["colombiano", "tradicional"]
        },
        {
            "id": "des_14",
            "nombre": "Arepa reina pepiada",
            "categoria": "desayuno",
            "tiempo_preparacion": "25 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pechuga de pollo y desmechar finamente",
                "Asar las arepas hasta que esten doradas",
                "Machacar aguacate con limon y sal",
                "Abrir arepas y rellenar con pollo y aguacate",
                "Servir inmediatamente"
            ],
            "informacion_nutricional": {
                "calorias": 400, "proteinas": 28, "carbohidratos": 38, "grasas": 14, "fibra": 5
            },
            "tags": ["venezolano", "proteina"]
        },
        {
            "id": "des_15",
            "nombre": "Arepas con huevo sin aguacate",
            "categoria": "desayuno",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "huevo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "tomate": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta que esten doradas",
                "Freir los huevos con un poco de aceite",
                "Picar tomate y cilantro finamente",
                "Servir la arepa con huevo y la mezcla de tomate y cilantro",
                "Sazonar con sal al gusto"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 16, "carbohidratos": 40, "grasas": 10, "fibra": 4
            },
            "tags": ["colombiano", "rapido"]
        }
    ],
    "almuerzos": [
        {
            "id": "alm_01",
            "nombre": "Bistec de res con arroz y ensalada",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "bistec_res": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar bistec con sal, pimienta, ajo machacado y limon",
                "Cocinar arroz normalmente con un poco de cebolla picada",
                "Cocinar bistec a la plancha 4 min por lado",
                "Lavar y cortar lechuga y tomate",
                "Servir bistec con arroz y ensalada"
            ],
            "informacion_nutricional": {
                "calorias": 560, "proteinas": 40, "carbohidratos": 55, "grasas": 18, "fibra": 5
            },
            "tags": ["proteina", "completo"]
        },
        {
            "id": "alm_02",
            "nombre": "Pollo guisado con verduras y arroz",
            "categoria": "almuerzo",
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "muslo_pollo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar muslo de pollo en presas",
                "Picar cebolla, ajo y tomate",
                "Sofreir cebolla, ajo y tomate en aceite",
                "Agregar pollo, comino y pimienta, cocinar 20 min",
                "Agregar zanahoria en rodajas",
                "Cocinar hasta que este tierno",
                "Servir con arroz blanco y cilantro picado"
            ],
            "informacion_nutricional": {
                "calorias": 560, "proteinas": 38, "carbohidratos": 58, "grasas": 18, "fibra": 6
            },
            "tags": ["saludable", "balanceado", "proteina"]
        },
        {
            "id": "alm_03",
            "nombre": "Pasta con pollo y champiñones",
            "categoria": "almuerzo",
            "tiempo_preparacion": "30 min",
            "dificultad": "facil",
            "ingredientes": {
                "pasta": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "pechuga_pollo": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "champiñones": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "crema_leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "queso_parmesano": {"cantidad": 30, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pasta en agua con sal hasta al dente",
                "Cortar pollo en tiras y saltear",
                "Saltear champiñones con ajo",
                "Mezclar pollo, champiñones y crema de leche",
                "Servir sobre la pasta con queso parmesano"
            ],
            "informacion_nutricional": {
                "calorias": 600, "proteinas": 38, "carbohidratos": 62, "grasas": 22, "fibra": 4
            },
            "tags": ["italiano", "cremoso", "proteina"]
        },
        {
            "id": "alm_04",
            "nombre": "Albondigas en salsa con pure de papa",
            "categoria": "almuerzo",
            "tiempo_preparacion": "45 min",
            "dificultad": "media",
            "ingredientes": {
                "carne_molida": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "huevo": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Mezclar carne molida con huevo, ajo picado, comino, pimienta y sal",
                "Formar albondigas y dorar en aceite",
                "Licuar tomate y cebolla para salsa",
                "Cocinar albondigas en la salsa 20 min",
                "Cocinar papas, hacer pure con leche, mantequilla y sal",
                "Servir albondigas sobre pure"
            ],
            "informacion_nutricional": {
                "calorias": 600, "proteinas": 32, "carbohidratos": 48, "grasas": 28, "fibra": 6
            },
            "tags": ["familiar", "reconfortante"]
        },
        {
            "id": "alm_05",
            "nombre": "Pescado a la plancha con arroz y platano",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "media",
            "ingredientes": {
                "filete_pescado": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "platano_maduro": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar pescado con limon, ajo machacado y sal",
                "Cocinar arroz normalmente",
                "Pelar y cortar platano en tajadas",
                "Freir tajadas de platano",
                "Cocinar pescado a la plancha 3-4 min por lado",
                "Servir con arroz y tajadas"
            ],
            "informacion_nutricional": {
                "calorias": 580, "proteinas": 35, "carbohidratos": 65, "grasas": 18, "fibra": 4
            },
            "tags": ["colombiano", "omega3"]
        },
        {
            "id": "alm_06",
            "nombre": "Chicharron con yuca frita y arroz",
            "categoria": "almuerzo",
            "tiempo_preparacion": "50 min",
            "dificultad": "media",
            "ingredientes": {
                "chicharron": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "yuca": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar arroz normalmente",
                "Pelar y cortar yuca en bastones",
                "Freir yuca en aceite caliente hasta dorar",
                "Freir chicharron hasta que este crocante",
                "Servir con limon"
            ],
            "informacion_nutricional": {
                "calorias": 650, "proteinas": 25, "carbohidratos": 55, "grasas": 38, "fibra": 3
            },
            "tags": ["colombiano", "ocasional"]
        },
        {
            "id": "alm_07",
            "nombre": "Sancocho de espinazo",
            "categoria": "almuerzo",
            "tiempo_preparacion": "1 hora 30 min",
            "dificultad": "media",
            "ingredientes": {
                "espinazo_cerdo": {"cantidad": 500, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "yuca": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "platano_verde": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "mazorca": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "cebolla_larga": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 5, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar el espinazo y cortar en trozos",
                "Hervir en agua con sal, ajo, comino y cebolla por 50 min",
                "Pelar y cortar papa, yuca y platano",
                "Agregar verduras y mazorca al caldo",
                "Cocinar hasta que la carne se desprenda del hueso",
                "Servir caliente con cilantro picado"
            ],
            "informacion_nutricional": {
                "calorias": 560, "proteinas": 32, "carbohidratos": 52, "grasas": 22, "fibra": 8
            },
            "tags": ["colombiano", "tradicional", "familiar"]
        },
        {
            "id": "alm_08",
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
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar el arroz normalmente",
                "Freir platano maduro en tajadas",
                "Cocinar frijoles con alinos, comino y sal",
                "Cocinar carne mechada con cebolla, aji y ajo",
                "Servir todo por separado en el plato"
            ],
            "informacion_nutricional": {
                "calorias": 580, "proteinas": 30, "carbohidratos": 68, "grasas": 20, "fibra": 10
            },
            "tags": ["venezolano", "tradicional", "completo"]
        },
        {
            "id": "alm_09",
            "nombre": "Hamburguesas caseras",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "carne_molida": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "pan_hamburguesa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "papa_francesa": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Mezclar carne molida con ajo picado, pimienta y sal, formar hamburguesas",
                "Cocinar hamburguesas en sarten o Air Fryer 12 min a 190 C",
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Armar hamburguesa con tomate, lechuga, cebolla y queso",
                "Servir con papas fritas"
            ],
            "informacion_nutricional": {
                "calorias": 680, "proteinas": 38, "carbohidratos": 55, "grasas": 32, "fibra": 5
            },
            "tags": ["rapido", "familiar", "ocasional"]
        },
        {
            "id": "alm_10",
            "nombre": "Higado encebollado",
            "categoria": "almuerzo",
            "tiempo_preparacion": "30 min",
            "dificultad": "facil",
            "ingredientes": {
                "higado_res": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar higado en laminas finas, sazonar con ajo, pimienta y sal",
                "Cocinar arroz normalmente",
                "Saltear cebolla en aceite hasta que este transparente",
                "Agregar higado y cocinar 5 min por lado",
                "Servir con arroz y limon"
            ],
            "informacion_nutricional": {
                "calorias": 520, "proteinas": 42, "carbohidratos": 52, "grasas": 14, "fibra": 3
            },
            "tags": ["colombiano", "proteina", "hierro"]
        },
        {
            "id": "alm_11",
            "nombre": "Alitas BBQ",
            "categoria": "almuerzo",
            "tiempo_preparacion": "45 min",
            "dificultad": "facil",
            "ingredientes": {
                "alitas_pollo": {"cantidad": 800, "unidad": "gr", "tipo": "peso"},
                "salsa_bbq": {"cantidad": 80, "unidad": "ml", "tipo": "volumen"},
                "papa_francesa": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar alitas con sal",
                "Cocinar alitas en Air Fryer 25 min a 190 C, volteando a mitad",
                "Cubrir con salsa BBQ y cocinar 5 min mas en Air Fryer",
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Servir alitas con papas"
            ],
            "informacion_nutricional": {
                "calorias": 720, "proteinas": 48, "carbohidratos": 42, "grasas": 38, "fibra": 4
            },
            "tags": ["familiar", "ocasional"]
        },
        {
            "id": "alm_12",
            "nombre": "Frijol rojo con pezuña",
            "categoria": "almuerzo",
            "tiempo_preparacion": "2 horas",
            "dificultad": "media",
            "ingredientes": {
                "frijol_rojo": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "pezuña_res": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "platano_verde": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Remojar frijol rojo y pezuña la noche anterior",
                "Cocinar pezuña con frijol rojo en olla a presion 1 hora",
                "Sofreir cebolla, tomate y ajo",
                "Agregar sofrito, comino y sal al guiso y cocinar 20 min mas",
                "Servir con platano verde cocido o frito"
            ],
            "informacion_nutricional": {
                "calorias": 580, "proteinas": 38, "carbohidratos": 62, "grasas": 16, "fibra": 12
            },
            "tags": ["colombiano", "tradicional", "reconfortante"]
        },
        {
            "id": "alm_13",
            "nombre": "Chuleta de cerdo con papas a la francesa",
            "categoria": "almuerzo",
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "chuleta_cerdo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "papa_francesa": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar chuletas con ajo machacado, pimienta y sal",
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Cocinar chuletas en sarten o Air Fryer 12 min a 190 C",
                "Servir chuletas con papas a la francesa"
            ],
            "informacion_nutricional": {
                "calorias": 680, "proteinas": 36, "carbohidratos": 48, "grasas": 38, "fibra": 5
            },
            "tags": ["proteina", "familiar"]
        },
        {
            "id": "alm_14",
            "nombre": "Salchipapa con pollo",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "salchicha": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "tocineta": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "papa_francesa": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Cocinar pechuga en Air Fryer o plancha y cortar en tiras",
                "Calentar salchichas y tocineta en Air Fryer 8 min a 190 C",
                "Mezclar todo con sal y servir con queso fresco rallado"
            ],
            "informacion_nutricional": {
                "calorias": 750, "proteinas": 42, "carbohidratos": 52, "grasas": 42, "fibra": 5
            },
            "tags": ["colombiano", "rapido", "ocasional"]
        },
        {
            "id": "alm_15",
            "nombre": "Arroz con pollo",
            "categoria": "almuerzo",
            "tiempo_preparacion": "45 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "arvejas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar pechuga de pollo en cubos",
                "Sofreir cebolla, ajo y tomate en aceite",
                "Agregar pollo y dorar por todos lados",
                "Incorporar arroz, verduras y sal",
                "Agregar agua y cocinar hasta que el arroz este listo",
                "Dejar reposar 5 min y servir"
            ],
            "informacion_nutricional": {
                "calorias": 590, "proteinas": 36, "carbohidratos": 68, "grasas": 16, "fibra": 6
            },
            "tags": ["colombiano", "tradicional", "completo"]
        }
    ],
    "cenas": [
        {
            "id": "cen_01",
            "nombre": "Ensalada Cesar con pollo",
            "categoria": "cena",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "lechuga": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "pan_integral": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "queso_parmesano": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar lechuga",
                "Cocinar pechuga a la plancha, sazonar con sal y cortar en tiras",
                "Hacer crutones con pan integral tostado",
                "Preparar aderezo con limon y aceite de oliva",
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
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "lentejas": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar lentejas y dejar en remojo",
                "Picar verduras y sofreir cebolla y ajo en aceite",
                "Cocinar lentejas con verduras",
                "Agregar comino, sal y condimentos",
                "Cocinar hasta que lentejas esten tiernas"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 22, "carbohidratos": 48, "grasas": 4, "fibra": 10
            },
            "tags": ["ligero", "vegetariano", "reconfortante"]
        },
        {
            "id": "cen_03",
            "nombre": "Tortilla de huevo con champiñones",
            "categoria": "cena",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 4, "unidad": "unidades", "tipo": "unidad"},
                "champiñones": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Saltear champiñones y cebolla picados",
                "Batir huevos con sal",
                "Mezclar todo y verter en sarten caliente",
                "Cocinar hasta que cuaje por ambos lados",
                "Servir caliente"
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
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "tortilla_harina": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pechuga a la plancha y cortar en tiras",
                "Machacar aguacate con limon y sal",
                "Picar tomate y lechuga",
                "Calentar tortillas",
                "Armar wrap con pollo, aguacate, tomate y lechuga"
            ],
            "informacion_nutricional": {
                "calorias": 410, "proteinas": 30, "carbohidratos": 32, "grasas": 18, "fibra": 7
            },
            "tags": ["ligero", "practico", "balanceado"]
        },
        {
            "id": "cen_05",
            "nombre": "Crema de verduras",
            "categoria": "cena",
            "tiempo_preparacion": "30 min",
            "dificultad": "facil",
            "ingredientes": {
                "zapallo": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "crema_leche": {"cantidad": 80, "unidad": "ml", "tipo": "volumen"},
                "mantequilla": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar todas las verduras",
                "Cocinar en agua con ajo y sal hasta que esten tiernas",
                "Licuar con crema de leche y mantequilla",
                "Volver a calentar y sazonar",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 290, "proteinas": 8, "carbohidratos": 38, "grasas": 12, "fibra": 5
            },
            "tags": ["ligero", "reconfortante", "vegetariano"]
        },
        {
            "id": "cen_06",
            "nombre": "Sandwich de jamon y queso",
            "categoria": "cena",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "jamon": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Tostar ligeramente el pan",
                "Untar mantequilla",
                "Colocar jamon, queso, tomate y lechuga",
                "Cerrar sandwich y cortar en diagonal",
                "Servir inmediatamente"
            ],
            "informacion_nutricional": {
                "calorias": 400, "proteinas": 25, "carbohidratos": 30, "grasas": 20, "fibra": 4
            },
            "tags": ["ligero", "rapido", "practico"]
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
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas",
                "Mezclar atun con cebolla picada, limon y sal",
                "Cortar aguacate y tomate",
                "Abrir arepas y rellenar con atun",
                "Servir con aguacate y tomate al lado"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 28, "carbohidratos": 35, "grasas": 14, "fibra": 5
            },
            "tags": ["ligero", "colombiano", "rapido"]
        },
        {
            "id": "cen_08",
            "nombre": "Pasta corta con verduras",
            "categoria": "cena",
            "tiempo_preparacion": "25 min",
            "dificultad": "facil",
            "ingredientes": {
                "pasta": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "aceite_oliva": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "queso_parmesano": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pasta en agua con sal",
                "Picar tomate, zanahoria y cebolla",
                "Sofreir verduras con ajo y sal en aceite de oliva",
                "Mezclar pasta con verduras",
                "Servir con queso parmesano rallado"
            ],
            "informacion_nutricional": {
                "calorias": 400, "proteinas": 14, "carbohidratos": 55, "grasas": 14, "fibra": 5
            },
            "tags": ["ligero", "vegetariano", "rapido"]
        },
        {
            "id": "cen_09",
            "nombre": "Sopa de pollo con verduras",
            "categoria": "cena",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar pechuga en cubos pequenos",
                "Picar zanahoria, papa y cebolla",
                "Hervir todo en agua con sal por 25 min",
                "Agregar cilantro picado al final",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 300, "proteinas": 28, "carbohidratos": 25, "grasas": 8, "fibra": 4
            },
            "tags": ["ligero", "reconfortante", "proteina"]
        },
        {
            "id": "cen_10",
            "nombre": "Ensalada de pollo y aguacate",
            "categoria": "cena",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "aguacate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite_oliva": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pechuga a la plancha o en Air Fryer 12 min a 190 C",
                "Lavar y cortar lechuga y tomate",
                "Cortar aguacate en tajadas",
                "Mezclar todo con limon, aceite de oliva y sal",
                "Servir fresco"
            ],
            "informacion_nutricional": {
                "calorias": 360, "proteinas": 32, "carbohidratos": 14, "grasas": 20, "fibra": 6
            },
            "tags": ["ligero", "proteina", "rapido"]
        },
        {
            "id": "cen_11",
            "nombre": "Arepa con chorizo",
            "categoria": "cena",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "chorizo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Calentar arepas en Air Fryer o sarten hasta dorar",
                "Cocinar chorizos en Air Fryer 10 min a 190 C o a la plancha",
                "Picar cebolla finamente",
                "Abrir arepas y rellenar con chorizo y cebolla",
                "Servir con limon al gusto"
            ],
            "informacion_nutricional": {
                "calorias": 420, "proteinas": 18, "carbohidratos": 38, "grasas": 22, "fibra": 3
            },
            "tags": ["colombiano", "rapido"]
        },
        {
            "id": "cen_12",
            "nombre": "Crema de pescado",
            "categoria": "cena",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "filete_pescado": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "crema_leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pescado en agua con cebolla, ajo y sal",
                "Agregar papas picadas y cocinar hasta tiernas",
                "Desmenuzar el pescado en el caldo",
                "Licuar con crema de leche",
                "Servir caliente con cilantro picado"
            ],
            "informacion_nutricional": {
                "calorias": 340, "proteinas": 28, "carbohidratos": 28, "grasas": 14, "fibra": 3
            },
            "tags": ["ligero", "reconfortante", "omega3"]
        },
        {
            "id": "cen_13",
            "nombre": "Guisado de menudencias de pollo",
            "categoria": "cena",
            "tiempo_preparacion": "40 min",
            "dificultad": "media",
            "ingredientes": {
                "menudencias_pollo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y picar menudencias de pollo",
                "Sofreir cebolla, ajo y tomate en aceite",
                "Agregar menudencias, comino y sal, cocinar 15 min",
                "Incorporar papa y zanahoria picadas",
                "Cocinar hasta que verduras esten tiernas y servir"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 30, "carbohidratos": 28, "grasas": 10, "fibra": 4
            },
            "tags": ["colombiano", "economico", "proteina"]
        },
        {
            "id": "cen_14",
            "nombre": "Sopa de arroz con pollo",
            "categoria": "cena",
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "muslo_pollo": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar muslo de pollo en presas",
                "Hervir pollo en agua con sal por 20 min",
                "Agregar arroz, papa y zanahoria picadas",
                "Cocinar hasta que arroz y verduras esten listos",
                "Servir caliente con cilantro picado"
            ],
            "informacion_nutricional": {
                "calorias": 360, "proteinas": 28, "carbohidratos": 38, "grasas": 10, "fibra": 4
            },
            "tags": ["ligero", "reconfortante", "colombiano"]
        },
        {
            "id": "cen_15",
            "nombre": "Patacon con carne mechada",
            "categoria": "cena",
            "tiempo_preparacion": "35 min",
            "dificultad": "media",
            "ingredientes": {
                "platano_verde": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "carne_mechar": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar platano verde en rodajas gruesas",
                "Freir platano, aplastar y freir de nuevo",
                "Calentar carne mechada con cebolla, ajo, comino y sal en un poco de aceite",
                "Colocar carne sobre cada patacon",
                "Agregar queso fresco y servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 450, "proteinas": 22, "carbohidratos": 42, "grasas": 22, "fibra": 4
            },
            "tags": ["venezolano", "colombiano", "especial"]
        }
    ]
}


def get_receta_por_id(receta_id):
    for categoria in RECETAS.values():
        for r in categoria:
            if r["id"] == receta_id:
                return r
    return None


def get_todas_recetas():
    return [r for cat in RECETAS.values() for r in cat]
