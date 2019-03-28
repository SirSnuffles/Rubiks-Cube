import pygame
import random
from pygame.locals import *

from PiBasicRotation import MotorControl

from OpenGL.GL import *
from OpenGL.GLU import *


#set a cubes starting vertices
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
#set a subes starting edges according to above vertices
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
#set a cubes starting surfaces according to above edges
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0), 
    (1, 5, 7, 2), 
    (4, 0, 3, 6)
)
#set basic rgb colour scheme (r,g,b) // 1:255
colors = (
    (1, 0, 0), 
    (0, 1, 0), 
    (1, 0.5, 0), 
    (0, 0, 1), 
    (1, 1, 0),
    (1, 1, 1)
)

class Cube():
    """creates a single cube which can be drawn and updated"""
    def __init__(self, id, N, scale):
        """
        id =        id of cube to perform operations on;
        i =         (ix, iy, iz) :: (iz, iy, N-1-ix) inverting indices when rotated;
        N =         Number of pieces per edge (3^3 = 27 number of cubes in total);
        scale =     size;
        init =      Where each cube is initially located;
        currentI =  Where each cube is currently located; 
        rot =       rotation matrix; 3 x size 3 arrays containing vertex positions"""
        self.i = -1
        self.N = N
        self.scale = scale
        self.initI = [i - (N // 2) for i in id]
        self.currentI = [i - (N // 2) for i in id]
        self.rot = [[1 if i == j else 0 for i in range(3)] for j in range(3)]

    def isAffected(self, axis, slice, dir):
        """returns bool to determine if cube is part of a slice to be rotated"""
        return self.currentI[axis] == slice - (self.N // 2)

    def update(self, axis, slice, dir):
        """rotates a single cube based on the following attributes;
        axis = int, 0,1,2 indexed to corresponding orientation;
        slice = int, 0,1,2 indexed to corresponding slice;
        dir = int, -1,1 indexed to backward and forward respectively;
        """
        if not self.isAffected(axis, slice, dir):
            #if cube not affected return"""
            return
        #cube rotation
        i, j = (axis + 1) % 3, (axis + 2) % 3
        for k in range(3):
            self.rot[k][i], self.rot[k][j] = -self.rot[k][j] * dir, self.rot[k][i] * dir

        self.currentI[i], self.currentI[j] = -self.currentI[j] * dir, self.currentI[i] * dir

    def draw(self, col, surf, vert, animate, angle, axis, slice, dir):
        """draw cube with OpenGL Legacy matrix"""

        pos = [(p - (self.N % 1) / 2) * 2.1 * self.scale for p in self.currentI]
        rotMat = [*self.rot[0], 0, *self.rot[1], 0, *self.rot[2], 0, *pos, 1]

        glPushMatrix()
        if animate and self.isAffected(axis, slice, dir):
            glRotatef(angle * dir, *[1 if i == axis else 0 for i in range(3)])
        glMultMatrixf(rotMat) 
        glScalef(self.scale, self.scale, self.scale)

        glBegin(GL_QUADS)
        for i in range(len(surf)): #change for loop to only iterate according to outside colour surfaces
            #inplement function that will iterate through array and return a number to colour
            glColor3fv(colors[i]) #change i to an iterable that maps colour to arrayofvalues colour
            for j in surf[i]:
                glVertex3fv(vertices[j])
        glEnd()

        glPopMatrix()

class EntireCube(MotorControl):
    """grouping of all cubes;
        MotorControl will only work if run on 
        raspberry pi or disabling GPIO imports"""
    def __init__(self, N, scale):
        """MotorControl is inherited by EntireCube
        N = Size of cube
        cr = Cube size
        cubes = list of cubes(coords, N, scale)
        """
        MotorControl.__init__(self)
        self.N = N
        cr = range(self.N)
        self.cubes = [Cube((x, y, z), self.N, scale) for x in cr for y in cr for z in cr]

    def mainloop(self):
        """map keypresses to sliced groups of rotated cubes"""
        rotateUpKey, rotateDownKey, rotateLeftKey, rotateRightKey = False, False, False, False
        rotationalSensitivity = 2
        rotateWholeCube = 5

        #Keypresses K_DIR: ()
        rotCubeMap  = { 
                    K_UP: (-1, 0),
                    K_DOWN: (1, 0),
                    K_LEFT: (0, -1),
                    K_RIGHT: (0, 1)
        }
        #Keypresses K_alphanumeric: (x,y,z) "action" passes back into cube for each cube in the slice
        #mid is not needed as can't map to motor input
        rotSliceMap = {
                    K_1: (0, 0, 1),
                    # K_2: (0, 1, 1), #mid slice
                    K_3: (0, 2, 1), 
                    K_4: (1, 0, 1), 
                    # K_5: (1, 1, 1), #mid slice
                    K_6: (1, 2, 1), 
                    K_7: (2, 0, 1), 
                    # K_8: (2, 1, 1), #mid slice
                    K_9: (2, 2, 1),
                    K_q: (0, 0, -1), 
                    # K_w: (0, 1, -1),#mid slice
                    K_e: (0, 2, -1), 
                    K_r: (1, 0, -1), 
                    # K_t: (1, 1, -1),#mid slice
                    K_y: (1, 2, -1), 
                    K_u: (2, 0, -1), 
                    # K_i: (2, 1, -1),#mid slice
                    K_o: (2, 2, -1),
        }  

        angX, angY, rotCube = 0, 0, (0, 0)
        animate, animateAng, animateSpeed = False, 0, 5
        action = (0, 0, 0)
        while True:
            for event in pygame.event.get():
                #quit on exit gui
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key in rotCubeMap:
                        #set rotCube to value of keypress dict
                        rotCube = rotCubeMap[event.key]
                    if not animate and event.key in rotSliceMap:
                        #motor control input
                        MotorControl.OrganiseMotorInput(self, str(pygame.key.name(event.key)))
                        #begin animation, set action to value of keypress dict
                        animate, action = True, rotSliceMap[event.key]
                if event.type == KEYUP:
                    #reset on release
                    if event.key in rotCubeMap:
                        rotCube = (0, 0)

            angX += rotateWholeCube * rotCube[0]
            angY += rotateWholeCube * rotCube[1]

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            #move cube back from "camera" to see
            glTranslatef(0, 0, -40)
            #rotation using opengl
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
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glEnable(GL_DEPTH_TEST) 

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    NewEntireCube = EntireCube(3, 1.5) 
    NewEntireCube.mainloop()

if __name__ == '__main__':
    main()
    pygame.quit()
    quit()