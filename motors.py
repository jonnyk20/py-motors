from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

motors = {
  "dc1": mh.getMotor(1),
  "dc2": mh.getMotor(2),
  "dc3": mh.getMotor(3),
  "dc4": mh.getMotor(4)
}

def forward(motorId, speed=255)
  motor = motors[motorId]
  motor.setSpeed(speed)
  motor.run(Adafruit_MotorHAT.FORWARD)

def backward(motorId, speed=255)
  motor = motors[motorId]
  motor.setSpeed(speed)
  motor.run(Adafruit_MotorHAT.BACKWARD)

def stop(motorId)
  motor = motors[motorId]
  motor.setSpeed(0)
  motor.run(Adafruit_MotorHAT.RELEASE)


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	motors["dc1"].run(Adafruit_MotorHAT.RELEASE)
	motors["dc2"].run(Adafruit_MotorHAT.RELEASE)
	motors["dc3"].run(Adafruit_MotorHAT.RELEASE)
	motors["dc4"].run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

# while (True):
# 	print "Forward! "
# 	myMotor.run(Adafruit_MotorHAT.FORWARD)
 
# 	print "\tSpeed up..."
# 	for i in range(255):
# 		myMotor.setSpeed(i)
# 		time.sleep(0.01)
 
# 	print "\tSlow down..."
# 	for i in reversed(range(255)):
# 		myMotor.setSpeed(i)
# 		time.sleep(0.01)
 
# 	print "Backward! "
# 	myMotor.run(Adafruit_MotorHAT.BACKWARD)
 
# 	print "\tSpeed up..."
# 	for i in range(255):
# 		myMotor.setSpeed(i)
# 		time.sleep(0.01)
 
# 	print "\tSlow down..."
# 	for i in reversed(range(255)):
# 		myMotor.setSpeed(i)
# 		time.sleep(0.01)
 
# 	print "Release"
# 	myMotor.run(Adafruit_MotorHAT.RELEASE)
# 	time.sleep(1.0)