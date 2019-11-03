import cliCube
import random
import time

class Algorithms():
	def __init__(self, board):
		self.moveCount = 0
		self.ScrambleToggle = 0
		self.solving = False
		self.FirstAlgorithm = ["RCCW", "BCCW", "RCW", "BCW"]

		self.SecondLayerAlgorithmLeft = ["TCW", "RCW", "TCCW", "RCCW", "TCCW", "FCCW", "TCW", "FCW"]

		self.SecondLayerAlgorithmRight = ["TCCW",  "LCCW", "TCW", "LCW", "TCW", "FCW", "TCCW", "FCCW"]

		self.TopCrossAlgorithm = ["FCW", "RCW", "TCW", "RCCW", "TCCW", "FCCW"]

		self.ThirdLayerAlgorithm = ["RCW", "TCW", "RCCW", "TCW", "RCW", "TCW", "TCW", "TCCW", "TCW"]

		# self.ThirdLayerCornersAlgorithm = ["RCW", "TCCW", "LCCW", "TCW", "RCCW", "TCCW", "LCW", "TCW"]

		# self.items = ["BCCW","RCCW"]
		# self.items = ["BCW","RCW"]
		# self.items = ["TCCW", "FCW", "RCW", "LCW", "FCW", "RCW", "FCW", "RCCW", "BCCW", "TCCW"]

		# self.items = *self.FirstAlgorithm[::-1]
		self.items = []

		# print(cli.board)

	def Scramble(self):
		"""Append to self.items 1 random moves, corresponds to right click mouse button"""
		for _ in range(1):
			moveToAppend = ""
			CW_CCW = random.randrange(2)
			face = random.randrange(6)
			if face == 0:
				moveToAppend += "F"
			elif face == 1:
				moveToAppend += "L"
			elif face == 2:
				moveToAppend += "R"
			elif face == 3:
				moveToAppend += "Ba"
			elif face == 4:
				moveToAppend += "T"
			elif face == 5:
				moveToAppend += "B"
			if CW_CCW == 0:
				moveToAppend += "CW"
			elif CW_CCW == 1:
				moveToAppend += "CCW"
			self.items.insert(0, moveToAppend)
			self.cli.rotateLayer(moveToAppend)

	def Solve(self):
		self.solving = True
		print("Solving")
		self.solveWhiteCross()

		self.solveWhiteSide()

		self.solveSecondLayer()

	def rotateCliGui(self, move):
		self.items.insert(0,move)

	def moveToYellowFace(self, curWhitePositions, solvedWhitePositions, solvedColouredPositions):
		totalMoves = 0
		while not all(self.cli.arrayOfValues[v[0]][v[1]] == "white" for v in solvedWhitePositions) and totalMoves < 10:
			"""if all positions are initially not in place"""
			totalMoves += 1
			"""set self.cli.arrayOfValues to a simpler name"""
			print("called")
			for whiteEdge in curWhitePositions:
				if whiteEdge[0] != 0:
					#if the element is not on yellow side
					if whiteEdge[0] == 4:
						#if the element is on the white side
						if self.cli.arrayOfValues[0][7] == "white":
							#while the yellowside has a piece in the 7th index rotate until it is not white
							
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						elif self.cli.arrayOfValues[4][1] != "white":
							#while edge piece on white side is not in position, rotate
							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")
							curWhitePositions = self.findWhiteEdges()
						else:
							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							curWhitePositions = self.findWhiteEdges()
					elif whiteEdge[0] == 1:
						#On the front side
						if self.cli.arrayOfValues[0][7] == "white":
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						if whiteEdge[1] == 1:
							"""https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step-1-first-layer-edges/							
							"FCW"
							"TCCW"
							"RCW"
							"TCW"	"""
							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("TCCW")
							self.items.insert(0, "TCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 3:
							"""L B R' F2'"""
							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")

							self.cli.rotateLayer("LCCW")
							self.items.insert(0, "LCCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 5:
							#R' D' R F2

							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")	

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")	
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 7:
							"""F' R' D' R F2"""
							self.cli.rotateLayer("FCCW")
							self.items.insert(0, "FCCW")

							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")
							curWhitePositions = self.findWhiteEdges()

					#happy
					elif whiteEdge[0] == 2:
						#on left side
						if self.cli.arrayOfValues[0][3] == "white":
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						if whiteEdge[1] == 1:
							"""https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step-1-first-layer-edges/							
							"FCW"
							"TCCW"
							"RCW"
							"TCW"	"""
							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("TCCW")
							self.items.insert(0, "TCCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
						#happy
						elif whiteEdge[1] == 3:
							"""R' D' R F2'"""
							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")

							self.cli.rotateLayer("BaCCW")
							self.items.insert(0, "BaCCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")
						#happy

						elif whiteEdge[1] == 5:

							self.cli.rotateLayer("FCCW")
							self.items.insert(0, "FCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")	

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")	
						#happy

						elif whiteEdge[1] == 7:
							"""R' D' R F2'"""
							self.cli.rotateLayer("LCCW")
							self.items.insert(0, "LCCW")

							self.cli.rotateLayer("FCCW")
							self.items.insert(0, "FCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")
						#happy

					elif whiteEdge[0] == 3:
						#On the right side
						if self.cli.arrayOfValues[0][5] == "white":
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						if whiteEdge[1] == 1:
							"""https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step-1-first-layer-edges/							
							"FCW"
							"TCCW"
							"RCW"
							"TCW"	"""
							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("TCCW")
							self.items.insert(0, "TCCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 3:
							"""L B R' F2'"""
							self.cli.rotateLayer("FCW")
							self.items.insert(0, "FCW")

							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")

							self.cli.rotateLayer("FCCW")
							self.items.insert(0, "FCCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 5:
							#R' D' R F2

							self.cli.rotateLayer("BaCCW")
							self.items.insert(0, "BaCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")	

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")	
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 7:
							"""F' R' D' R F2"""
							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BaCCW")
							self.items.insert(0, "BaCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")
							curWhitePositions = self.findWhiteEdges()

					elif whiteEdge[0] == 5:
						#On the back side
						if self.cli.arrayOfValues[0][1] == "white":
							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
						if whiteEdge[1] == 1:
							"""https://ruwix.com/the-rubiks-cube/how-to-solve-the-rubiks-cube-beginners-method/step-1-first-layer-edges/							
							"FCW"
							"TCCW"
							"RCW"
							"TCW"	"""
							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("TCCW")
							self.items.insert(0, "TCCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("TCW")
							self.items.insert(0, "TCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 5:
							"""L B R' F2'"""
							self.cli.rotateLayer("RCW")
							self.items.insert(0, "RCW")

							self.cli.rotateLayer("BCW")
							self.items.insert(0, "BCW")

							self.cli.rotateLayer("RCCW")
							self.items.insert(0, "RCCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 2:
							#R' D' R F2

							self.cli.rotateLayer("LCCW")
							self.items.insert(0, "LCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")	

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")	
							curWhitePositions = self.findWhiteEdges()
							#happy

						elif whiteEdge[1] == 7:
							"""F' R' D' R F2"""
							self.cli.rotateLayer("BaCCW")
							self.items.insert(0, "BaCCW")

							self.cli.rotateLayer("LCCW")
							self.items.insert(0, "LCCW")

							self.cli.rotateLayer("BCCW")
							self.items.insert(0, "BCCW")

							self.cli.rotateLayer("LCW")
							self.items.insert(0, "LCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")

							self.cli.rotateLayer("BaCW")
							self.items.insert(0, "BaCW")
							curWhitePositions = self.findWhiteEdges()

	def solveWhiteCross(self):
		curWhitePositions = self.findWhiteEdges()
		solvedWhitePositions = [(4, 1), (4, 3), (4, 5), (4, 7)]
		solvedColouredPositions = [(1, 7),(2, 7), (3, 7), (5, 1)]

		
		self.moveToYellowFace(curWhitePositions, solvedWhitePositions, solvedColouredPositions)
		# print(self.cli.arrayOfValues)
		print("Got here!")
		while not self.cli.arrayOfValues[4][4] == self.cli.arrayOfValues[4][1] == self.cli.arrayOfValues[4][3] == self.cli.arrayOfValues[4][5] == self.cli.arrayOfValues[4][7]:
			for whiteEdge in curWhitePositions:
				"""front:orange
				left:green
				right:blue
				top:yellow
				bot:white
				back:red"""

				if self.cli.arrayOfValues[1][1] == self.cli.arrayOfValues[1][4]:
					self.cli.rotateLayer("FCW")
					self.items.insert(0, "FCW")

					self.cli.rotateLayer("FCW")
					self.items.insert(0, "FCW")
					curWhitePositions = self.findWhiteEdges()

				if self.cli.arrayOfValues[2][1] == self.cli.arrayOfValues[2][4]:
					self.cli.rotateLayer("LCW")
					self.items.insert(0, "LCW")

					self.cli.rotateLayer("LCW")
					self.items.insert(0, "LCW")	
					curWhitePositions = self.findWhiteEdges()

				if self.cli.arrayOfValues[3][1] == self.cli.arrayOfValues[3][4]:
					self.cli.rotateLayer("RCW")
					self.items.insert(0, "RCW")

					self.cli.rotateLayer("RCW")
					self.items.insert(0, "RCW")	
					curWhitePositions = self.findWhiteEdges()

				if self.cli.arrayOfValues[5][7] == self.cli.arrayOfValues[5][4]:
					self.cli.rotateLayer("BaCW")
					self.items.insert(0, "BaCW")

					self.cli.rotateLayer("BaCW")
					self.items.insert(0, "BaCW")	
					curWhitePositions = self.findWhiteEdges()
				self.cli.rotateLayer("TCW")
				self.items.insert(0, "TCW")
				curWhitePositions = self.findWhiteEdges()


		print("Solved White Cross!")


	def findWhiteEdges(self):
		curWhitePositions = []
		for indSide, side in enumerate(self.board):
			for edge in range(1, len(side), 2):
				if side[edge] == "white":
					curWhitePositions.append((indSide, edge),)
		return curWhitePositions

	def solveWhiteSide(self):
		curWhitePositions = self.findWhiteCorners()
		print(curWhitePositions)

		solvedWhitePositions = [(4, 0), (4, 2), (4, 4), (4, 6), (4, 8)] #(4,4) not nessessary
		solvedGreenPositions = [(2, 0), (2, 2)]
		solvedRedPositions = [(5, 0), (5, 2)]
		solvedBluePositions = [(3, 0), (3, 2)]
		solvedOrangePositions = [(1, 0), (1, 2)]

		#for testing purposes
		count = 0
		while not all(x==self.cli.arrayOfValues[4][0] for x in self.cli.arrayOfValues[4]) and count < 25:
			count += 1
			for whiteCorner in curWhitePositions:

				if whiteCorner[0] == 4 and whiteCorner[1] == 0 or whiteCorner[0] == 1 and whiteCorner[1] == 6 or whiteCorner[0] == 2 and whiteCorner[1] == 9:
					"""if whitesquare in the green orange white corner"""
					if self.cli.arrayOfValues[0][6] == "white" or self.cli.arrayOfValues[2][2] == "white" or self.cli.arrayOfValues[1][0] == "white":
						self.cli.rotateLayer("TCW")
						self.items.insert(0, "TCW")
						curWhitePositions = self.findWhiteCorners()
					self.cli.rotateLayer("FCCW")
					self.items.insert(0, "FCCW")
					self.cli.rotateLayer("BCCW")
					self.items.insert(0, "BCCW")
					self.cli.rotateLayer("FCW")
					self.items.insert(0, "FCW")
					self.cli.rotateLayer("BCW")
					self.items.insert(0, "BCW")
					curWhitePositions = self.findWhiteCorners()

				if whiteCorner[0] == 4 and whiteCorner[1] == 2 or whiteCorner[0] == 1 and whiteCorner[1] == 8 or whiteCorner[0] == 3 and whiteCorner[1] == 7:
					if self.cli.arrayOfValues[0][6] == "white" or self.cli.arrayOfValues[2][2] == "white" or self.cli.arrayOfValues[1][0] == "white":
						self.cli.rotateLayer("TCW")
						self.items.insert(0, "TCW")
						curWhitePositions = self.findWhiteCorners()
					self.cli.rotateLayer("RCCW")
					self.items.insert(0, "RCCW")
					self.cli.rotateLayer("BCCW")
					self.items.insert(0, "BCCW")
					self.cli.rotateLayer("RCW")
					self.items.insert(0, "RCW")
					self.cli.rotateLayer("BCW")
					self.items.insert(0, "BCW")
					curWhitePositions = self.findWhiteCorners()

				if whiteCorner[0] == 4 and whiteCorner[1] == 8 or whiteCorner[0] == 3 and whiteCorner[1] == 8 or whiteCorner[0] == 5 and whiteCorner[1] == 2:
					if self.cli.arrayOfValues[0][8] == "white" or self.cli.arrayOfValues[1][2] == "white" or self.cli.arrayOfValues[3][0] == "white":
						self.cli.rotateLayer("TCW")
						self.items.insert(0, "TCW")
						curWhitePositions = self.findWhiteCorners()
					self.cli.rotateLayer("BaCCW")
					self.items.insert(0, "BaCCW")
					self.cli.rotateLayer("BCCW")
					self.items.insert(0, "BCCW")
					self.cli.rotateLayer("BaCW")
					self.items.insert(0, "BaCW")
					self.cli.rotateLayer("BCW")
					self.items.insert(0, "BCW")
					curWhitePositions = self.findWhiteCorners()
					corner = (1, 1, 1)
				
				if whiteCorner[0] == 4 and whiteCorner[1] == 6 or whiteCorner[0] == 2 and whiteCorner[1] == 6 or whiteCorner[0] == 5 and whiteCorner[1] == 0:	
					if self.cli.arrayOfValues[0][8] == "white" or self.cli.arrayOfValues[1][2] == "white" or self.cli.arrayOfValues[3][0] == "white":
						self.cli.rotateLayer("TCW")
						self.items.insert(0, "TCW")
						curWhitePositions = self.findWhiteCorners()
					self.cli.rotateLayer("LCCW")
					self.items.insert(0, "LCCW")
					self.cli.rotateLayer("BCCW")
					self.items.insert(0, "BCCW")
					self.cli.rotateLayer("LCW")
					self.items.insert(0, "LCW")
					self.cli.rotateLayer("BCW")
					self.items.insert(0, "BCW")
					curWhitePositions = self.findWhiteCorners()
					corner = (0, 0, 1)

		print("Solved White Side!")

	def findWhiteCorners(self):
		curWhitePositions = []
		for indSide, side in enumerate(self.board):
			for corner in range(0, len(side), 2):
				if side[corner] == "white":
					curWhitePositions.append((indSide, corner),)
		return curWhitePositions

	def solveSecondLayer(self):
		pass

	# def makeMove(self, move):
		"""instead of calling self.items.insert(0,move) and self.cli.rotateLayer(move)
		do it in one move"""
		# self.cli.rotateLayer(move)
		# self.items.insert(0, move)

class Queue(Algorithms):
	def __init__(self, board):
		Algorithms.__init__(self, board)
		self.board = board

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		# print("Pushed item: ", item)
		self.items.append(item)

	def pop(self):
		# print("Popped item: ", self.items[-1])
		return self.items.pop()

	def peek(self):
		# print("Peeked at item: ", self.items[len(self.items)-1])
		return self.items[len(self.items)-1]

	def size(self):
		# print("size of queue: ", len(self.items))
		return len(self.items)




class Solve():
	def __init__(self, InitSolvedSide):
		self.InitSolvedSide = InitSolvedSide
		self.InitSolvedSide = 'W'	
		self.OppositeInitSolvedSide = InvertInitSolvedSide()

	def FindPositionPiece(self, ColourToFind):
		"""split cubes into grouped blocks and return position and wether it is a middle or corner piece"""
		#return the positions of all ColourToFind
		index = 0
		for face in arrayOfValues:
			yield index, [i for i, e in enumerate([face]) if e == ColourToFind]
			index += 1

	def InvertInitSolvedSide(self, InitSolvedSide):
		#inverts InitSolvedSide
		if self.InitSolvedSide == 'W':
			self.OppositeInitSolvedSide = 'Y'
		elif self.InitSolvedSide == 'Y':
			self.OppositeInitSolvedSide = 'W'

		elif self.InitSolvedSide == 'R':
			self.OppositeInitSolvedSide = 'O'
		elif self.InitSolvedSide == 'O':
			self.OppositeInitSolvedSide = 'R'
		
		elif self.InitSolvedSide == 'B':
			self.OppositeInitSolvedSide = 'G'
		elif self.InitSolvedSide == 'G':
			self.OppositeInitSolvedSide = 'B'
		else:
			print("Invalid input")
		return self.OppositeInitSolvedSide

	def SolveInitCross(self):
		#find InitSolvedSide and solve cross
		self.InvertInitSolvedSide(self.InitSolvedSide)

		while self.FindPositionPiece(InitSolvedSide):
			if CheckMiddle(self.FindPositionPiece):
				if self.FindPositionPiece(InitSolvedSide) == self.InitSolvedSide:
					#match piece to center piece
					Cube.Rotate()
			elif CheckCorner(self.FindPositionPiece):
				pass

	def SolveInitSide(self):
		pass

	def SecondLayerSolved(self):
		if arrayOfValues[0][3] == arrayOfValues[0][4] == arrayOfValues[0][5]:
			if arrayOfValues[3][1] == arrayOfValues[3][4] == arrayOfValues[3][7]:
				if arrayOfValues[2][1] == arrayOfValues[2][4] == arrayOfValues[2][7]:
					if arrayOfValues[4][3] == arrayOfValues[4][4] == arrayOfValues[4][5]:
						return True
		else:
			return False

	def SolveOpSideCross(self):
		pass

	def SolveThirdLayerMiddle(self):
		pass

	def SortThirdLayerCorners(self):
		pass
