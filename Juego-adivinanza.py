
from operator import truediv
import random


numero_secreto = random.randint(1,100)
cant_intentos = 0
cant_max_intentos = 10
adivinado = False

print ("Bienvenido al juego de adivinar el nro secreto")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = input("introduce un nro del 1 al 100: ")
    numero = int(entrada)

    if numero == numero_secreto:
        print("Felicidades, ganaste")
        adivinado = True
    elif numero < numero_secreto:
        print("Ingresa un Numero mayor")
    else:
        print("Ingresa un Numero menor")

    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print ("Game Over! no has podido adivinar dentro de los 5 intentos")