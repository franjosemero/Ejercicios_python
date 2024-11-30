frase=input("introduce una frase ")
letra=input("introduce la letra")
contador = 0
for i in frase:
    if i  == letra:
        contador += 1
print("la letra '%s' aparece %2i veces en la frase '%s'. " % (letra,contador,frase))
#     ( el simbolo %s,%s,%s concatena con lo marcado en el parentesis seguido de %( 1,2,3 ))