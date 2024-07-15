from robot_control_class import RobotControl

rc = RobotControl(robot_name="summit")

def obtener_distancias(angulo1: int, angulo2: int, angulo3: int):
    
    d1 = rc.get_laser_summit(angulo1)
    d2 = rc.get_laser_summit(angulo2)
    d3 = rc.get_laser_summit(angulo3)

    return [d1, d2, d3]

distancias = obtener_distancias(0, 360, 719)
print(distancias)

