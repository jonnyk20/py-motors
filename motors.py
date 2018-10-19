from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO
 
import time import sleep
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

dcMotors = {
  "dc1": mh.getMotor(1),
  "dc2": mh.getMotor(2),
  "dc3": mh.getMotor(3),
  "dc4": mh.getMotor(4)
}

movements = {
  "forward": ["runDC", "dc1"],
  "backward": ["runDC", "dc2"],
  "left": ["runDC", "dc3"],
  "right": ["runDC", "dc4"],
  "down": ["runStepper", "cw"],
  "up": ["runStepper", "ccw"]
}

def runDC(motorId, time = 1):
  print("running dc motor")
  motor = dcMotors[motorId]
  motor.setSpeed(255)
  sleep(time)
  print("stopping dc motor")
  motor.setSpeed(0)
  motor.run(Adafruit_MotorHAT.RELEASE)

def stepper(direction):
  print(direction)

motorFunctions = {
  "runDC": runDC,
  "stepper": stepper
}

def move(movement):
  movement = movements[movement]
  motorFunction = motorFunctions[movement[0]]
  directionDetail = movement[1]
  motorFunction(directionDetail)

GPIO.setmode(GPIO.BOARD)
control_pins = [7,11,13,15]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
      GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
    time.sleep(0.001)
GPIO.cleanup()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	dcMotors["dc1"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc2"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc3"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc4"].run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

