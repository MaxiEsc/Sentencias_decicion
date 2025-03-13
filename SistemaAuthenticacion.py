#Sistema de authenticacion con comprobaciones en if y elif

print('--> Sistema de Autenticación <--')

USUARIO = 'admin'
PASSWORD = '123'

usuario = input('Ingresa tu usuario: ')
password = input('Ingresa tu password: ')

if usuario == USUARIO and password == PASSWORD:
    print('Bienvenido al Sistema')
elif usuario == USUARIO:
    print('Password incorrecto, favor de corregirlo!')
elif password == PASSWORD:
    print('Usuario incorrecto, favor de corregirlo!')
else:
    print('Usuario y password incorrectos, favor de corregirlos!')
