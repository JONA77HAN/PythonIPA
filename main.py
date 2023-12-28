import random

frases = [
    "¡Hola, mundo!",
    "Python es increíble.",
    "La creatividad es contagiosa, pásala.",
    "Programar es como resolver un rompecabezas.",
    "La curiosidad es la clave del aprendizaje.",
]

#######3 comienzo del programa
print('Bienvenido a mi programa:')
print('soy IPA')
# bien aca, ponerle un freno a la pregunta inmediata


# conseguir aprender como hacer la barra invertida
# para luego ponerle la aclaracion una linea debajo

nombre = input('¿cuál es tu nombre? ...')
amor_yas = random.choice(frases)
# aca comienza el desafio, hacer q esto que te contesta, te esta contestando realmente

if nombre == 'yasmin':
    print(amor_yas)

print(nombre)



