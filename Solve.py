import Application
import random
print(random.randrange(0,3))

arrayOfValues = [['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'], ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'], ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'], ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'], ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']]

class Shuffle():
	def __init__(self):
		pass


class Stack():
     def __init__(self):
     	self.items = ['FCW', 'FCCW', 'BaCW','FCW', 'FCCW', 'BaCW','FCW', 'FCCW', 'BaCW']

     def isEmpty(self):
     	# print("checked if empty!")
     	return self.items == []

     def push(self, item):
     	# print("Pushed item: ", item)
     	self.items.append(item)

     def pop(self):
     	print("Popped item: ", self.items[-1])
     	return self.items.pop()

     def peek(self):
     	# print("Peeked at item: ", self.items[len(self.items)-1])
     	return self.items[len(self.items)-1]

     def size(self):
     	# print("size of stack: ", len(self.items))
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

	# def SolveSecondLayer(self):
	# 	while !SecondLayerSolved:
	# 		if 

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

class Algorithms():
	def __init__(self):
		self.FirstAlgorithm = {'R':'D', 'B':'L', 'R':'U', 'B':'R'}

		self.SecondLayerAlgorithmLeft = {'T':'L', 'R':'U', 'T':'R', 'R':'D', 'T':'R', 'F':'L', 'T':'L', 'F':'R'}

		self.SecondLayerAlgorithmRight = {'T':'R', 'L':'U', 'T':'L', 'L':'D', 'T':'L', 'F':'R', 'T':'R', 'F':'L'}

		self.InvertedCrossAlgorithm = {'F':'R', 'R':'U','T':'L','R':'D','T':'R','F':'L'}

		self.ThirdLayerAlgorithm = {'R':'U', 'T':'L', 'R':'D', 'T':'L', 'R':'U', 'T':'L', 'T':'L', 'R':'D'}

		self.ThirdLayerCornersAlgorithm = {'T':'L', 'R':'U','T':'R','L':'U','T':'L','R':'D','T':'R','L':'D'}



def main():
	pass

if __name__ == '__main__':
	main()