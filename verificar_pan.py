from data.menu_generator import MenuGenerator
from data.inventory import InventoryManager

mg = MenuGenerator(dias=15)
menu = mg.generar_menu()
inv = InventoryManager(menu)

if 'pan_integral' in inv.inventario_necesario:
    pan = inv.inventario_necesario['pan_integral']
    print(f'Pan necesario para 15 dias: {pan["cantidad"]} {pan["unidad"]}')
    print(f'Equivale a {pan["cantidad"]/1000:.1f} kg')
    print(f'Paquetes D1 (450gr): {pan["cantidad"]/450:.1f}')
    print(f'Costo D1: ${pan["cantidad"]/450 * 3600:,.0f} COP')
else:
    print('No hay pan en el menu actual')

# Mostrar recetas con pan
print('\nRecetas que usan pan integral:')
for dia in menu:
    for comida in ['desayuno', 'almuerzo', 'cena']:
        receta = dia[comida]
        if 'pan_integral' in receta['ingredientes']:
            pan = receta['ingredientes']['pan_integral']
            print(f'  Dia {dia["dia"]}: {receta["nombre"]} - {pan["cantidad"]} {pan["unidad"]}')