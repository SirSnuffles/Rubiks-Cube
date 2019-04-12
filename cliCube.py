#local

import StoreImageValuesInArray

#libs

import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


# arrayOfValues = [['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],        #1-9 w
#                 ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],         #10-18 o
#                 ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],         #19-27 y
#                 ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],         #28-36 r
#                 ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'],         #37-45 b
#                 ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']]         #46-54 g


class cliCube():

    def __init__(self, arrayOfValues):
        self.arrayOfValues = arrayOfValues

    def __str__(self):
        """prints a formatted perspective of arrayOfValues for clarity"""
        #bworgy
    #                       '#' '#' '#'
    #                       '#' 'b' '#'
    #                       '#' '#' '#'

    #   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'
    #   '#' 'o' '#'         '#' 'w' '#'         '#' 'r' '#'
    #   '#' '#' '#'         '#' '#' '#'         '#' '#' '#'

    #                       '#' '#' '#'
    #                       '#' 'g' '#'
    #                       '#' '#' '#'

    #                       '#' '#' '#'
    #                       '#' 'y' '#'
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

    def ImageProcessedArray(self):
        """get array from StoreImageValuesInArray and return"""
        # newArray = StoreImageValuesInArray.SaveToArray()
        # arrayOfValues = newArray.returnArray()
        """for testing purposes"""
        arrayOfValues = [['silver', 'maroon', 'teal', 'orange', 'teal', 'white', 'teal', 'yellow', 'yellow'], ['silver', 'red', 'teal', 'white', 'teal', 'yellow', 'teal', 'orange', 'yellow'], ['silver', 'teal', 'teal', 'teal', 'orange', 'yellow', 'teal', 'teal', 'yellow'], ['maroon', 'orange', 'orange', 'teal', 'red', 'teal', 'orange', 'teal', 'red'], ['orange', 'maroon', 'red', 'white', 'white', 'teal', 'yellow', 'red', 'teal'], ['teal', 'orange', 'white', 'teal', 'yellow', 'white', 'maroon', 'orange', 'orange']]
        return arrayOfValues

	def rotateTop(self, dir):
		if dir == 'CW':
			self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
			self.arrayOfValues[5][6], self.arrayOfValues[5][7], self.arrayOfValues[5][8], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2] = \
			self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
			self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
			self.arrayOfValues[5][6], self.arrayOfValues[5][7], self.arrayOfValues[5][8], \
			self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2]
		elif dir == 'CCW':
            self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2], \
            self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
            self.arrayOfValues[5][6], self.arrayOfValues[5][7], self.arrayOfValues[5][8], \
            self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2] = \
            self.arrayOfValues[2][0], self.arrayOfValues[2][1], self.arrayOfValues[2][2], \
            self.arrayOfValues[5][6], self.arrayOfValues[5][7], self.arrayOfValues[5][8], \
            self.arrayOfValues[3][0], self.arrayOfValues[3][1], self.arrayOfValues[3][2], \
            self.arrayOfValues[1][0], self.arrayOfValues[1][1], self.arrayOfValues[1][2]
		
	def rotateFront(self, dir):
		if dir == 'CW':
			self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6], \
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
			self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8], \
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8] = \
			self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8],\
			self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6],\
			self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2],\
			self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8]
		elif dir == 'CCW':
            self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8],\
            self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6],\
            self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2],\
            self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8] = \
            self.arrayOfValues[3][0], self.arrayOfValues[3][3], self.arrayOfValues[3][6], \
            self.arrayOfValues[4][0], self.arrayOfValues[4][1], self.arrayOfValues[4][2], \
            self.arrayOfValues[2][2], self.arrayOfValues[2][5], self.arrayOfValues[2][8], \
            self.arrayOfValues[0][6], self.arrayOfValues[0][7], self.arrayOfValues[0][8] 
			
	def rotateBottom(self, dir):
	    if dir == 'CW':
            self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8], \
            self.arrayOfValues[5][0], self.arrayOfValues[5][1], self.arrayOfValues[5][2], \
            self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8], \
            self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8] = \
            self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8],\
            self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8],\
            self.arrayOfValues[5][0], self.arrayOfValues[5][1], self.arrayOfValues[5][2],\
            self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8]
	    elif dir == 'CCW':
            self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8],\
            self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8],\
            self.arrayOfValues[5][0], self.arrayOfValues[5][1], self.arrayOfValues[5][2],\
            self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8] = \
            self.arrayOfValues[3][6], self.arrayOfValues[3][7], self.arrayOfValues[3][8], \
            self.arrayOfValues[5][0], self.arrayOfValues[5][1], self.arrayOfValues[5][2], \
            self.arrayOfValues[2][6], self.arrayOfValues[2][7], self.arrayOfValues[2][8], \
            self.arrayOfValues[1][6], self.arrayOfValues[1][7], self.arrayOfValues[1][8]
			
	def rotateBack(self, dir):
	    if dir == 'CW':
            self.arrayOfValues[2][0], self.arrayOfValues[2][3], self.arrayOfValues[2][6], \
            self.arrayOfValues[4][6], self.arrayOfValues[4][7], self.arrayOfValues[4][8], \
            self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
            self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2] = \
            self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2],\
            self.arrayOfValues[2][0], self.arrayOfValues[2][3], self.arrayOfValues[2][6],\
            self.arrayOfValues[4][6], self.arrayOfValues[4][7], self.arrayOfValues[4][8],\
            self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8]
		elif dir == 'CCW':
            self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2],\
            self.arrayOfValues[2][0], self.arrayOfValues[2][3], self.arrayOfValues[2][6],\
            self.arrayOfValues[4][6], self.arrayOfValues[4][7], self.arrayOfValues[4][8],\
            self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8] = \
			self.arrayOfValues[2][0], self.arrayOfValues[2][3], self.arrayOfValues[2][6], \
            self.arrayOfValues[4][6], self.arrayOfValues[4][7], self.arrayOfValues[4][8], \
            self.arrayOfValues[3][2], self.arrayOfValues[3][5], self.arrayOfValues[3][8], \
            self.arrayOfValues[0][0], self.arrayOfValues[0][1], self.arrayOfValues[0][2] 
		
	def rotateLeft(self, dir):
	    if dir == 'CW':
            self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
            self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
            self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
            self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6] = \
            self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6], \
            self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
            self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
            self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6]	
		elif dir == 'CCW':
            self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6],\
            self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6],\
            self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6],\
            self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6] = \
            self.arrayOfValues[1][0], self.arrayOfValues[1][3], self.arrayOfValues[1][6], \
            self.arrayOfValues[4][0], self.arrayOfValues[4][3], self.arrayOfValues[4][6], \
            self.arrayOfValues[5][0], self.arrayOfValues[5][3], self.arrayOfValues[5][6], \
            self.arrayOfValues[0][0], self.arrayOfValues[0][3], self.arrayOfValues[0][6] 
			
	def rotateRight(self, dir):
	    if face == 'R':
            self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8],\
            self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8],\
            self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8],\
            self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8] = \
            self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
            self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
            self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
            self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8]
	    elif dir == 'CCW':
            self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8], \
            self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8], \
            self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8], \
            self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8] = \
            self.arrayOfValues[5][2], self.arrayOfValues[5][5], self.arrayOfValues[5][8],\
            self.arrayOfValues[4][2], self.arrayOfValues[4][5], self.arrayOfValues[4][8],\
            self.arrayOfValues[1][2], self.arrayOfValues[1][5], self.arrayOfValues[1][8],\
            self.arrayOfValues[0][2], self.arrayOfValues[0][5], self.arrayOfValues[0][8]

    def rotateLayer(self, face, direction, arrayOfValues):
        # updatedArray = arrayOfValues

        index = None
        if face == 'T': #Top
            index = 0
        elif face == 'F': #Front
            index = 1
        elif face == 'L': #Left
            index = 2
        elif face == 'R': #Right
            index = 3
        elif face == 'B': #Bottom
            index = 4
        elif face == 'BA': #Back
            index = 5
        else:
            print('ERROR! Unknown face name: input = "T", "F", "B", "BA", "L", "R"')
            return
        if direction == 'CW':
            #rotate the face clockwise
            arrayOfValues[index][0], arrayOfValues[index][1], arrayOfValues[index][2], arrayOfValues[index][3], arrayOfValues[index][4], arrayOfValues[index][5], arrayOfValues[index][6], arrayOfValues[index][7], arrayOfValues[index][8] = \
            arrayOfValues[index][6], arrayOfValues[index][3], arrayOfValues[index][0], arrayOfValues[index][7], arrayOfValues[index][4], arrayOfValues[index][1], arrayOfValues[index][8], arrayOfValues[index][5], arrayOfValues[index][2]
            
            #rotate first layer clockwise













        elif direction == 'CCW':
            #rotate the face counter-clockwise

            arrayOfValues[index][0], arrayOfValues[index][1], arrayOfValues[index][2], arrayOfValues[index][3], arrayOfValues[index][4], arrayOfValues[index][5], arrayOfValues[index][6], arrayOfValues[index][7], arrayOfValues[index][8] = \
            arrayOfValues[index][2], arrayOfValues[index][5], arrayOfValues[index][8], arrayOfValues[index][1], arrayOfValues[index][4], arrayOfValues[index][7], arrayOfValues[index][0], arrayOfValues[index][3], arrayOfValues[index][6]
            
            #rotate first layer clockwise









        #needs testing because is buggy
        #could be simplified patterns are 2,5,8; 0,3,6; 6,7,8; 0,1,2

        else:
            print('ERROR! Unknown rotation direction: input = "CW", "CCW"')

