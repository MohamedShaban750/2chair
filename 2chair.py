from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def init():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def seat(a,b,c,d,e,f):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glLineWidth(2)
    glTranslate(a,b,c)
    glScale(d,e,f)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

def back(m,n,o,p,q,r):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, 0, 0)
    glTranslate(m, n, o)
    glScale(p, q, r)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

def leg(g,h,i,j,k,l):
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0,1)
    glTranslate(g,h,i)
    glScale(j,k,l)
    glutSolidCube(.5)
    glPopAttrib()
    glPopMatrix()



def drawChair():
    #chair 1

    leg(-1.31, -1.5, 1.2,1, 5, 1)
    leg(1.2, -1.5, 1.20, 1, 5, 1)
    leg(0, -1, -.6, 1,5, 1)
    leg(1, -1.5, -2.1, 1,5, 1)
    seat(0,0,0,3,.25,3)
    back(-2, 0, -4,3.8, 4, .5)


  #chair 1

    leg(-7.31, -1.5, 1.2,1, 5, 1)
    leg(-4.8, -1.5, 1.2,1, 5, 1)
    leg(-6.25, -1.5, -1 ,1, 5, 1)
    leg(-4, -0.5, -.7,1, 5, 1)
    seat(-6, 0, 0,3, .25, 3)
    back(-9.5, 0,-4,3.5,4,.5)




    glFlush()

###########################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Chair")
glutDisplayFunc(drawChair)
init()
glutMainLoop()




