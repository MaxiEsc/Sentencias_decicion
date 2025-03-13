#Poniendo en practica conceptos de Ternario

print('*** Aplicación de Salud y Fitness ***')

# Constantes
META_DIARIA = 10000
CALORIAS_PASO = 0.04 # Valor aproximado, son kilocalorias

# Pedimos los valores al usuario
nombre_usuario = input('Cuál es tu nombre? ')
paso_diario = int(input('Cuántos pasos has caminado hoy? '))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = paso_diario >= META_DIARIA
# TERNARIO PARA DECIDIR EL eEL SI o NO
meta_alcanzada_txt = 'Sí' if meta_alcanzada else 'No'
# Calculamos las calorias quemadas
calorias_quemadas = paso_diario * CALORIAS_PASO

# Mostra de detalles
print(f'\nUsuario: {nombre_usuario}')
print(f'Pasos dados hoy: {paso_diario}')
print(f'Calorías quemadas: {calorias_quemadas} kcal')
print(f'Meta de pasos diario alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_DIARIA} pasos')