
#Instrucciones: Dada una tupla de números (10, 20, 30, 40, 50), realiza las siguientes tareas:
#Accede e imprime el tercer elemento de la tupla.
#Desempaqueta los elementos de la tupla en variables individuales.
#Crea una nueva tupla que contenga los primeros tres elementos de la tupla original.

tuple = [10,20,30,40,50]

tercer = tuple[2]

print("El tercer elemento de la tupla es: ", tercer)

print("Elementos desempaquetados:")

print("a:", 10)
print("b:", 20)
print("c:", 30)
print("d:", 40)
print("e:", 50)

ntuple = tuple[:3]

print("primeros tres elementos:", ntuple)