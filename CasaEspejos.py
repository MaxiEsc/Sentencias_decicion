print('--> Bienvenidos a la Casa de los Espejos <--')

edad = int(input('Ingresa tu edad? '))
temes_oscuridad = input('Temes a la oscuridad (Si/No)? ')
temes_oscuridad = temes_oscuridad.strip().lower() == 'si'

if not temes_oscuridad and edad >= 10:
    print('Puedes ingresar a la Casa de los Espejos')
else:
    print('Lo siento, la Casa de los Espejos podría darte miedo')
