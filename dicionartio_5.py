"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será 
el número de factura y el valor el coste de la factura. El programa debe preguntar 
al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su
coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el 
número de factura y se eliminará del diccionario. Después de cada operación el programa 
debe mostrar por pantalla la cantidad 
cobrada hasta el momento y la cantidad pendiente de cobro.

facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

"""

factur_global={}
facturas = {}
cobrado = 0
pendientes = 0
mas = ""
while mas != "S":
    if mas == "A":
        clave = input ("introduce el numero de factura: ")
        coste = float(input("introduce el importe de la factura :"))
        factur_global[clave]=coste
        facturas[clave]= coste
        pendientes += coste
    if mas == "P":
        clave = input ("introduce el numero de factura a pagar: ") 
        coste = facturas.pop(clave,0)
        cobrado += coste
        pendientes -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendientes)
    print(facturas)
    print(factur_global)

    mas=input("quiere añadir una factura nueva (A),quiere pagar una factura (P), quiere salir (S)")
 





