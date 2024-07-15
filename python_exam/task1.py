from robot_control_class import RobotControl

def get_highest_lowest():
    rc = RobotControl()
    l = rc.get_laser_full()
    no_inf = [d for d in l if d != float('inf')]

    return no_inf.index(max(no_inf)), no_inf.index(min(no_inf))