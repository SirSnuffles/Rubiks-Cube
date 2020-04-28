



class cliCube():
	"""Creates a cli representation of a rubik's cube"""

	def __init__(self):
		"""initiate a 6x9 array of values"""
		self.state = [
		9*['yellow'],
		9*['blue'],
		9*['red'],
		9*['green'], 
		9*['orange'],
		9*['white']
		]

	def __str__(self):
		"""prints a formatted perspective of state for clarity"""
		#
		#                       '#' '#' '#'
		#                       '#' 'y' '#'1 Top
		#                       '#' '#' '#'

		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'					'#' '#' '#'
		#   '#' 'b' '#'3 Left   '#' 'r' '#'2Front   '#' 'g' '#'4 Right 			'#' 'o' '#'6 Back
		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'					'#' '#' '#'

		#                       '#' '#' '#'
		#                       '#' 'w' '#'5 Bottom
		#                       '#' '#' '#'
             
		#Top = T
		#Left = L
		#Right = R
		#Front = F
		#Bottom = B
		#Back = Ba

		print("{:>37}{:>10}{:>10}".format(*self.state[0][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.state[0][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.state[0][6:9]))
		print("")
		print("{}{:>10}{:>10}".format(*self.state[2][:3]), "{:>10}{:>10}{:>10}".format(*self.state[1][:3]), "{:>10}{:>10}{:>10}".format(*self.state[3][:3]))
		print("{}{:>11}{:>10}".format(*self.state[2][3:10]), "{:>10}{:>10}{:>10}".format(*self.state[1][3:10]), "{:>10}{:>10}{:>10}".format(*self.state[3][3:10]))
		print("{}{:>10}{:>10}".format(*self.state[2][6:9]), "{:>10}{:>10}{:>10}".format(*self.state[1][6:9]), "{:>10}{:>10}{:>10}".format(*self.state[3][6:9]))
		print("")
		print("{:>37}{:>10}{:>10}".format(*self.state[4][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.state[4][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.state[4][6:9]))
		print("")
		print("{:>37}{:>10}{:>10}".format(*self.state[5][:3]))
		print("{:>37}{:>10}{:>10}".format(*self.state[5][3:10]))
		print("{:>37}{:>10}{:>10}".format(*self.state[5][6:9]))

	def __repr__(self):
		"""prints settings of cube to be created"""
		print(self.state)
		print(self.vertices)
		print(self.edges)
		print(self.surfaces)
		print(self.colors)

	def rotateFace(self, dir, index):
		"""rotate the index of the state given the direction"""
		if dir == "CW":
			self.state[index][2], self.state[index][5], self.state[index][8], \
			self.state[index][1], self.state[index][4], self.state[index][7], \
			self.state[index][0], self.state[index][3], self.state[index][6] = \
			self.state[index][0], self.state[index][1], self.state[index][2], \
			self.state[index][3], self.state[index][4], self.state[index][5], \
			self.state[index][6], self.state[index][7], self.state[index][8]

		elif dir == "CCW":
			self.state[index][6], self.state[index][3], self.state[index][0], \
			self.state[index][7], self.state[index][4], self.state[index][1], \
			self.state[index][8], self.state[index][5], self.state[index][2] = \
			self.state[index][0], self.state[index][1], self.state[index][2], \
			self.state[index][3], self.state[index][4], self.state[index][5], \
			self.state[index][6], self.state[index][7], self.state[index][8]
		else:
			print("Can't rotate face values!")

	def rotateTop(self, face, dir):
		"""rotate the top layer"""
		
		index = 0
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[4][0], self.state[4][1], self.state[4][2], \
			self.state[1][0], self.state[1][1], self.state[1][2], \
			self.state[2][0], self.state[2][1], self.state[2][2], \
			self.state[3][0], self.state[3][1], self.state[3][2] = \
			self.state[1][0], self.state[1][1], self.state[1][2], \
			self.state[2][0], self.state[2][1], self.state[2][2], \
			self.state[3][0], self.state[3][1], self.state[3][2], \
			self.state[4][0], self.state[4][1], self.state[4][2]
			

		elif dir == 'CCW':
			self.state[1][0], self.state[1][1], self.state[1][2], \
			self.state[2][0], self.state[2][1], self.state[2][2], \
			self.state[3][0], self.state[3][1], self.state[3][2], \
			self.state[4][0], self.state[4][1], self.state[4][2] = \
			self.state[4][0], self.state[4][1], self.state[4][2], \
			self.state[1][0], self.state[1][1], self.state[1][2], \
			self.state[2][0], self.state[2][1], self.state[2][2], \
			self.state[3][0], self.state[3][1], self.state[3][2]


	def rotateFront(self, face, dir):
		"""rotate the front layer"""
		index = 2
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[0][8], self.state[0][7], self.state[0][6], \
			self.state[1][2], self.state[1][5], self.state[1][8], \
			self.state[3][0], self.state[3][3], self.state[3][6], \
			self.state[5][2], self.state[5][1], self.state[5][0] = \
			self.state[1][2], self.state[1][5], self.state[1][8], \
			self.state[5][0], self.state[5][1], self.state[5][2], \
			self.state[0][6], self.state[0][7], self.state[0][8], \
			self.state[3][0], self.state[3][3], self.state[3][6]

		elif dir == 'CCW':
			self.state[1][2], self.state[1][5], self.state[1][8], \
			self.state[5][0], self.state[5][1], self.state[5][2], \
			self.state[0][6], self.state[0][7], self.state[0][8], \
			self.state[3][0], self.state[3][3], self.state[3][6] = \
			self.state[0][8], self.state[0][7], self.state[0][6], \
			self.state[1][2], self.state[1][5], self.state[1][8], \
			self.state[3][0], self.state[3][3], self.state[3][6], \
			self.state[5][2], self.state[5][1], self.state[5][0]
			
	def rotateLeft(self, face, dir):
		"""rotate the left layer"""
		index = 1
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[2][0], self.state[2][3], self.state[2][6], \
			self.state[5][0], self.state[5][3], self.state[5][6], \
			self.state[0][0], self.state[0][3], self.state[0][6], \
			self.state[4][2], self.state[4][5], self.state[4][8] = \
			self.state[0][0], self.state[0][3], self.state[0][6], \
			self.state[2][0], self.state[2][3], self.state[2][6], \
			self.state[4][8], self.state[4][5], self.state[4][2], \
			self.state[5][6], self.state[5][3], self.state[5][0]

		elif dir == 'CCW':
			self.state[0][0], self.state[0][3], self.state[0][6], \
			self.state[2][0], self.state[2][3], self.state[2][6], \
			self.state[4][8], self.state[4][5], self.state[4][2], \
			self.state[5][6], self.state[5][3], self.state[5][0] = \
			self.state[2][0], self.state[2][3], self.state[2][6], \
			self.state[5][0], self.state[5][3], self.state[5][6], \
			self.state[0][0], self.state[0][3], self.state[0][6], \
			self.state[4][2], self.state[4][5], self.state[4][8]

	def rotateRight(self, face, dir):
		"""rotate the right layer"""
		index = 3
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[0][2], self.state[0][5], self.state[0][8], \
			self.state[2][2], self.state[2][5], self.state[2][8], \
			self.state[4][6], self.state[4][3], self.state[4][0], \
			self.state[5][8], self.state[5][5], self.state[5][2] = \
			self.state[2][2], self.state[2][5], self.state[2][8], \
			self.state[5][2], self.state[5][5], self.state[5][8], \
			self.state[0][2], self.state[0][5], self.state[0][8], \
			self.state[4][0], self.state[4][3], self.state[4][6]

		elif dir == 'CCW':
			self.state[2][2], self.state[2][5], self.state[2][8], \
			self.state[5][2], self.state[5][5], self.state[5][8], \
			self.state[0][2], self.state[0][5], self.state[0][8], \
			self.state[4][0], self.state[4][3], self.state[4][6] = \
			self.state[0][2], self.state[0][5], self.state[0][8], \
			self.state[2][2], self.state[2][5], self.state[2][8], \
			self.state[4][6], self.state[4][3], self.state[4][0], \
			self.state[5][8], self.state[5][5], self.state[5][2]


	def rotateBottom(self, face, dir):
		"""rotate the bottom layer"""
		index = 5
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[2][6], self.state[2][7], self.state[2][8], \
			self.state[3][6], self.state[3][7], self.state[3][8], \
			self.state[4][6], self.state[4][7], self.state[4][8], \
			self.state[1][6], self.state[1][7], self.state[1][8] = \
			self.state[1][6], self.state[1][7], self.state[1][8], \
			self.state[2][6], self.state[2][7], self.state[2][8], \
			self.state[3][6], self.state[3][7], self.state[3][8], \
			self.state[4][6], self.state[4][7], self.state[4][8]

		elif dir == 'CCW':
			self.state[1][6], self.state[1][7], self.state[1][8], \
			self.state[2][6], self.state[2][7], self.state[2][8], \
			self.state[3][6], self.state[3][7], self.state[3][8], \
			self.state[4][6], self.state[4][7], self.state[4][8] = \
			self.state[2][6], self.state[2][7], self.state[2][8], \
			self.state[3][6], self.state[3][7], self.state[3][8], \
			self.state[4][6], self.state[4][7], self.state[4][8], \
			self.state[1][6], self.state[1][7], self.state[1][8]

	def rotateBack(self, face, dir):
		"""rotate the back layer"""
		index = 4
		self.rotateFace(dir, index)
		if dir == 'CW':
			self.state[0][0], self.state[0][1], self.state[0][2], \
			self.state[1][6], self.state[1][3], self.state[1][0], \
			self.state[3][2], self.state[3][5], self.state[3][8], \
			self.state[5][8], self.state[5][7], self.state[5][6] = \
			self.state[3][2], self.state[3][5], self.state[3][8], \
			self.state[0][0], self.state[0][1], self.state[0][2], \
			self.state[5][8], self.state[5][7], self.state[5][6], \
			self.state[1][6], self.state[1][3], self.state[1][0]

		elif dir == 'CCW':
			self.state[3][2], self.state[3][5], self.state[3][8], \
			self.state[0][0], self.state[0][1], self.state[0][2], \
			self.state[5][8], self.state[5][7], self.state[5][6], \
			self.state[1][6], self.state[1][3], self.state[1][0] = \
			self.state[0][0], self.state[0][1], self.state[0][2], \
			self.state[1][6], self.state[1][3], self.state[1][0], \
			self.state[3][2], self.state[3][5], self.state[3][8], \
			self.state[5][8], self.state[5][7], self.state[5][6]
		
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