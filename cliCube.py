#local

import StoreImageValuesInArray

#libs


class cliCube():

	def __init__(self):
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
		#                       '#' 'y' '#'1
		#                       '#' '#' '#'

		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'
		#   '#' 'g' '#'3        '#' 'o' '#'2        '#' 'b' '#'4
		#   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'

		#                       '#' '#' '#'
		#                       '#' 'w' '#'5
		#                       '#' '#' '#'

		#                       '#' '#' '#'
		#                       '#' 'r' '#'6
		#                       '#' '#' '#'
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

	# def ImageProcessedArray(self):
		"""get array from StoreImageValuesInArray and return"""
		# newArray = StoreImageValuesInArray.SaveToArray()
		# arrayOfValues = newArray.returnArray()
		"""for testing purposes"""
		# arrayOfValues = [['silver', 'maroon', 'teal', 'orange', 'teal', 'white', 'teal', 'yellow', 'yellow'], ['silver', 'red', 'teal', 'white', 'teal', 'yellow', 'teal', 'orange', 'yellow'], ['silver', 'teal', 'teal', 'teal', 'orange', 'yellow', 'teal', 'teal', 'yellow'], ['maroon', 'orange', 'orange', 'teal', 'red', 'teal', 'orange', 'teal', 'red'], ['orange', 'maroon', 'red', 'white', 'white', 'teal', 'yellow', 'red', 'teal'], ['teal', 'orange', 'white', 'teal', 'yellow', 'white', 'maroon', 'orange', 'orange']]
		# return arrayOfValues

	def rotateTop(self, face, dir):
		#Error!
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
		#Tested 100%
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
		#Tested
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
		#Tested
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
		#Tested
		index = 4
		# pass
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
		# updatedArray = arrayOfValues
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
			# index = 1
		elif face == 'L': #Left
			self.rotateLeft(face, direction)
			# index = 2
		elif face == 'R': #Right
			self.rotateRight(face, direction)
			# index = 3
		elif face == 'B': #Bottom
			self.rotateBottom(face, direction)
			# index = 4
		elif face == 'Ba': #Back
			self.rotateBack(face, direction)
			# index = 5
		else:
			print('ERROR! Unknown face name: input = "T", "F", "B", "Ba", "L", "R"')
			return