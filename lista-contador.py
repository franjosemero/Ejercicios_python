asignaturas = ['matematicas','ingles','filosofia','castellano','fisica','quimica','etica','informatica']

for i in asignaturas:
   nota=input('que nota sacaste en '+ i)
for i in asignaturas : 
    print("mi nota en: " + i ,'es' + nota ) 
  
# LA FORMA DE SOLUCION DEL CURSO
"""
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])"""