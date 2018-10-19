from time import sleep

Adafruit_MotorHAT_FORWARD = 'Adafruit_MotorHAT_FORWARD'
Adafruit_MotorHAT_BACKWARD = 'Adafruit_MotorHAT_BACKWARD'
Adafruit_MotorHAT_RELEASE = 'Adafruit_MotorHAT_RELEASE'

class DCMotor:
  def __init__(self, num):
    self.num = num
    self.speed = 0
    self.rotation = Adafruit_MotorHAT_FORWARD
  def setSpeed(self, speed):
    self.speed = speed
  
  def run(self, direction):
    print("Running " + str(self.num))
    print("Direction " + direction)

motors = {
  "dc1": DCMotor(1),
  "dc2": DCMotor(2),
  "dc3": DCMotor(3),
  "dc4": DCMotor(4)
}

movements = {
  "forward": ["dc", "dc1"],
  "backward": ["dc", "dc2"],
  "left": ["dc", "dc3"],
  "right": ["dc", "dc4"],
  "down": ["stepper", "cw"],
  "up": ["stepper", "ccw"]
}

def dc(motorId, time = 1):
  print("running dcc motor")
  motor = motors[motorId]
  motor.setSpeed(255)
  sleep(time)
  print("stopping dc motor")
  motor.setSpeed(0)
  motor.run(Adafruit_MotorHAT_RELEASE)


def stepper(direction):
  print(direction)

motorFunctions = {
  "dc": dc,
  "stepper": stepper
}

def move(movement):
  movement = movements[movement]
  motorFunction = motorFunctions[movement[0]]
  directionDetail = movement[1]
  motorFunction(directionDetail)
