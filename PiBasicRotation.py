# import RPi.GPIO as GPIO

import time

#TODO
#finished Just need to implement phyically

class IODevices(object):
	def __init__(self):
		# GPIO.setmode(GPIO.BCM)
		# self.MotorControlPins = [[8,9,7,0], [0,2,3,12], [13,14,21,22], [23,24,25,15], [16,1,4,5], [6,10,11,26]]
		self.MotorControlPins = [[2,3,4,17], [27,22,10,9], [11,5,6,13], [14,15,18,23], [24,25,8,7], [12,16,20,21]]
		########################  Front       bottom         Right         Back          Top           Left
		# self.ControlPins = [5,6,13,19]
		self.seq = [ [1,0,0,0],
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
		print('setup GPIO Pins')
		"""uncomment when using a raspberry pi"""
		# for motor in self.MotorControlPins:
		# 	for pin in motor:
		# 		GPIO.setup(pin, GPIO.OUT)
		# 		GPIO.output(pin,0)
		# for switch in self.ControlPins:
			# GPIO.setup(switch, GPIO.IN)


	def OrganiseMotorInput(self, inputString):
		"""CW is clockwise, CCW is counter clockwise, will rotate motor depending on Direction"""
		if inputString == "1":
			MotorID = 5
			Direction = "CW"
			print("LCW")
		# elif inputString == "2":
		# 	print("MCW")
		elif inputString == "3":
			MotorID = 2
			Direction = "CCW"
			print("RCCW")
		elif inputString == "f1":
			MotorID = 5
			Direction = "CCW"
			print("LCCW")
		# elif inputString == "w":
		# 	print("MCCW")
		elif inputString == "f3":
			MotorID = 2
			Direction = "CW"
			print("RCW")

		elif inputString == "4":
			MotorID = 1
			Direction = "CW"
			print("BCW")
		# elif inputString == "5":
		# 	print("MCW")
		elif inputString == "6":
			MotorID = 4
			Direction = "CCW"
			print("TCCW")
		elif inputString == "f4":
			MotorID = 1
			Direction = "CCW"
			print("BCCW")
		# elif inputString == "t":
		# 	print("MCCW")
		elif inputString == "f6":
			MotorID = 4
			Direction = "CW"
			print("TCW")

		elif inputString == "7":
			MotorID = 3
			Direction = "CW"
			print("BACW")
		# elif inputString == "8":
		# 	print("MCW")
		elif inputString == "9":
			MotorID = 0
			Direction = "CCW"
			print("FCCW")
		elif inputString == "f7":
			MotorID = 3
			Direction = "CCW"
			print("BACCW")
		# elif inputString == "i":
		# 	print("MCCW")
		elif inputString == "f9":
			MotorID = 0
			Direction = "CW"
			print("FCW")
		self.Rotate90(MotorID, Direction)

	def solveButton(self):
		"""implement physical button for inserting solve sequence into
			move sequence in Solve.py"""
		if GPIO.input(self.solvePin):
			return True

	def scrambleButton(self):
		"""implement physical button for inserting scramble sequence into
			move sequence in Solve.py"""

		if GPIO.input(self.scramblePin):
			return True

	def manualButton(self, buttonPin):
		"""implement physical buttons for inserting manual sequence into
			move sequence in Solve.py"""
		recordButtonPin = buttonPin
		for pin in self.ControlPins:
			if GPIO.input(pin):
				
				pushedPin = pin
				buttonTime = time.time()
				return pin

	def Rotate90(self, MotorID, Direction):
		"""rotate nema17 stepper motors 90 degrees depending on the motor
		id and direction"""

		#Note: Will need testing to ensure accurate 90 turns 100% of the 
		#time
		# Will need adjusting with the rotation rate of opengl implementation
		# to ensure sync is good (also needs to adjust for fastest and most
		#accurate )

		print("rotated ", MotorID, " 90 degrees ", Direction)
		# if Direction == "CW":
		# 	for i in range(128):
		# 		for halfstep in range(8):
		# 			for pin in range(4):
		# 				GPIO.output(self.MotorControlPins[MotorID][pin], self.seq[halfstep][pin])
		# 			time.sleep(0.001)
		# elif Direction == "CCW":
		# 	for i in range(128):
		# 		for halfstep in reversed(range(8)):
		# 			for pin in range(4):
		# 				GPIO.output(self.MotorControlPins[MotorID][pin], self.seq[halfstep][pin])
		# 			time.sleep(0.001)

		# GPIO.cleanup()#maybe?


# def main():
# 	motors = MotorControl()

# 	motors.rotate90(0, "CW")
# 	motors.rotate90(0, "CCW")


# if __name__ == '__main__':
# 	main()
# 	GPIO.cleanup()