from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
 
import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

dcMotors = {
  "dc1": mh.getMotor(1),
  "dc2": mh.getMotor(2),
  "dc3": mh.getMotor(3),
  "dc4": mh.getMotor(4)
}

def forward(motorId, speed=255):
  motor = dcMotors[motorId]
  motor.setSpeed(speed)
  motor.run(Adafruit_MotorHAT.FORWARD)

def backward(motorId, speed=255):
  motor = dcMotors[motorId]
  motor.setSpeed(speed)
  motor.run(Adafruit_MotorHAT.BACKWARD)

def stop(motorId):
  motor = dcMotors[motorId]
  motor.setSpeed(0)
  motor.run(Adafruit_MotorHAT.RELEASE)


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	dcMotors["dc1"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc2"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc3"].run(Adafruit_MotorHAT.RELEASE)
	dcMotors["dc4"].run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)