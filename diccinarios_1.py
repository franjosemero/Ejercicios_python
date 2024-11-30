

# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
# upper()  lo convierte todo en mayusculas
# lower()  lo convierte todo en minusculas
# title()  convierte la primera en muyusculas


monedas={'Euros':'€', 'Dolares':'$','Yens':'¥'}  

divisa=input("introduzca su divisa: ")
if divisa in monedas:
    print(monedas[divisa])
else:
    print("divisa no valida ")






monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
print(monedas.get(divisa.title(), "La divisa no está."))



monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa: ")
if divisa.title() in monedas:
    print(monedas[divisa.title()])
else:
    print("La divisa no está.")