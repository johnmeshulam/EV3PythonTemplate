#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Button
from util import buttons
from robot import Robot
from runs import drive_run, align_run, line_follow_run, light_reset_run

def display_menu():
  Robot.brick.screen.clear()

  Robot.brick.screen.print(" ^ " + drive_run.name)
  Robot.brick.screen.print(" > " + align_run.name)
  Robot.brick.screen.print(" v " + line_follow_run.name)
  Robot.brick.screen.print(" < " + light_reset_run.name)
  #Robot.brick.screen.print("[] " + _run.name)

#TODO: for higher level - think about using a run class
#       or adding a method that takes a start method and clears screen before starting it
while True:
  display_menu()

  btn = buttons.wait_for_any_press()

  Robot.brick.screen.clear()

  if(btn==Button.UP):
    drive_run.start()
    pass
  elif(btn==Button.RIGHT):
    align_run.start()
    pass
  elif(btn==Button.DOWN):
    line_follow_run.start()
    pass
  elif(btn==Button.LEFT):
    light_reset_run.start()
    pass
  elif(btn==Button.CENTER):
    #_run.start()
    pass

    



