from robot_control_class import RobotControl

class ExamControl:
    def __init__(self) -> None:
        self.rc = RobotControl()

    def get_laser_readings(self):
        return self.rc.get_laser(719), self.rc.get_laser(0)

    def main(self):
        self.rc.move_straight()

        left, right = self.get_laser_readings()

        while left != float('inf') or right != float('inf'):
            left, right = self.get_laser_readings() # Actualizar
            self.rc.move_straight()

        self.rc.stop_robot()