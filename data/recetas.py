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
                "cebolla_larga": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 0.5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta que esten doradas",
                "Sofreir tomate y cebolla larga en la mitad del aceite; retirar del fuego y agregar cilantro",
                "Freir los huevos con el aceite restante y sazonar con sal y pimienta",
                "Cortar el aguacate en tajadas",
                "Servir la arepa con huevo, aguacate y el hogao ligero"
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
                "Batir los huevos con sal",
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
                "miel": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "canela": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Mezclar la avena con leche fria y canela",
                "Refrigerar al menos 30 minutos o durante toda la noche",
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
                "canela": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "sal": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Separar el huevo y batir la clara a punto de nieve",
                "Mezclar harina, canela, azucar y sal con la yema y la leche",
                "Incorporar la clara con movimientos envolventes",
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
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Batir los huevos con sal y pimienta",
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
            "nombre": "Huevos revueltos con pan integral",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 3, "unidad": "unidades", "tipo": "unidad"},
                "pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 0.5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Batir los huevos con sal y pimienta",
                "Calentar el aceite en un sarten y cocinar los huevos revueltos",
                "Picar el tomate y mezclarlo con los huevos al final",
                "Tostar el pan integral y untar con mantequilla",
                "Servir los huevos con el pan tostado"
            ],
            "informacion_nutricional": {
                "calorias": 360, "proteinas": 22, "carbohidratos": 24, "grasas": 20, "fibra": 3
            },
            "tags": ["rapido", "saludable"]
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
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "canela": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Disolver el chocolate y la canela en una pequena parte de la leche tibia",
                "Agregar el resto de la leche fria y licuar",
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
                "pimienta": {"cantidad": 0.5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Tostar el pan integral hasta que este dorado",
                "Machacar el aguacate con limon, sal y pimienta",
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
            "nombre": "Tostadas integrales con mermelada y queso fresco",
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
                "Pincelar las empanadas con muy poco aceite",
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
                "Pincelar las carimañolas con muy poco aceite",
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
            "nombre": "Frutas con yogur griego",
            "categoria": "desayuno",
            "tiempo_preparacion": "10 min",
            "dificultad": "facil",
            "ingredientes": {
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "yogurt_griego": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "granola": {"cantidad": 25, "unidad": "gr", "tipo": "peso"},
                "miel": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Lavar las fresas y cortarlas en mitades",
                "Pelar el banano y cortarlo en rodajas",
                "Servir el yogur griego en un tazon",
                "Agregar las frutas y la granola",
                "Terminar con la miel y servir frio"
            ],
            "informacion_nutricional": {
                "calorias": 315, "proteinas": 13, "carbohidratos": 49, "grasas": 8, "fibra": 5
            },
            "tags": ["saludable", "rapido", "sin_coccion"]
        },
        {
            "id": "des_15",
            "nombre": "Arepa con huevo",
            "categoria": "desayuno",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "huevo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "tomate": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cebolla_larga": {"cantidad": 15, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 0.5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta que esten doradas",
                "Sofreir tomate y cebolla larga en la mitad del aceite",
                "Retirar el hogao del fuego y agregar cilantro",
                "Freir los huevos con el aceite restante y sazonar con sal y pimienta",
                "Servir la arepa con huevo y hogao"
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
                "comino": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar el bistec 15 minutos con sal, pimienta, comino, ajo y la mitad del limon",
                "Cocinar arroz normalmente con un poco de cebolla picada",
                "Cocinar bistec a la plancha con parte del aceite, 4 min por lado",
                "Lavar y cortar lechuga y tomate; aderezar con el aceite y limon restantes",
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
                "pimenton": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "laurel": {"cantidad": 0.2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar muslo de pollo en presas",
                "Picar cebolla, ajo, tomate y pimenton",
                "Sofreir cebolla, ajo, tomate y pimenton en aceite",
                "Agregar pollo, comino, pimienta y laurel; cocinar 20 min",
                "Agregar zanahoria en rodajas",
                "Cocinar hasta que este tierno",
                "Retirar el laurel y servir con arroz blanco y cilantro picado"
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
                "queso_parmesano": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "oregano": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pasta en agua con sal hasta al dente",
                "Cortar pollo en tiras, sazonar con pimienta y sal, y saltear",
                "Saltear champiñones con ajo",
                "Mezclar pollo, champiñones, crema de leche y oregano",
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
                "pimenton": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
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
                "Sofreir cebolla, pimenton y ajo; agregar tomate y cocinar hasta formar una salsa",
                "Cocinar albondigas en la salsa 20 min",
                "Cocinar papas, hacer pure con leche, mantequilla y sal",
                "Terminar las albondigas con cilantro y servir sobre el pure"
            ],
            "informacion_nutricional": {
                "calorias": 600, "proteinas": 32, "carbohidratos": 48, "grasas": 28, "fibra": 6
            },
            "tags": ["familiar", "reconfortante"]
        },
        {
            "id": "alm_05",
            "nombre": "Pescado a la plancha con ensalada y platano",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "media",
            "ingredientes": {
                "filete_pescado": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "platano_maduro": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "lechuga": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar el pescado con la mitad del limon, ajo, pimienta y sal",
                "Lavar y cortar la lechuga y el tomate",
                "Aderezar la ensalada con la otra mitad del limon y un poco de aceite",
                "Pelar y cortar platano en tajadas",
                "Freir las tajadas de platano en parte del aceite",
                "Cocinar pescado a la plancha 3-4 min por lado",
                "Servir el pescado con la ensalada y las tajadas"
            ],
            "informacion_nutricional": {
                "calorias": 490, "proteinas": 36, "carbohidratos": 45, "grasas": 18, "fibra": 7
            },
            "tags": ["colombiano", "omega3"]
        },
        {
            "id": "alm_06",
            "nombre": "Chicharron con yuca frita y ensalada",
            "categoria": "almuerzo",
            "tiempo_preparacion": "50 min",
            "dificultad": "media",
            "ingredientes": {
                "chicharron": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "yuca": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "paprika": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar solo la parte carnosa del chicharron con ajo, paprika y pimienta; mantener la piel seca",
                "Pelar y cortar yuca en bastones",
                "Freir yuca en aceite caliente hasta dorar",
                "Cocinar el chicharron en su propia grasa hasta que este crocante y terminar con sal",
                "Lavar y cortar la lechuga, el tomate y la cebolla",
                "Aderezar la ensalada con limon y servir con el chicharron y la yuca"
            ],
            "informacion_nutricional": {
                "calorias": 610, "proteinas": 25, "carbohidratos": 45, "grasas": 38, "fibra": 6
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
                "comino": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
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
                "pimenton": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "laurel": {"cantidad": 0.4, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar el arroz normalmente",
                "Freir platano maduro en tajadas",
                "Preparar un sofrito con cebolla, aji, pimenton, tomate y ajo; dividirlo en dos",
                "Cocinar frijoles con una parte del sofrito, comino, una hoja de laurel y sal",
                "Cocinar carne mechada con el resto del sofrito y otra hoja de laurel",
                "Retirar el laurel de ambas preparaciones",
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
                "mostaza": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Mezclar carne molida con ajo picado, pimienta y sal, formar hamburguesas",
                "Pincelar las hamburguesas con aceite y cocinar en sarten o Air Fryer 12 min a 190 C",
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Armar hamburguesa con tomate, lechuga, cebolla y queso",
                "Servir con papas fritas y mostaza"
            ],
            "informacion_nutricional": {
                "calorias": 680, "proteinas": 38, "carbohidratos": 55, "grasas": 32, "fibra": 5
            },
            "tags": ["rapido", "familiar", "ocasional"]
        },
        {
            "id": "alm_10",
            "nombre": "Costilla de cerdo con arroz y ensalada",
            "categoria": "almuerzo",
            "tiempo_preparacion": "55 min",
            "dificultad": "media",
            "ingredientes": {
                "costilla_cerdo": {"cantidad": 500, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "paprika": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar la costilla con ajo, comino, paprika, pimienta, sal y la mitad del limon",
                "Dejar reposar 15 minutos y cocinar en horno o Air Fryer hasta dorar y alcanzar coccion completa",
                "Cocinar arroz normalmente",
                "Lavar y cortar la lechuga y el tomate",
                "Aderezar la ensalada con el aceite y el limon restante",
                "Servir la costilla con arroz y ensalada"
            ],
            "informacion_nutricional": {
                "calorias": 690, "proteinas": 39, "carbohidratos": 55, "grasas": 34, "fibra": 5
            },
            "tags": ["proteina", "completo", "cerdo"]
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
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "paprika": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar alitas con ajo, paprika, pimienta y sal; pincelar con aceite",
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
                "comino": {"cantidad": 1.5, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 4, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Remojar frijol rojo y pezuña la noche anterior",
                "Cocinar pezuña con frijol rojo en olla a presion 1 hora",
                "Sofreir cebolla, tomate y ajo",
                "Agregar sofrito, comino y sal al guiso y cocinar 20 min mas",
                "Terminar con cilantro y servir con platano verde cocido o frito"
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
                "comino": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar las chuletas 20 minutos con ajo, comino, pimienta, sal y medio limon",
                "Cocinar papa francesa congelada en Air Fryer 15 min a 200 C",
                "Pincelar las chuletas con aceite y cocinar en sarten o Air Fryer 12 min a 190 C",
                "Servir chuletas con papas a la francesa y el limon restante"
            ],
            "informacion_nutricional": {
                "calorias": 680, "proteinas": 36, "carbohidratos": 48, "grasas": 38, "fibra": 5
            },
            "tags": ["proteina", "familiar"]
        },
        {
            "id": "alm_14",
            "nombre": "Pechuga asada con arroz y papas a la francesa",
            "categoria": "almuerzo",
            "tiempo_preparacion": "40 min",
            "dificultad": "facil",
            "ingredientes": {
                "pechuga_pollo": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "papa_francesa": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "paprika": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar el arroz con agua y sal hasta que este listo",
                "Mezclar la papa francesa con la mitad del aceite y cocinar en Air Fryer 15 min a 200 C",
                "Sazonar la pechuga con ajo picado, paprika, pimienta y sal",
                "Asar la pechuga en Air Fryer o plancha 15 min a 190 C hasta que este bien cocida",
                "Servir la pechuga asada con el arroz y las papas a la francesa"
            ],
            "informacion_nutricional": {
                "calorias": 620, "proteinas": 45, "carbohidratos": 68, "grasas": 15, "fibra": 4
            },
            "tags": ["proteina", "familiar"]
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
                "pimenton": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "achiote": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar pechuga de pollo en cubos",
                "Calentar el achiote en el aceite y sofreir cebolla, ajo, tomate y pimenton",
                "Agregar pollo, comino y pimienta, y dorar por todos lados",
                "Incorporar arroz, verduras y sal",
                "Agregar agua y cocinar hasta que el arroz este listo",
                "Dejar reposar 5 min, terminar con cilantro y servir"
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
                "ajo": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "mostaza": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "salsa_inglesa": {"cantidad": 5, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar lechuga",
                "Cocinar pechuga a la plancha, sazonar con sal y pimienta y cortar en tiras",
                "Hacer crutones con pan integral tostado",
                "Emulsionar limon, aceite de oliva, ajo, mostaza y salsa inglesa para el aderezo",
                "Mezclar todo y agregar queso parmesano"
            ],
            "informacion_nutricional": {
                "calorias": 380, "proteinas": 32, "carbohidratos": 20, "grasas": 18, "fibra": 4
            },
            "tags": ["ligero", "proteina", "rapido"]
        },
        {
            "id": "cen_02",
            "nombre": "Wrap de jamon y queso",
            "categoria": "cena",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "tortilla_harina": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "jamon": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "oregano": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar el tomate y la lechuga",
                "Calentar las tortillas en una sarten",
                "Distribuir jamon, queso, tomate y lechuga sobre cada tortilla",
                "Sazonar con oregano y pimienta",
                "Enrollar, dorar un minuto por lado y servir"
            ],
            "informacion_nutricional": {
                "calorias": 450, "proteinas": 28, "carbohidratos": 36, "grasas": 22, "fibra": 4
            },
            "tags": ["rapido", "practico", "proteina"]
        },
        {
            "id": "cen_03",
            "nombre": "Tortilla de huevo con jamon",
            "categoria": "cena",
            "tiempo_preparacion": "15 min",
            "dificultad": "facil",
            "ingredientes": {
                "huevo": {"cantidad": 4, "unidad": "unidades", "tipo": "unidad"},
                "jamon": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Picar el jamon y la cebolla; saltear la cebolla en parte del aceite",
                "Batir los huevos con sal y pimienta",
                "Agregar jamon y cebolla a los huevos",
                "Verter la mezcla en la sarten caliente",
                "Cocinar hasta que cuaje por ambos lados",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 31, "carbohidratos": 5, "grasas": 23, "fibra": 1
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
                "ajo": {"cantidad": 3, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar la pechuga con ajo, pimienta y parte de la sal; cocinar a la plancha y cortar en tiras",
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
                "nuez_moscada": {"cantidad": 0.3, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar todas las verduras",
                "Cocinar en agua con ajo y sal hasta que esten tiernas",
                "Licuar con crema de leche y mantequilla",
                "Volver a calentar y sazonar con pimienta y nuez moscada",
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
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "mostaza": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Tostar ligeramente el pan",
                "Untar mantequilla y una capa fina de mostaza",
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
                "cilantro": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas",
                "Mezclar atun con cebolla picada, cilantro, limon, pimienta y sal",
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
                "oregano": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pasta en agua con sal",
                "Picar tomate, zanahoria y cebolla",
                "Sofreir verduras con ajo, oregano y sal en aceite de oliva",
                "Mezclar pasta con verduras",
                "Terminar con pimienta y queso parmesano rallado"
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
                "picado_pollo": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "cebolla_larga": {"cantidad": 30, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 10, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 5, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 0.5, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Porcionar el picado de pollo si las piezas son grandes",
                "Picar zanahoria, papa y cebolla",
                "Hervir todo con ajo, comino, sal y la parte blanca de la cebolla larga por 25 min",
                "Agregar cilantro y la parte verde de la cebolla larga al final",
                "Servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 300, "proteinas": 28, "carbohidratos": 25, "grasas": 8, "fibra": 4
            },
            "tags": ["ligero", "reconfortante", "proteina"]
        },
        {
            "id": "cen_10",
            "nombre": "Arepa con queso",
            "categoria": "cena",
            "tiempo_preparacion": "12 min",
            "dificultad": "facil",
            "ingredientes": {
                "arepa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "queso_fresco": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 10, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Asar las arepas hasta que esten doradas",
                "Abrir las arepas con cuidado",
                "Rellenar con el queso fresco",
                "Untar la mantequilla por fuera",
                "Calentar hasta que el queso se ablande y servir"
            ],
            "informacion_nutricional": {
                "calorias": 390, "proteinas": 18, "carbohidratos": 40, "grasas": 18, "fibra": 3
            },
            "tags": ["colombiano", "rapido", "vegetariano"]
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
                "Picar la cebolla finamente y macerarla 10 minutos con el limon",
                "Abrir arepas y rellenar con chorizo y cebolla",
                "Servir con la cebolla encurtida"
            ],
            "informacion_nutricional": {
                "calorias": 420, "proteinas": 18, "carbohidratos": 38, "grasas": 22, "fibra": 3
            },
            "tags": ["colombiano", "rapido"]
        },
        {
            "id": "cen_12",
            "nombre": "Crema de champiñones de sobre",
            "categoria": "cena",
            "tiempo_preparacion": "12 min",
            "dificultad": "facil",
            "ingredientes": {
                "crema_champinones_sobre": {"cantidad": 1, "unidad": "sobres", "tipo": "unidad"},
                "leche": {"cantidad": 500, "unidad": "ml", "tipo": "volumen"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Revisar en el empaque la cantidad de liquido indicada para un sobre",
                "Disolver el contenido del sobre en una parte de la leche fria",
                "Agregar el resto de la leche y llevar a fuego medio",
                "Revolver continuamente hasta que hierva y espese",
                "Terminar con pimienta y servir caliente"
            ],
            "informacion_nutricional": {
                "calorias": 260, "proteinas": 10, "carbohidratos": 34, "grasas": 9, "fibra": 1
            },
            "tags": ["rapido", "reconfortante", "despensa"]
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
                "pimenton": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "cilantro": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "comino": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Limpiar las menudencias con papel de cocina y picarlas sin lavarlas bajo el grifo",
                "Sofreir cebolla, ajo, pimenton y tomate en aceite",
                "Agregar menudencias, comino, pimienta y sal, cocinar 15 min",
                "Incorporar papa y zanahoria picadas",
                "Cocinar hasta que las verduras esten tiernas, terminar con cilantro y servir"
            ],
            "informacion_nutricional": {
                "calorias": 320, "proteinas": 30, "carbohidratos": 28, "grasas": 10, "fibra": 4
            },
            "tags": ["colombiano", "economico", "proteina"]
        },
        {
            "id": "cen_14",
            "nombre": "Panquecas con jamon",
            "categoria": "cena",
            "tiempo_preparacion": "25 min",
            "dificultad": "facil",
            "ingredientes": {
                "harina": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "huevo": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "leche": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "jamon": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Separar el huevo y batir la clara a punto de nieve",
                "Mezclar harina, sal y pimienta con la yema y la leche",
                "Incorporar la clara con movimientos envolventes",
                "Picar el jamon e incorporarlo a la mezcla",
                "Engrasar una sarten con mantequilla y verter porciones",
                "Cocinar las panquecas por ambos lados hasta dorar y servir"
            ],
            "informacion_nutricional": {
                "calorias": 510, "proteinas": 25, "carbohidratos": 58, "grasas": 20, "fibra": 3
            },
            "tags": ["rapido", "salado", "practico"]
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
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "pimenton": {"cantidad": 40, "unidad": "gr", "tipo": "peso"},
                "comino": {"cantidad": 2, "unidad": "gr", "tipo": "peso"},
                "pimienta": {"cantidad": 1, "unidad": "gr", "tipo": "peso"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar platano verde en rodajas gruesas",
                "Freir platano, aplastar y freir de nuevo",
                "Preparar un sofrito con cebolla, ajo, tomate y pimenton; agregar carne, comino, pimienta y sal",
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
