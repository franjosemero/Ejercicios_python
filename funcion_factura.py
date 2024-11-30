
""" Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%."""




def factura(importe, iva):

    importe=float(input('introduzca importe: '))
    iva=float(input('introduzca tipo iva: '))
    return importe + importe*iva/100

print(factura('','' ))
print(factura( '',''))




#def invoice(amount, vat=21): #valor fijo al iva

#   return amount + amount*vat/100

#print(invoice(1000,10))
#print(invoice(1000))



