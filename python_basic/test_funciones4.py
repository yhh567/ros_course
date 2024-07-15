from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")


while True:
    print("Moviendo")
    sentido = input('Introduce un sentido de movimiento para el robot <<forward o backward>>: ')
    velocidad = float(input('Introduce una velocidad de movimiento: '))
    tiempo = int(input('Introduce el tiempo en movimiento: '))
    en_movimiento = rc.move_straight_time(sentido, velocidad, tiempo)
    print(en_movimiento)

    print("Girando")
    sentido_giro = input('Introduce un sentido de giro <<clockwise o counter-clockwise>>: ')
    velocida_giro = float(input("Introduce una velocidad del giro: "))
    tiempo_giro = int(input("Introduce el tiempo de giro: "))
    girando = rc.turn(sentido, velocidad, tiempo)
    print(girando)

    continuar = input('Deseas continuar? <<Si o No>>: ').lower()
    if continuar != 'si':
        print("Finalizando el programa")
        break

