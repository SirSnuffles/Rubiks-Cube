import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import random
from pygame.locals import *
import time
import cliCube
import _thread

from PiBasicRotation import IODevices
from Solve import Queue

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	( 1, -1, -1),
	( 1,  1, -1),
	(-1,  1, -1),
	(-1, -1, -1),
	( 1, -1,  1), 
	( 1,  1,  1), 
	(-1, -1,  1), 
	(-1,  1,  1)
)
edges = (
	(0,1),
	(0,3),
	(0,4),
	(2,1),
	(2,3),
	(2,7),
	(6,3),
	(6,4),
	(6,7),
	(5,1),
	(5,4),
	(5,7)
)
surfaces = (
	(0, 1, 2, 3),
	(3, 2, 7, 6),
	(6, 7, 5, 4),
	(4, 5, 1, 0), 
	(1, 5, 7, 2), 
	(4, 0, 3, 6)
)
colors = (
	(1, 0.5, 0), #O
	(0, 0, 1), #B
	(1, 0, 0), #R
	(0, 1, 0), #G
	(1, 1, 0), #Y
	(1, 1, 1) #W
)

class Cube():
	def __init__(self, id, N, scale):
		self.i = -1
		self.N = N
		self.scale = scale
		self.initI = [i - (N // 2) for i in id]
		self.currentI = [i - (N // 2) for i in id]
		self.rot = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

	def isAffected(self, axis, slice, dir):
		return self.currentI[axis] == slice - (self.N // 2)

	def update(self, axis, slice, dir):

		if not self.isAffected(axis, slice, dir):
			return

		i, j = (axis + 1) % 3, (axis + 2) % 3

		for k in range(3):
			self.rot[k][i], self.rot[k][j] = -self.rot[k][j] * dir, self.rot[k][i] * dir

		self.currentI[i], self.currentI[j] = -self.currentI[j] * dir, self.currentI[i] * dir

	def draw(self, col, surf, vert, animate, angle, axis, slice, dir):

		pos = [(p - (self.N % 1) / 2) * 2.05 * self.scale for p in self.currentI]
		#Set the rotation matrix to apply to the cube
		rotMat = [*self.rot[0], 0, *self.rot[1], 0, *self.rot[2], 0, *pos, 1]

		glPushMatrix()

		if animate and self.isAffected(axis, slice, dir):
			glRotatef(angle * dir, *[1 if i == axis else 0 for i in range(3)])
		glMultMatrixf(rotMat) 
		glScalef(self.scale, self.scale, self.scale)

		glBegin(GL_QUADS)
		for i in range(len(surf)): #change for loop to only iterate according to outside colour surfaces
			#implement function that will iterate through array and return a number to colour
			glColor3fv(colors[i]) #change i to an iterable that maps colour to state colour
			for j in surf[i]:
				glVertex3fv(vertices[j])
		glEnd()

		glPopMatrix()

class EntireCube(IODevices, Queue):
	"""create all cubes based on a matrix of cubes called self.cubes"""
	def __init__(self, N, scale, cli, screen):
		self.cli = cli
		IODevices.__init__(self)
		Queue.__init__(self, self.cli.state)
		self.screen = screen
		
		self.N = N
		cr = range(self.N)
		"""list that contains the cubes to be rendered"""
		self.cubes = [Cube((x, y, z), self.N, scale) for x in cr for y in cr for z in cr]

	def loadTexture(self):
	    textureSurface = pygame.image.load('blueSide.png')
	    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
	    width = textureSurface.get_width()
	    height = textureSurface.get_height()

	    glEnable(GL_TEXTURE_2D)
	    texid = glGenTextures(1)

	    glBindTexture(GL_TEXTURE_2D, texid)
	    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
	                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

	    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

	    return texid


	def mainloop(self):
		"""main gameloop"""
		rotateUpKey, rotateDownKey, rotateLeftKey, rotateRightKey = False, False, False, False
		rotationalSensitivity = 2
		rotateWholeCube = 5

		rotCubeMap  = { K_UP: (-1, 0), K_DOWN: (1, 0), K_LEFT: (0, -1), K_RIGHT: (0, 1)}
		rotSliceMap = {
			"LCW": (0, 0, 1),
			"RCCW": (0, 2, 1), 
			"BCW": (1, 0, 1), 
			"TCCW": (1, 2, 1), 
			"BaCW": (2, 0, 1), 
			"FCCW": (2, 2, 1),
			"LCCW": (0, 0, -1), 
			"RCW": (0, 2, -1), 
			"BCCW": (1, 0, -1), 
			"TCW": (1, 2, -1), 
			"BaCCW": (2, 0, -1), 
			"FCW": (2, 2, -1),
		}

		#commented moves are middle moves that cannot be matched to pibasicrotation file
		#due to physical restraints
		manualControl = {
			K_1: (0, 0, 1), 
			# K_2: (0, 1, 1), 
			K_3: (0, 2, 1), 
			K_4: (1, 0, 1),
			# K_5: (1, 1, 1),
			K_6: (1, 2, 1), 
			K_7: (2, 0, 1), 
			# K_8: (2, 1, 1), 
			K_9: (2, 2, 1),
			K_F1: (0, 0, -1), 
			# K_F2: (0, 1, -1), 
			K_F3: (0, 2, -1), 
			K_F4: (1, 0, -1), 
			# K_F5: (1, 1, -1),
			K_F6: (1, 2, -1), 
			K_F7: (2, 0, -1), 
			# K_F8: (2, 1, -1), 
			K_F9: (2, 2, -1),
		}

		angX, angY, rotCube = 0, 0, (0, 0)
		animate, animateAng, animateSpeed = False, 0, 30
		action = (0, 0, 0)

		while True:
			if not self.isEmpty():
				if self.peek() in rotCubeMap:
					rotCube = rotCubeMap[self.peek()]
				if not animate and self.peek() in rotSliceMap:
					poppedItem = self.pop()
					# self.cli.rotateLayer(poppedItem)
					# self.updateBoard(self.cli.state)
					# print(self.cli.__str__())
					# IODevices.OrganiseMotorInput(self, str(pygame.key.name(event.key)))
					animate, action = True, rotSliceMap[poppedItem]

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				# if IODevices.solveButton():
					# _thread.start_new_thread(self.Solve, ())

				# if IODevices.scrambleButton():
				# 	for i in range(10):
				# 		_thread.start_new_thread(self.Scramble, ())

				# if IODevices.manualButton() in rotCubeMap:
				# 	rotCube = rotCubeMap[]

				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					"""if left mouse button is pushed, add solve moves to queue"""
					_thread.start_new_thread(self.Solve, ())
					
					
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
					"""if right mouse button is pushed, add 10 scramble moves to queue"""
					for i in range(10):
						_thread.start_new_thread(self.Scramble, ())

				if event.type == KEYDOWN:
					"""if a manual control move is init, perform move"""
					if event.key in rotCubeMap:
						rotCube = rotCubeMap[event.key]

					if not animate and event.key in manualControl:
						getMove = manualControl[event.key]
						for key, value in rotSliceMap.items():
							if getMove == value:
								move = key
						self.cli.rotateLayer(move)
						IODevices.OrganiseMotorInput(self, str(pygame.key.name(event.key)))
						animate, action = True, manualControl[event.key]
				if event.type == KEYUP:
					if event.key in rotCubeMap:
						rotCube = (0, 0)

			angX += rotateWholeCube * rotCube[0]
			angY += rotateWholeCube * rotCube[1]

			glMatrixMode(GL_MODELVIEW)
			glEnable(GL_TEXTURE_2D)
			glLoadIdentity()
			glTranslatef(0, 0, -40)
			glRotatef(angY, 0, 1, 0)
			glRotatef(angX, 1, 0, 0)

			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

			if animate:
				if animateAng >= 90:
					for cube in self.cubes:
						cube.update(*action)
					animate = False
					animateAng = 0

			for cube in self.cubes:

				cube.draw(colors, surfaces, vertices, animate, animateAng, *action)

			if animate:
				animateAng += animateSpeed

			pygame.display.flip()
			pygame.time.wait(10)  

def main():
	pygame.init()
	display = (500,500)
	screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL|OPENGLBLIT)
	glEnable(GL_DEPTH_TEST) 

	glMatrixMode(GL_PROJECTION)
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	cli = cliCube.cliCube()

	NewEntireCube = EntireCube(3, 1.5, cli, screen) 
	NewEntireCube.mainloop()

if __name__ == '__main__':
	main()
	pygame.quit()
	quit()