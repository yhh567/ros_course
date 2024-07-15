import time
from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit") # Elegir el robot summit

def en_movimiento():

    en_movimiento = int(input("Introduce los segundos que quieras que el robot este en movimiento: "))

    rc.move_straight() # Movimiento en recto

    time.sleep(en_movimiento) # X segundos despues

    rc.stop_robot() # Parar el robot

en_movimiento()