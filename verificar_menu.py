from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager

mg = MenuGenerator()
menu = mg.cargar_menu_fijo()
des = [d["desayuno"]["nombre"] for d in menu]
alm = [d["almuerzo"]["nombre"] for d in menu]
cen = [d["cena"]["nombre"] for d in menu]
print("Dias:", len(menu))
print("Desayunos unicos:", len(set(des)), "/", len(des))
print("Almuerzos unicos:", len(set(alm)), "/", len(alm))
print("Cenas unicas:", len(set(cen)), "/", len(cen))
print("Recetario:", len(mg.get_todas_las_recetas()))
inv = InventoryManager(menu)
print("Ingredientes inventario:", len(inv.inventario_necesario))
for d in menu:
    print(
        f"Dia {d['dia']}: {d['desayuno']['nombre']} / "
        f"{d['almuerzo']['nombre']} / {d['cena']['nombre']}"
    )
