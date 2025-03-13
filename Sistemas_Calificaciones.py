print('*** Sistema de Calificaciones ***')

calif = float(input('Proporciona una calificación entre 0 y 10: '))
calif_letra = None
# Revisamos si está en los siguientes rangos
if 9 <= calif <= 10:
    calif_letra = 'A'
elif 8 <= calif < 9:
    calif_letra = 'B'
elif 7 <= calif < 8:
    calif_letra = 'C'
elif 6 <= calif < 7:
    calif_letra = 'D'
elif 0 <= calif < 6:
    calif_letra = 'F'
else:
    calif_letra = 'Calificacion incorrecta'

# Imprimir el resultado
print(f'Calificación {calif} es equivalente a {calif_letra}')