import RPi.GPIO as GPIO

import time

#TODO
#implement method to work with 6 steppermotors that can rotate at the same time if possible (think top \n
#and bottom rotation vs top and left rotation)

#setup some physical system that will allow 6 motors to be run from 4 pins and a data cable for scheduling \n
#what motors to turn at a specific time (scheduler)

#find more adequete, higher current, 5v power supply and regulate
class MotorControl(object):
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.MotorControlPins = [[8,9,7,0], [0,2,3,12], [13,14,21,22], [23,24,25,15], [16,1,4,5], [6,10,11,26]]
		self.ControlPins = [5,6,13,19]
		seq = [ [1,0,0,0],
				[1,1,0,0],
				[0,1,0,0],
				[0,1,1,0],
				[0,0,1,0],
				[0,0,1,1],
				[0,0,0,1],
				[1,0,0,1]
		]
		self.SetupGPIOPins()

	def MoveMotorsForPictures(self):
		pass

	def SetupGPIOPins(self):
		for motor in self.MotorControlPins:
			for pin in motor:
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin,0)

	def Rotate90(self, MotorID, Direction):
		"""CW is clockwise, CCW is counter clockwise, will rotate motor depending on Direction"""
		if Direction == "CW":
			for i in range(128):
				for halfstep in range(8):
					for pin in range(4):
						GPIO.output(self.MotorControlPins[MotorID][pin], self.seq[halfstep][pin])
					time.sleep(0.001)
		elif Direction == "CCW":
			for i in range(128):
				for halfstep in reversed(range(8)):
					for pin in range(4):
						GPIO.output(self.MotorControlPins[MotorID][pin], self.seq[halfstep][pin])
					time.sleep(0.001)

def main():
	motors = MotorControl = []

	motors.rotate90(0, "CW")
	motors.rotate90(0, "CCW")


if __name__ == '__main__':
	main()
	GPIO.cleanup()