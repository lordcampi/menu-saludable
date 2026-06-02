# Arreglar pan integral en recetas
with open('data/recetas.py', 'r', encoding='utf-8') as f:
    contenido = f.read()

# Cambiar pan en rebanadas a gramos
viejo = '"pan_integral": {"cantidad": 4, "unidad": "rebanadas", "tipo": "unidad"}'
nuevo = '"pan_integral": {"cantidad": 100, "unidad": "gr", "tipo": "peso"}'

contenido = contenido.replace(viejo, nuevo)

with open('data/recetas.py', 'w', encoding='utf-8') as f:
    f.write(contenido)

print('✅ Pan integral estandarizado a gramos')
print('   4 rebanadas = 100gr = tipo peso')