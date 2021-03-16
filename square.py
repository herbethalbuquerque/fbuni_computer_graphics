# pip install PyOpenGL PyOpenGL_accelerate
# pip install pygame
# pip install numpy

import pygame
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def square(p, l):
    v1 = np.array((-1, -1, 0)) * l + np.array(p)
    v2 = np.array((-1, 1, 0)) * l + np.array(p)
    v3 = np.array((1, 1, 0)) * l + np.array(p)
    v4 = np.array((1, -1, 0)) * l + np.array(p)

    glBegin(GL_QUADS)
    glVertex3fv(v1)
    glVertex3fv(v2)
    glVertex3fv(v3)
    glVertex3fv(v4)
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(70, (display[0]/display[1]), 0.1, 50.0)

    width = 4
    height = 3

    z = -5
    l = 0.3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        for e in range(-width, width + 1):
            square((e , -height, z), l)
            square((e , height, z), l)

        for e in range(-height + 1, height):
            square((-width , e, z), l)
            square((width , e, z), l)

        pygame.display.flip()

main()