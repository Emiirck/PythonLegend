
print('BANCO DE CODÉDEX')

pin = int(input('Introduce tu PIN: '))

while pin != 1234:
    pin = int(input('PIN incorrecto. Introduce tu PIN nuevamente: '))

if pin == 1234:
    print('¡PIN aceptado!')
