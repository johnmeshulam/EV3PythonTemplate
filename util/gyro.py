
from robot import Robot

def reset_gyro():
Robot.gyro.reset_angle(0)
Robot.gyro.speed()
Robot.gyro.angle()