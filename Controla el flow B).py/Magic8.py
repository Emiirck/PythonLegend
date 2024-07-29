
import random

pregunta = input('Pregunta:      ')

numero_aleatorio = random.randint(1, 9)

# La declaración if/elif/else comienza aquí
if numero_aleatorio == 1:
    print("Bola 8 Mágica: Sí, definitivamente.")
elif numero_aleatorio == 2:
    print("Bola 8 Mágica: Es decididamente así.")
elif numero_aleatorio == 3:
    print("Bola 8 Mágica: Sin duda.")
elif numero_aleatorio == 4:
    print("Bola 8 Mágica: Respuesta confusa, intenta de nuevo.")
elif numero_aleatorio == 5:
    print("Bola 8 Mágica: Pregunta de nuevo más tarde.")
elif numero_aleatorio == 6:
    print("Bola 8 Mágica: Mejor no te lo digo ahora.")
elif numero_aleatorio == 7:
    print("Bola 8 Mágica: Mis fuentes dicen que no.")
elif numero_aleatorio == 8:
    print("Bola 8 Mágica: La perspectiva no es tan buena.")
else:
    print("Bola 8 Mágica: Muy dudoso.")
