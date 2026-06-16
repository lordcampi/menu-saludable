"""
Plan fijo de 15 dias - Julian y Annmar
Cada dia tiene desayuno, almuerzo y cena unicos (45 recetas distintas).
"""

MENU_DIAS = [
    {"dia": 1, "desayuno": "des_08", "almuerzo": "alm_06", "cena": "cen_01"},
    {"dia": 2, "desayuno": "des_06", "almuerzo": "alm_08", "cena": "cen_11"},
    {
        "dia": 3,
        "desayuno": "des_15",
        "almuerzo": "alm_05",
        "cena": "cen_05",
        "overrides": {
            "almuerzo": {
                "platano_maduro": {"cantidad": 1, "unidad": "unidades", "tipo": "unidad"}
            }
        },
    },
    {"dia": 4, "desayuno": "des_09", "almuerzo": "alm_10", "cena": "cen_09"},
    {"dia": 5, "desayuno": "des_03", "almuerzo": "alm_09", "cena": "cen_03"},
    {"dia": 6, "desayuno": "des_04", "almuerzo": "alm_04", "cena": "cen_06"},
    {"dia": 7, "desayuno": "des_07", "almuerzo": "alm_01", "cena": "cen_04"},
    {"dia": 8, "desayuno": "des_10", "almuerzo": "alm_11", "cena": "cen_12"},
    {"dia": 9, "desayuno": "des_02", "almuerzo": "alm_02", "cena": "cen_07"},
    {"dia": 10, "desayuno": "des_11", "almuerzo": "alm_12", "cena": "cen_13"},
    {"dia": 11, "desayuno": "des_05", "almuerzo": "alm_13", "cena": "cen_08"},
    {"dia": 12, "desayuno": "des_01", "almuerzo": "alm_14", "cena": "cen_02"},
    {"dia": 13, "desayuno": "des_12", "almuerzo": "alm_07", "cena": "cen_10"},
    {"dia": 14, "desayuno": "des_13", "almuerzo": "alm_03", "cena": "cen_14"},
    {"dia": 15, "desayuno": "des_14", "almuerzo": "alm_15", "cena": "cen_15"},
]

DIAS_PLAN = 15
