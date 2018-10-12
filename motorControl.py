from time import sleep
from motors import forward, backward, stop

directions = {
  "forward": "dc1",
  "reverse": "dc2",
  "left": "dc3",
  "right": "dc4",
}


def moveDirection(req, time=3):
  direction = req["direction"]
  print("Moving: " + direction)
  forward(directions[direction])
  sleep(time)
  print("Finished Moving")
  stop(directions[direction])

def toggleMotor(req):
  command = req["command"]
  motorId = req["motorId"]
  print(motorId)
