import os
isPy = os.environ.get('RASPBERRY_PI', 'False')

if (isPy == 'True'):
    from motors import move
else:
    from fakeMotors import move


def moveDirection(req, time=3):
    direction = req["direction"]
    print("Moving: " + direction)
    move(direction)
    print("Finished Moving")
