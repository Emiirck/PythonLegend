
import random

def tirar_dado():
    return random.randint(1, 6)

def jugar_pig():
    puntuacion_jugador = 0
    puntuacion_computadora = 0
    objetivo = 100
    
    while puntuacion_jugador < objetivo and puntuacion_computadora < objetivo:
       
        turno_jugador = True
        puntuacion_temporal = 0
        
        print("\nTurno del jugador")
        
        while turno_jugador:
            tirada = tirar_dado()
            print(f"Tiraste un {tirada}")
            
            if tirada == 1:
                print("¡Perdiste todos los puntos de este turno!")
                puntuacion_temporal = 0
                turno_jugador = False
            else:
                puntuacion_temporal += tirada
                print(f"Puntos temporales: {puntuacion_temporal}")
                decision = input("¿Deseas guardar los puntos? (s/n): ").lower()
                if decision == 's':
                    puntuacion_jugador += puntuacion_temporal
                    turno_jugador = False
            
        print(f"Puntuación total del jugador: {puntuacion_jugador}")
        
        
        if puntuacion_jugador < objetivo:
            turno_computadora = True
            puntuacion_temporal = 0
            
            print("\nTurno de la computadora")
            
            while turno_computadora:
                tirada = tirar_dado()
                print(f"La computadora tiró un {tirada}")
                
                if tirada == 1:
                    print("La computadora perdió todos los puntos de este turno!")
                    puntuacion_temporal = 0
                    turno_computadora = False
                else:
                    puntuacion_temporal += tirada
                    if puntuacion_temporal >= 20 or (puntuacion_temporal + puntuacion_computadora) >= objetivo:
                        puntuacion_computadora += puntuacion_temporal
                        turno_computadora = False
            
            print(f"Puntuación total de la computadora: {puntuacion_computadora}")
    
    if puntuacion_jugador >= objetivo:
        print("\n¡Felicidades! Has ganado el juego.")
    else:
        print("\nLa computadora ha ganado. ¡Suerte la próxima vez!")

jugar_pig()
