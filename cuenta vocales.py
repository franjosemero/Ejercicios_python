

palabra = input("intrudice una palabra:  ")
vocales = ['a','e','i','o','u']
for vocal in vocales:
    count = 0
    for letra in palabra:
        if letra == vocal :
            count += 1
    print("la vocal" , vocal , "aparece" , str(count) , "veces" )







"""
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")"""