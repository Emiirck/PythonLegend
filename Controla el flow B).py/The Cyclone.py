
altura = int(input('¿Cuál es tu altura (cm)? '))
creditos = int(input('¿Cuántos créditos tienes? '))

if altura >= 150 and creditos >= 10:
    print('¡Disfruta del paseo!')
elif creditos >= 10 and altura < 150:
    print('No tienes la altura suficiente para montar.')
elif altura >= 150 and creditos < 10:
    print('No tienes suficientes créditos.')
else:
    print('No cumples con ningún requisito.')