

"""Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>."""


nombre=input("Cual es su mnombre:")
edad=input("cual es tu edad: ")
direccion=input("Introduce tu direccion: ")
telefono=input("introduce tu telefono: ")
usuario={"nombre": nombre , "edad": edad ,"direccion": direccion , "telefono": telefono, }
print(usuario["nombre"],'tiene ', usuario["edad"],'vive en ' ,usuario["direccion"],'su telefono es: ',usuario["telefono"],)





