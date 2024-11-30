

palabra=input("intrudice una palabra:  ")
invert_palabra = palabra
palabra = list(palabra)
invert_palabra= list(invert_palabra)
invert_palabra.reverse()

if palabra == invert_palabra :
    print ("es un polindromo ")
else:
    print("no es un polidromo ")







"""
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")"""