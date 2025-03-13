#Tienda de descuentos

miembro = "SI"
compra = 1000
if compra >= 1000 and miembro == "SI":
    compra = compra - (compra*5)/100
    compra = compra - (compra*10)/100
    print(f'Precio Final a abonar en total ${compra} final')
elif compra >= 1000 and miembro == "NO":
    compra = compra - (compra*10)/100
    print(f'Precio Final a abonar en total ${compra} final')
else:
    print(f'Precio Final a abonar en total ${compra} final')