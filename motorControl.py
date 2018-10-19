from time import sleep
import os
isPy = os.environ.get('RASPBERRY_PI', False)

if (isPy):
    from motors import forward, stop
else:
    from fakeMotors import forward, stop

directions = {
    "forward": "dc1",
    "backward": "dc2",
    "left": "dc3",
    "right": "dc4",
    "up": "stepper-reverse",
    "down": "stepper-reverse"
}


def moveDirection(req, time=1):
    direction = req["direction"]
    print("Moving: " + direction)
    forward(directions[direction])
    sleep(time)
    print("Finished Moving")
    stop(directions[direction])


def toggleMotor(req):
    motorId = req["motorId"]
    print(motorId)
