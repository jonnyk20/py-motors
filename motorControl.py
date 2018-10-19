import os
isPy = os.environ.get('RASPBERRY_PI', False)

if (isPy):
    from motors import move
else:
    from fakeMotors import move

def moveDirection(req, time=1):
    direction = req["direction"]
    print("Moving: " + direction)
    move(direction)
    print("Finished Moving")
