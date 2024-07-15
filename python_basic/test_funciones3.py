from robot_control_class import RobotControl
import time


rc = RobotControl(robot_name="summit")

def en_movimiento(sentido, velocidad, tiempo):
    s = rc.move_straight_time(sentido, velocidad, tiempo)
    return s

def girando(sentido, velocidad, tiempo):
    s = rc.turn(sentido, velocidad, tiempo)
    return s

print("En movimiento")
print(en_movimiento('forward', 0.3, 5)) # En movimiento delante 5 segundos a 0.3 m/s
print("Parado")
time.sleep(10) # Delay de 10 segundos
print("Girando")
print(girando('clockwise', 0.3, 7))# Girando sentido horario durante 7 segundos a 0.3 rad/s
print("Fin del giro")