from robot import Robot, constants

#TODO: make this normal because its cancer right now
def align(drive_speed, align_speed):
  threshold = 5
  target = constants["black"] + threshold

  left_value, right_value = _read_sensors()

  if(not (right_value <= target or left_value <= target)):
  Robot.chassis.drive(drive_speed, 0)
  while(not (right_value <= target or left_value <= target)):
    right_value, left_value = _read_sensors()
  Robot.brake()

  if(not (right_value <= target and left_value <= target)):
    if(right_value <= target):
      Robot.wheel_left.run(align_speed)
    elif(left_value <= target):
      Robot.wheel_right.run(align_speed)
    while(not (right_value <= target and left_value <= target)):
      right_value, left_value = _read_sensors()

  Robot.brake()

def _read_sensors():
    right_value = Robot.color_right.reflection()
    left_value = Robot.color_left.reflection()
    return (left_value, right_value)
