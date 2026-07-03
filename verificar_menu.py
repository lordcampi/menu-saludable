"""
Script de verificación del menú con el nuevo sistema de miembros del hogar.
Muestra el menú generado y las cantidades escaladas según los miembros activos.
"""
from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager
from data.hogar import cargar_miembros, get_miembros_activos, get_factor_consumo_total, get_factor_escalado, FACTOR_BASE_REFERENCIA

miembros = cargar_miembros()
activos = get_miembros_activos(miembros)
factor_total = get_factor_consumo_total(miembros)
factor_escalado = get_factor_escalado(miembros)

print("=" * 70)
print("VERIFICACIÓN DEL SISTEMA DE MENÚ CON MIEMBROS DEL HOGAR")
print("=" * 70)

print("\n🏠 MIEMBROS DEL HOGAR:")
for m in miembros:
    estado = "ACTIVO" if m["activo"] else "INACTIVO"
    print(f"  [{estado}] {m['nombre']} (factor: {m['factor_consumo']})")

print(f"\n📊 Factor de consumo total: {factor_total:.2f}")
print(f"📊 Factor de escalado: {factor_escalado:.2f}")
print(f"📊 Factor base de referencia: {FACTOR_BASE_REFERENCIA}")

if factor_total != FACTOR_BASE_REFERENCIA:
    delta = ((factor_total - FACTOR_BASE_REFERENCIA) / FACTOR_BASE_REFERENCIA) * 100
    print(f"⚠️  Escalado aplicado: {'+' if delta > 0 else ''}{delta:.0f}%")
else:
    print(f"✓  Sin escalado (comportamiento original)")

mg = MenuGenerator()
menu = mg.cargar_menu_fijo()

des = [d["desayuno"]["nombre"] for d in menu]
alm = [d["almuerzo"]["nombre"] for d in menu]
cen = [d["cena"]["nombre"] for d in menu]

print(f"\n📅 Menú cargado: {len(menu)} días")
print(f"  Desayunos únicos: {len(set(des))}/{len(des)}")
print(f"  Almuerzos únicos: {len(set(alm))}/{len(alm)}")
print(f"  Cenas únicas: {len(set(cen))}/{len(cen)}")
print(f"  Recetario total: {len(mg.get_todas_las_recetas())} recetas")

inv = InventoryManager(menu)
print(f"  Ingredientes en inventario: {len(inv.inventario_necesario)}")

# Verificar que el escalado funciona correctamente con una receta de ejemplo
print("\n🔍 VERIFICACIÓN DE ESCALADO (receta de ejemplo):")
receta_ejemplo = menu[0]["almuerzo"]
print(f"  Receta: {receta_ejemplo['nombre']} (Día {menu[0]['dia']})")
for ing, datos in list(receta_ejemplo["ingredientes"].items())[:5]:
    print(f"    {ing}: {datos['cantidad']} {datos['unidad']}")

print("\n📋 MENÚ COMPLETO:")
for d in menu:
    print(
        f"  Día {d['dia']:2d}: {d['desayuno']['nombre']:<40s} | "
        f"{d['almuerzo']['nombre']:<40s} | {d['cena']['nombre']}"
    )

# Verificar consistencia: todas las recetas deben tener ingredientes
errores = 0
for d in menu:
    for comida in ["desayuno", "almuerzo", "cena"]:
        if not d[comida].get("ingredientes"):
            print(f"  ❌ ERROR: Día {d['dia']} {comida} no tiene ingredientes")
            errores += 1

if errores == 0:
    print(f"\n✅ Todas las recetas tienen ingredientes correctamente cargados.")
else:
    print(f"\n❌ Se encontraron {errores} errores.")