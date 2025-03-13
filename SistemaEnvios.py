

print('--> Sistema de Envíos <--')

# Definimos las tarifas de envío por kilogramo
TARIFA_NAC = 10
TARIFA_INT = 20

# Solicitamos los valores de destino y peso al usuario
destino = input('Ingresa el destino del paquete (nacional/internacional): ')
peso = float(input('Ingresa el peso del paquete (en kg): '))

# Cálculo del envío del paquete
cost_envio = None
destino = destino.strip().lower()
if destino == 'nacional':
    cost_envio = peso * TARIFA_NAC
elif destino == 'internacional':
    cost_envio = peso * TARIFA_INT
else:
    print('Destino no válido. Ingresa el valor de nacional o internacional')

# Mostramos el costo de envío sólo si es un valor válido
if cost_envio is not None:
    print(f'El costo de envío del paquete es: ${cost_envio:.2f}')