import os
isPy = os.environ.get('RASPBERRY_PI', 'False')
print('isPy:')
print(isPy)

if (isPy == 'True'):
    from motors import move
else:
    from fakeMotors import move


def moveDirection(req, time=1):
    direction = req["direction"]
    print("Moving: " + direction)
    move(direction)
    print("Finished Moving")
