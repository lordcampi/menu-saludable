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
            "nombre": "Cereal con frutas y yogurt",
            "categoria": "desayuno",
            "tiempo_preparacion": "5 min",
            "dificultad": "facil",
            "ingredientes": {
                "cereal": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "yogurt": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "fresas": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "banano": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Servir el cereal en un tazon",
                "Agregar yogurt frio",
                "Cortar frutas y agregar encima",
                "Mezclar y disfrutar"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 12, "carbohidratos": 50, "grasas": 10, "fibra": 5
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
                "yogurt": {"cantidad": 200, "unidad": "ml", "tipo": "volumen"},
                "miel": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "nueces": {"cantidad": 20, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Lavar y cortar fresas en mitades",
                "Pelar y cortar banano en rodajas",
                "Servir yogurt en tazon",
                "Agregar frutas encima",
                "Decorar con nueces y miel"
            ],
            "informacion_nutricional": {
                "calorias": 300, "proteinas": 10, "carbohidratos": 45, "grasas": 10, "fibra": 5
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
                "bistec_res": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Sazonar bistec con sal y limon",
                "Cocinar arroz normalmente",
                "Cocinar bistec a la plancha 4 min por lado",
                "Lavar y cortar lechuga y tomate",
                "Servir bistec con arroz y ensalada"
            ],
            "informacion_nutricional": {
                "calorias": 580, "proteinas": 42, "carbohidratos": 55, "grasas": 20, "fibra": 5
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
                "pechuga_pollo": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "brocoli": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cortar pechuga en cubos",
                "Picar cebolla y tomate",
                "Sofreir cebolla y tomate en aceite",
                "Agregar pollo y cocinar 15 min",
                "Agregar zanahoria y brocoli",
                "Cocinar hasta que este tierno",
                "Servir con arroz blanco"
            ],
            "informacion_nutricional": {
                "calorias": 550, "proteinas": 40, "carbohidratos": 58, "grasas": 16, "fibra": 6
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
                "carne_molida": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 120, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "huevo": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"},
                "leche": {"cantidad": 100, "unidad": "ml", "tipo": "volumen"},
                "mantequilla": {"cantidad": 20, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Mezclar carne molida con huevo y sal",
                "Formar albondigas y dorar en aceite",
                "Licuar tomate y cebolla para salsa",
                "Cocinar albondigas en la salsa 20 min",
                "Cocinar papas, hacer pure con leche y mantequilla",
                "Servir albondigas sobre pure"
            ],
            "informacion_nutricional": {
                "calorias": 620, "proteinas": 35, "carbohidratos": 48, "grasas": 30, "fibra": 6
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
                "aceite": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Marinar pescado con limon y sal",
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
            "nombre": "Sancocho colombiano de gallina",
            "categoria": "almuerzo",
            "tiempo_preparacion": "1 hora 30 min",
            "dificultad": "media",
            "ingredientes": {
                "gallina": {"cantidad": 400, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "yuca": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
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
            "id": "alm_09",
            "nombre": "Hamburguesas caseras con papas fritas",
            "categoria": "almuerzo",
            "tiempo_preparacion": "35 min",
            "dificultad": "facil",
            "ingredientes": {
                "carne_molida": {"cantidad": 350, "unidad": "gr", "tipo": "peso"},
                "pan_hamburguesa": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "papa": {"cantidad": 300, "unidad": "gr", "tipo": "peso"},
                "tomate": {"cantidad": 80, "unidad": "gr", "tipo": "peso"},
                "lechuga": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "queso_fresco": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 30, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Formar hamburguesas con la carne molida",
                "Cocinar en sarten 4-5 min por lado",
                "Pelar y cortar papas en bastones",
                "Freir papas hasta dorar",
                "Armar hamburguesa con tomate, lechuga y queso",
                "Servir con papas fritas"
            ],
            "informacion_nutricional": {
                "calorias": 700, "proteinas": 40, "carbohidratos": 55, "grasas": 35, "fibra": 5
            },
            "tags": ["rapido", "familiar", "ocasional"]
        },
        {
            "id": "alm_10",
            "nombre": "Empanadas de carne con arroz",
            "categoria": "almuerzo",
            "tiempo_preparacion": "45 min",
            "dificultad": "media",
            "ingredientes": {
                "carne_molida": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "harina": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "aceite": {"cantidad": 40, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 3, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar carne molida con cebolla y papa picada",
                "Preparar masa con harina, agua y sal",
                "Rellenar y formar empanadas",
                "Freir en aceite caliente hasta dorar",
                "Servir con arroz blanco"
            ],
            "informacion_nutricional": {
                "calorias": 650, "proteinas": 28, "carbohidratos": 62, "grasas": 32, "fibra": 4
            },
            "tags": ["colombiano", "especial"]
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
                "aceite_oliva": {"cantidad": 20, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Lavar y cortar lechuga",
                "Cocinar pechuga a la plancha y cortar en tiras",
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
                "yogurt": {"cantidad": 50, "unidad": "ml", "tipo": "volumen"}
            },
            "preparacion": [
                "Cocinar pechuga a la plancha y cortar en tiras",
                "Machacar aguacate",
                "Picar tomate y lechuga",
                "Calentar tortillas",
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
            "tiempo_preparacion": "30 min",
            "dificultad": "facil",
            "ingredientes": {
                "zapallo": {"cantidad": 250, "unidad": "gr", "tipo": "peso"},
                "zanahoria": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "papa": {"cantidad": 150, "unidad": "gr", "tipo": "peso"},
                "crema_leche": {"cantidad": 80, "unidad": "ml", "tipo": "volumen"},
                "mantequilla": {"cantidad": 15, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Pelar y cortar todas las verduras",
                "Cocinar en agua hasta que esten tiernas",
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
                "limon": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            },
            "preparacion": [
                "Asar las arepas",
                "Mezclar atun con cebolla picada y limon",
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
                "tomate": {"cantidad": 100, "unidad": "gr", "tipo": "peso"},
                "pimenton": {"cantidad": 60, "unidad": "gr", "tipo": "peso"},
                "cebolla": {"cantidad": 50, "unidad": "gr", "tipo": "peso"},
                "ajo": {"cantidad": 8, "unidad": "gr", "tipo": "peso"},
                "aceite_oliva": {"cantidad": 15, "unidad": "ml", "tipo": "volumen"},
                "queso_parmesano": {"cantidad": 20, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar pasta en agua con sal",
                "Picar tomate, pimenton y cebolla",
                "Sofreir verduras con ajo en aceite de oliva",
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
            "nombre": "Arroz con huevo frito",
            "categoria": "cena",
            "tiempo_preparacion": "20 min",
            "dificultad": "facil",
            "ingredientes": {
                "arroz": {"cantidad": 200, "unidad": "gr", "tipo": "peso"},
                "huevo": {"cantidad": 2, "unidad": "unidades", "tipo": "unidad"},
                "aceite": {"cantidad": 10, "unidad": "ml", "tipo": "volumen"},
                "sal": {"cantidad": 2, "unidad": "gr", "tipo": "peso"}
            },
            "preparacion": [
                "Cocinar arroz normalmente",
                "Calentar aceite en sarten",
                "Freir huevos con cuidado",
                "Servir arroz con huevo encima",
                "Acompanar con ensalada si se desea"
            ],
            "informacion_nutricional": {
                "calorias": 350, "proteinas": 14, "carbohidratos": 50, "grasas": 10, "fibra": 2
            },
            "tags": ["ligero", "rapido", "economico"]
        }
    ]
}