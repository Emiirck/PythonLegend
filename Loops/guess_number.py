
adivinanza = 0
intentos = 0

while adivinanza != 6 and intentos < 7:
    adivinanza = int(input("Adivina el número:  "))
    intentos += 1

print("¡Lo adivinaste!")
