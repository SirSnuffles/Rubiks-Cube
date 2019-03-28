class Solve():
	def __init__(self, InitSolvedSide):
		self.InitSolvedSide = InitSolvedSide
		self.InitSolvedSide = 'W'	
		self.OppositeInitSolvedSide = InvertInitSolvedSide()

	def FindPositionPiece(ColourToFind):
		"""split cubes into grouped blocks and return position and wether it is a middle or corner piece"""
		#return the positions of all ColourToFind
		index = 0
		for face in arrayOfValues:
			yield index, [i for i, e in enumerate([face]) if e == ColourToFind]
			index += 1

	def InvertInitSolvedSide(InitSolvedSide):
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

	def SolveSecondLayer(self):
		if self.OppositeInitSolvedSide:
			pass

	def SolveOpSideCross(self):
		pass

	def SolveThirdLayerMiddle(self):
		pass

	def SortThirdLayerCorners(self):
		pass

class Algorithms(object):
	def __init__(self):
		"""needs to hold order and multiple keys and values"""
		self.FirstAlgorithm = {'R':'D', 'B':'L', 'R':'U', 'B':'R'}

		self.SecondLayerAlgorithmLeft = {'T':'L', 'R':'U', 'T':'R', 'R':'D', 'T':'R', 'F':'L', 'T':'L', 'F':'R'}

		self.SecondLayerAlgorithmRight = {'T':'R', 'L':'U', 'T':'L', 'L':'D', 'T':'L', 'F':'R', 'T':'R', 'F':'L'}

		self.InvertedCrossAlgorithm = {'F':'R', 'R':'U','T':'L','R':'D','T':'R','F':'L'}

		self.ThirdLayerAlgorithm = {'R':'U', 'T':'L', 'R':'D', 'T':'L', 'R':'U', 'T':'L', 'T':'L', 'R':'D'}

		self.ThirdLayerCornersAlgorithm = {'T':'L', 'R':'U','T':'R','L':'U','T':'L','R':'D','T':'R','L':'D'}



def main():
	applyalgorithm = Algorithms()
	print(applyalgorithm.FirstAlgorithm)

if __name__ == '__main__':
	main()