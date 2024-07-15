from microproyecto_oop import RoboMov

""""
Descripcion: El microproyecto consiste en sacar al robot de un laberinto.

El siguiente codigo es el main del programa, que consiste en interacciones con el usuario para realizar acciones sobre el robot
"""

robo = RoboMov()

while True:

    accion = input("Que accion quieres realizar? <<(M)over/m(O)ver con parada/(R)otar/>>: ").lower()

    # Movimiento principal en linea recta con deteccion de obstaculos a 1 m
    if accion == 'm':
        d = robo.escaneo() # Escaneo de obstaculos
        while d > 1: # Mientras la distancia sea de 1 metro
            robo.en_movimiento() # Mover
            d = robo.escaneo() # Escanear de nuevo     
        robo.parar() # Parar          

    # Movimiento con parada en el tiempo
    elif accion == 'o':
        robo.en_movimiento_con_parada()

    # Rotar el robot
    elif accion == 'r':
        robo.girando()

    else:
        print("Introduce una de las acciones válidas.")

    continuar = input("Seguir controlando el robot?: <<S/N>>: ").lower()
    if continuar != 's' and continuar != 'si':
        break

print("Finalizado")