class cliCube():
	"""Creates a cli representation of a rubik's cube"""

	def __init__(self):
		"""initiate a 6x9 array of values"""
		self.arrayOfValues = [
		9*['yellow'],
		9*['orange'],
		9*['green'],
		9*['blue'], 
		9*['white'],
		9*['red']
		]

	def __str__(self):
		"""prints a formatted perspective of arrayOfValues for clarity"""
		#bworgy
		#                       '#' '#' '#'
		#                       '#' 'y' '#'1 Top
		#                       '#' '#' '#'

		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'
		#   '#' 'g' '#'3 Left   '#' 'o' '#'2Front   '#' 'b' '#'4 Right
		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'

		#                       '#' '#' '#'
		#                       '#' 'w' '#'5 Bottom
		#                       '#' '#' '#'

		#                       '#' '#' '#'
		#                       '#' 'r' '#'6 Back
		#                       '#' '#' '#'
		#Top = T
		#Left = L
		#Right = R
		#Front = F
		#Bottom = B
		#Back = Ba

		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[0][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[0][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[0][6:9]))
		print("")
		print("{}{:>10}{:>10}".format(*self.arrayOfValues[2][:3]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[1][:3]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[3][:3]))
		print("{}{:>11}{:>10}".format(*self.arrayOfValues[2][3:10]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[1][3:10]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[3][3:10]))
		print("{}{:>10}{:>10}".format(*self.arrayOfValues[2][6:9]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[1][6:9]), "{:>10}{:>10}{:>10}".format(*self.arrayOfValues[3][6:9]))
		print("")
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[4][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[4][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[4][6:9]))
		print("")
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[5][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[5][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.arrayOfValues[5][6:9]))

	def __repr__(self):
		"""prints settings of cube to be created"""
		print(self.arrayOfValues)
		print(self.vertices)
		print(self.edges)
		print(self.surfaces)
		print(self.colors)

	def rotateTop(self, face, dir):
		"""rotate the top layer"""
		index = 0
		if dir == 'CW':

			self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
			self.arrayOfValues[5][8], self.arrayOfValues[5][7], self.arrayOfValues[5][6], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6] = \
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
			self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
			self.arrayOfValues[5][8], self.arrayOfValues[5][7], self.arrayOfValues[5][6], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

		elif dir == 'CCW':
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
			self.arrayOfValues[2][2], self.arrayOfValues[2][1], self.arrayOfValues[2][0], \
			self.arrayOfValues[5][8], self.arrayOfValues[5][7], self.arrayOfValues[5][6], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2] = \
			self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
			self.arrayOfValues[5][6], self.arrayOfValues[5][7], self.arrayOfValues[5][8], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

	def rotateFront(self, face, dir):
		"""rotate the front layer"""
		index = 1
		if dir == 'CW':
			self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
			self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8], \
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6] = \
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8], \
			self.arrayOfValues[3][6], self.arrayOfValues[3][3], self.arrayOfValues[3][0], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
			self.arrayOfValues[2][8], self.arrayOfValues[2][5], self.arrayOfValues[2][2], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8] 

		elif dir == 'CCW':
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8], \
			self.arrayOfValues[3][6], self.arrayOfValues[3][3], self.arrayOfValues[3][0], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
			self.arrayOfValues[2][8], self.arrayOfValues[2][5], self.arrayOfValues[2][2], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2] = \
			self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
			self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8], \
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8] 
			
	def rotateLeft(self, face, dir):
		"""rotate the left layer"""
		index = 2
		if dir == 'CW':
			self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
			self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
			self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6] = \
			self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6], \
			self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
			self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

		elif dir == 'CCW':
			self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6], \
			self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
			self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2] = \
			self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
			self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
			self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]
			
	def rotateRight(self, face, dir):
		"""rotate the right layer"""
		index = 3
		if dir == 'CW':
			self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
			self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
			self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8], \
			self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6] = \
			self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
			self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
			self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
			self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

		elif dir == 'CCW':
			self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
			self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
			self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
			self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2] = \
			self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
			self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
			self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8], \
			self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

	def rotateBottom(self, face, dir):
		"""rotate the bottom layer"""
		index = 4
		if dir == 'CCW':
			self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8], \
			self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8], \
			self.arrayOfValues[5][2], self.arrayOfValues[5][1], self.arrayOfValues[5][0], \
			self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8] = \
			self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8],\
			self.arrayOfValues[5][2], self.arrayOfValues[5][1], self.arrayOfValues[5][0],\
			self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8],\
			self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6]


		elif dir == 'CW':
			self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8], \
			self.arrayOfValues[5][2], self.arrayOfValues[5][1], self.arrayOfValues[5][0], \
			self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8], \
			self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8] = \
			self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8], \
			self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8], \
			self.arrayOfValues[5][2], self.arrayOfValues[5][1], self.arrayOfValues[5][0], \
			self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2]

	def rotateBack(self, face, dir):
		"""rotate the back layer"""
		index = 5
		if dir == 'CW':
			self.arrayOfValues[2][6], self.arrayOfValues[2][3], self.arrayOfValues[2][0], \
			self.arrayOfValues[4][8], self.arrayOfValues[4][7], self.arrayOfValues[4][6], \
			self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
			self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2], \
			self.arrayOfValues[index][2], self.arrayOfValues[index][5], self.arrayOfValues[index][8], \
			self.arrayOfValues[index][1], self.arrayOfValues[index][4], self.arrayOfValues[index][7], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][3], self.arrayOfValues[index][6] = \
			self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2], \
			self.arrayOfValues[2][6], self.arrayOfValues[2][3], self.arrayOfValues[2][0], \
			self.arrayOfValues[4][8], self.arrayOfValues[4][7], self.arrayOfValues[4][6], \
			self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]

		elif dir == 'CCW':
			self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2], \
			self.arrayOfValues[2][6], self.arrayOfValues[2][3], self.arrayOfValues[2][0], \
			self.arrayOfValues[4][8], self.arrayOfValues[4][7], self.arrayOfValues[4][6], \
			self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][3], self.arrayOfValues[index][0], \
			self.arrayOfValues[index][7], self.arrayOfValues[index][4], self.arrayOfValues[index][1], \
			self.arrayOfValues[index][8], self.arrayOfValues[index][5], self.arrayOfValues[index][2] = \
			self.arrayOfValues[2][6], self.arrayOfValues[2][3], self.arrayOfValues[2][0], \
			self.arrayOfValues[4][8], self.arrayOfValues[4][7], self.arrayOfValues[4][6], \
			self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
			self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2], \
			self.arrayOfValues[index][0], self.arrayOfValues[index][1], self.arrayOfValues[index][2], \
			self.arrayOfValues[index][3], self.arrayOfValues[index][4], self.arrayOfValues[index][5], \
			self.arrayOfValues[index][6], self.arrayOfValues[index][7], self.arrayOfValues[index][8]
		
	def rotateLayer(self, move):
		"""rotate the any layer based on format of move"""
		if move[0:2] == "Ba":
			face = "Ba"
			direction = move[2:]
		else:
			face = move[0]
			direction = move[1:]
			
		if face == 'T': #Top
			self.rotateTop(face, direction)
		elif face == 'F': #Front
			self.rotateFront(face, direction)
		elif face == 'L': #Left
			self.rotateLeft(face, direction)
		elif face == 'R': #Right
			self.rotateRight(face, direction)
		elif face == 'B': #Bottom
			self.rotateBottom(face, direction)
		elif face == 'Ba': #Back
			self.rotateBack(face, direction)
		else:
			print('ERROR! Unknown face name: input = "T", "F", "B", "Ba", "L", "R"')
			return