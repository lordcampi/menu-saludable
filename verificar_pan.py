from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager
from data.menu_fijo import DIAS_PLAN

mg = MenuGenerator(dias=DIAS_PLAN, personas=2)
menu = mg.cargar_menu_fijo()
inv = InventoryManager(menu)

if 'pan_integral' in inv.inventario_necesario:
    pan = inv.inventario_necesario['pan_integral']
    print(f'Pan necesario para {DIAS_PLAN} dias: {pan["cantidad"]} {pan["unidad"]}')
    print(f'Equivale a {pan["cantidad"]/1000:.1f} kg')
    print(f'Paquetes D1 (450gr): {pan["cantidad"]/450:.1f}')
    print(f'Costo D1: ${pan["cantidad"]/450 * 3600:,.0f} COP')
else:
    print('No hay pan en el menu actual')

print('\nRecetas que usan pan integral:')
for dia in menu:
    for comida in ['desayuno', 'almuerzo', 'cena']:
        receta = dia[comida]
        if 'pan_integral' in receta['ingredientes']:
            pan_ing = receta['ingredientes']['pan_integral']
            print(f'  Dia {dia["dia"]}: {receta["nombre"]} - {pan_ing["cantidad"]} {pan_ing["unidad"]}')
