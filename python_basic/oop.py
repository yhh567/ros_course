from robot_control_class import RobotControl

class RoboMov:
    def __init__(self, sentido_mov, sentido_giro, velocidad, tiempo_mov, tiempo_de_giro) -> None:
        self.sentido_mov = sentido_mov
        self.sentido_giro = sentido_giro
        self.velocidad = velocidad
        self.tiempo_mov = tiempo_mov
        self.tiempo_de_giro = tiempo_de_giro
        self.rc = RobotControl(robot_name='summit')

    def hacer_cuadrados(self):
        i = 0
        while i < 4:
            self.rc.move_straight_time(self.sentido_mov, self.velocidad, self.tiempo_mov)
            self.rc.turn(self.sentido_giro, self.velocidad, self.tiempo_de_giro)
            i += 1

cuadrado1 = RoboMov('forward', 'clockwise', 0.5, 4, 7)
cuadrado1.hacer_cuadrados()
cuadrado2 = RoboMov('forward', 'other', 0.5, 8, 7)
cuadrado2.hacer_cuadrados()