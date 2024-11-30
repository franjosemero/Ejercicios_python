

""" Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
ada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""


persona = {}
continuar= True
while continuar:
    clave = input ("¿que dato quieres introducir : ?")
    valor = input (clave + ' :')
    persona[clave] = valor
    print(persona)
    continuar = input("¿Quieres añadir mas datos (Si/No ) ?") == "Si"

#datos_usuario=persona     guardar los datos en una variable nueva
#print(datos_usuario)





