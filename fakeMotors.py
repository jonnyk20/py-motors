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


dcMotors = {
    "dc1": DCMotor(1),
    "dc2": DCMotor(2),
    "dc3": DCMotor(3),
    "dc4": DCMotor(4)
}

halfstepSequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

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
    "lowerLimit": -5,
    "upperLimit": 5
}

movements = {
    "forward": ["runDC", "dc1"],
    "backward": ["runDC", "dc2"],
    "left": ["runDC", "dc3"],
    "right": ["runDC", "dc4"],
    "down": ["runStepper", "cw"],
    "up": ["runStepper", "ccw"]
}


def runDC(motorId, time=1):
    print("running dc motor")
    motor = dcMotors[motorId]
    motor.setSpeed(255)
    sleep(time)
    print("stopping dc motor")
    motor.setSpeed(0)
    motor.run(Adafruit_MotorHAT_RELEASE)


def runStepper(direction, rotations=3):
    sequence = stepperMotor["halfStepSequence"]
    position = stepperMotor["position"]
    stepCount = len(sequence)
    steps = range(stepCount)
    rotationCount = 0
    up = (direction == "cw")
    positionChange = 1 if up else -1
    if direction == "ccw":
      steps = list(reversed(steps))
    while rotationCount < rotations:
        for step in steps:
          if ((position >= stepperMotor["upperLimit"] and up) or
            (position <= stepperMotor["lowerLimit"] and not up)):
            return
          print(sequence[step])
          sleep(0.1)
        print("1 rotation")
        stepperMotor["position"] += positionChange
        rotationCount += 1


motorFunctions = {
    "runDC": runDC,
    "runStepper": runStepper
}


def move(movement):
    movement = movements[movement]
    motorFunction = motorFunctions[movement[0]]
    directionDetail = movement[1]
    motorFunction(directionDetail)
