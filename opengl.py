# pip install PyOpenGL PyOpenGL_accelerate
# pip install pygame
# pip install numpy

import pygame
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),    # 0
    (1, 1, -1),     # 1
    (-1, 1, -1),    # 2
    (-1, -1, -1),   # 3
    (1, -1, 1),     # 4
    (1, 1, 1),      # 5
    (-1, -1, 1),    # 6
    (-1, 1, 1)      # 7
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

faces = (
    # X positivo (1, 0, 4, 5)
    (1, 0, 4, 5),
    # X negativo (2, 3, 6, 7)
    (2, 3, 6, 7),
    # Y positivo (2, 1, 5, 7)
    (2, 1, 5, 7),
    # Y negativo (3, 0, 4, 6)
    (3, 0, 4, 6),
    # Z positivo (5, 4, 6, 7)
    (5, 4, 6, 7),
    # Z negativo (0, 1, 2, 3)
    (0, 1, 2, 3)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Cube2(p, l):
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            v = (np.array(verticies[vertex]) + np.array(p)) * l
            glVertex3fv(v)
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()

        Cube2((1, -3, 1), 0.1)
        Cube2((-1, -3, 1), 0.1)
        Cube2((3, -1, 1), 0.1)
        Cube2((-3, -1, 1), 0.1)
        Cube2((3, 1, 1), 0.1)
        Cube2((-3, 1, 1), 0.1)
        Cube2((-3, 3, 1), 0.1)
        Cube2((1, 1, 1), 0.1)
        Cube2((-3, 5, 1), 0.1)
        Cube2((-1, 7, 1), 0.1)
        Cube2((1, 7, 1), 0.1)
        Cube2((3, 5, 1), 0.1)
        
        pygame.display.flip()
        pygame.time.wait(10)

main()