def main():
    #make cube RubiksCube object

    arrayOfValues = [['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'], ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'], ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange'], ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'], ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']]
    # for i, array in enumerate(arrayOfValues):
    #     for j, value in enumerate(array):
    #         arrayOfValues[i][j] = arrayOfValues[i][j] + str(j)
    # arrayOfValues = [['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'], ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'], ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'], ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'], ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']]
    # arrayOfValues = [['silver', 'maroon', 'teal', 'orange', 'teal', 'white', 'teal', 'yellow', 'yellow'], ['silver', 'red', 'teal', 'white', 'teal', 'yellow', 'teal', 'orange', 'yellow'], ['silver', 'teal', 'teal', 'teal', 'orange', 'yellow', 'teal', 'teal', 'yellow'], ['maroon', 'orange', 'orange', 'teal', 'red', 'teal', 'orange', 'teal', 'red'], ['orange', 'maroon', 'red', 'white', 'white', 'teal', 'yellow', 'red', 'teal'], ['teal', 'orange', 'white', 'teal', 'yellow', 'white', 'maroon', 'orange', 'orange']]
    # cube = RubiksCube(ImageProcessedArray())
    cube = cliCube(arrayOfValues)
    # arrayOfValues = ImageProcessedArray()
    print(cube.__str__())
    cube.rotateLayer('R', 'CW', arrayOfValues)
    print(cube.__str__())
    
    cube.rotateLayer('L', 'CW', arrayOfValues)
    print(cube.__str__())
    # rotateLayer('T', 'CCW', arrayOfValues)
    # print(newCube.__str__())


if __name__ == "__main__":
    main()
    # pygame.quit()
    # quit()
