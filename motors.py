from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

from time import sleep
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

dcMotors = {
  "dc1": mh.getMotor(1),
  "dc2": mh.getMotor(2),
  "dc3": mh.getMotor(3),
  "dc4": mh.getMotor(4)
}

rotationLimit = 99
rotationSteps = 512
stepsPerMovement = rotationSteps // 4
stepLimit = rotationLimit * rotationSteps

stepperMotor = {
    "controlPins": [7, 11, 13, 15],
    "halfStepSequence": [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 0, 0, 1]
    ],
    "position": 0,
    "lowerLimit": stepLimit * -1,
    "upperLimit": stepLimit
}

for pin in stepperMotor["controlPins"]:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

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
  motor.run(Adafruit_MotorHAT.FORWARD)
  sleep(time)
  print("stopping dc motor")
  motor.setSpeed(0)
  motor.run(Adafruit_MotorHAT.RELEASE)

def runStepper(direction, rotations=3):
    sequence = stepperMotor["halfStepSequence"]
    position = stepperMotor["position"]
    controlPins = stepperMotor["controlPins"]
    stepCount = len(sequence)
    steps = range(stepCount)
    rotationCount = 0
    up = (direction == "cw")
    positionChange = 1 if up else -1
    if direction == "ccw":
      steps = list(reversed(steps))
    for i in range(stepsPerMovement):
      for step in steps:
        if ((position >= stepperMotor["upperLimit"] and up) or
          (position <= stepperMotor["lowerLimit"] and not up)):
          return
        for pin in range(4):
          GPIO.output(controlPins[pin], sequence[step][pin])
        sleep(0.001)
      stepperMotor["position"] += positionChange
      rotationCount += 1
    for pin in range(4):
      GPIO.output(controlPins[pin], 0)

motorFunctions = {
  "runDC": runDC,
  "runStepper": runStepper
}

def move(movement):
  movement = movements[movement]
  motorFunction = motorFunctions[movement[0]]
  directionDetail = movement[1]
  motorFunction(directionDetail)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	dcMotors["dc1"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc2"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc3"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc4"].run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

