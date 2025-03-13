# Sentencias de decision de Python

#Bloque elseif

edad = 9
print(f'*** Sentencia Simple IF')
if edad <= 18:
    print(f'Eres menor a 18 años')
    print (f'Posees {edad} de años' )
elif edad >= 60:
    print(f'Eres un abuelo')
    print(f'Eres mayor de edad posees {edad} de edad')
else:
    print(f'Eres mayor de edad posees {edad} de edad')