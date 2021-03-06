import cliCube
import random
import time

from rubik_solver import utils

#debugging
import pdb

class Algorithms():
	def __init__(self, board):
		self.moveCount = 0
		self.ScrambleToggle = 0

		"""note that these algorithms are not in use, instead
		using a temporary solving library created by 'Victor Cabezas'"""

		# self.FirstAlgorithm = ["RCCW", "BCCW", "RCW", "BCW"]

		# self.SecondLayerAlgorithmLeft = ["TCW", "RCW", "TCCW", "RCCW", "TCCW", "FCCW", "TCW", "FCW"]

		# self.SecondLayerAlgorithmRight = ["TCCW",  "LCCW", "TCW", "LCW", "TCW", "FCW", "TCCW", "FCCW"]

		# self.TopCrossAlgorithm = ["FCW", "RCW", "TCW", "RCCW", "TCCW", "FCCW"]

		# self.ThirdLayerAlgorithm = ["RCW", "TCW", "RCCW", "TCW", "RCW", "TCW", "TCW", "TCCW", "TCW"]

		self.moveSequence = []

	def Scramble(self):
		"""Append to self.moveSequence 1 random moves, corresponds to right click mouse button"""
		# for _ in range(1):
		addMove = ""
		CW_CCW = random.randrange(2) #add a random direction
		face = random.randrange(6) #add a random face
		#Face
		if face == 0:
			addMove += "F"
		elif face == 1:
			addMove += "L"
		elif face == 2:
			addMove += "R"
		elif face == 3:
			addMove += "Ba"
		elif face == 4:
			addMove += "T"
		elif face == 5:
			addMove += "B"

		#Direction
		if CW_CCW == 0:
			addMove += "CW"
		elif CW_CCW == 1:
			addMove += "CCW"
		self.moveSequence.insert(0, addMove)
		self.cli.rotateLayer(addMove)

	def Solve(self):
		"""Call library to append solve sequence to move sequence, temporary"""
		#Note:
		#problem where gui lags when processing the cli to append solve sequence,
		#may need to implement a seperate thread? multiprocessing may help here?


		print("Solving")
		cube = ""
		#This is a bit gross...
		array = [self.cli.state[5][8], self.cli.state[5][7], self.cli.state[5][6], self.cli.state[5][5], self.cli.state[5][4], self.cli.state[5][3], self.cli.state[5][2], self.cli.state[5][1], self.cli.state[5][0]]
		adjustedstate = [self.cli.state[0], self.cli.state[3], array, self.cli.state[2], self.cli.state[1], self.cli.state[4]]
		state = [y for x in self.cli.state for y in x]
		for face in state:
			cube += face[0]

		print("Solve sequence is: ")

		print(utils.solve(cube, 'Kociemba'))

		for move in utils.solve(cube, 'Kociemba'):
			self.convert(str(move))

		print("Solved!")
		print("total moves to solve: ", self.moveCount)

	def convert(self, item):
		"""To append the right syntax of moves generated by utils.solve"""
		if "2" in item:
			item = item[0]
			self.convert(item)
			self.convert(item)
		elif item == "U":
			self.move("TCW")
		elif item == "U'":
			self.move("TCCW")
		elif item == "L":
			self.move("LCW")
		elif item == "L'":
			self.move("LCCW")
		elif item == "R":
			self.move("RCW")
		elif item == "R'":
			self.move("RCCW")
		elif item == "D":
			self.move("BCW")
		elif item == "D'":
			self.move("BCCW")
		elif item == "F":
			self.move("FCW")
		elif item == "F'":
			self.move("FCCW")
		elif item == "B":
			self.move("BaCW")
		elif item == "B'":
			self.move("BaCCW")
		elif item == "M":
			self.move("LCCW")
			self.move("RCW")
		elif item == "M'":
			self.move("LCW")
			self.move("RCCW")
		# elif item == "Y":
		# 	self.move()
		# elif item == "Y'":
		# 	self.move()
		else:
			print("ERROR: item is not processed: ", item)


	def move(self, move):
		self.moveCount += 1
		self.moveSequence.insert(0, move)
		self.cli.rotateLayer(move)

class Queue(Algorithms):
	"""simple Queue implementation to handle the order of moves made,
	This will help when paired with twitch chat"""
	def __init__(self, board):
		Algorithms.__init__(self, board)
		self.board = board

	def isEmpty(self):
		return self.moveSequence == []

	def push(self, item):
		# print("Pushed item: ", item)
		self.moveSequence.append(item)

	def pop(self):
		# print("Popped item: ", self.moveSequence[-1])
		return self.moveSequence.pop()

	def peek(self):
		# print("Peeked at item: ", self.moveSequence[len(self.moveSequence)-1])
		return self.moveSequence[len(self.moveSequence)-1]

	def size(self):
		# print("size of queue: ", len(self.moveSequence))
		return len(self.moveSequence)

