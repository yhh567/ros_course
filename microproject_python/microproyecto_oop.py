from robot_control_class import RobotControl

class RoboMov:
    def __init__(self) -> None:
        self.rc = RobotControl()

    def en_movimiento_con_parada(self):
        print("Recibido, en movimiento")
        self.sentido_mov = input("Sentido del movimiento <<forward/backward>>: ")
        self.vel_mov = float(input("Velocidad de movimiento: "))
        self.tiempo_mov = int(input("Tiempo en movimiento: "))
        self.rc.move_straight_time(self.sentido_mov, self.vel_mov, self.tiempo_mov)

    def girando(self):
        print("Recibido, rotando")
        self.angulo = int(input("Angulo de giro: "))
        self.rc.rotate(self.angulo)
    
    def escaneo(self):
        return self.rc.get_laser(360)

    def en_movimiento(self):
        print("En movimiento")
        self.rc.move_straight()
    
    def parar(self):
        print("Parando")
        self.rc.stop_robot()
