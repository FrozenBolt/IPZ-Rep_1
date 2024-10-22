"""SimpleVechicle controller."""
from controller import Robot,Motor
from camera import CameraWrapper
from keyboardFunctions import getKeys
from robot_steering import steer_robot
#Const
CAMERANAME = "camera"

#motor names in motor must be "wheelX" where x in wheel number
#and on each side there are even or odd numbers

# create the Robot instance.
robot = Robot()

motors:dict[str,list[Motor]]
motors = {"LEFT":[],
          "RIGHT":[]}
krw = 0
for i in range(1,11):
    motor_name =  "wheel" + str(i)
    side = "LEFT" if i%2==1 else "RIGHT"
    motor:Motor
    motor = robot.getDevice(motor_name)
    if motor is not None:
        motors[side].append(motor)

for motor in motors["LEFT"]:
    motor.setPosition(float("inf"))
    motor.setVelocity(0)
    
for motor in motors["RIGHT"]:
    motor.setPosition(float("inf"))
    motor.setVelocity(0)
    
timestep = int(robot.getBasicTimeStep())

#INIT
keyboard = robot.getKeyboard()
keyboard.enable(timestep) #get keyboard values every 10 frames in Simulation

while robot.step(timestep) != -1:
    steer_robot(keyboard,motors_left=motors["LEFT"],motors_right=motors["RIGHT"])

    pass

