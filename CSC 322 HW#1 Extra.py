### 
### Created by David S. 
### CSC 322 HW#1 Code 

import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0
width,height= 500,500 			# window size

def drawSquare(x,y,width,height):
 glBegin(GL_QUADS) 			# start drawing a square
 glVertex2f(x,y) 			# bottom left point
 glVertex2f(x + width,y)		# bottom right point
 glVertex2f(x + width,y + height)	# top right point
 glVertex2f(x, y + height)		# top left point
 glEnd()				# done drawing

def drawTriangle(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x,y)
 glVertex2f(x + width,y)
 glVertex2f(x + width,y + height)
 glEnd()



def drawScene():
 glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 	# clear the screen
 glLoadIdentity() 					# reset position
 refresh2d(width, height)

# (x.x, x.x, x.x) = RGB values
# glColor3f(0.0, 0.0, 0.0);          black 
# glColor3f(1.0, 0.0, 0.0);           red 
# glColor3f(0.0, 1.0, 0.0);           green 
# glColor3f(1.0, 1.0, 0.0);           yellow 
# glColor3f(0.0, 0.0, 1.0);           blue 
# glColor3f(1.0, 0.0, 1.0);           magenta 
# glColor3f(0.0, 1.0, 1.0);           cyan 
# glColor3f(1.0, 1.0, 1.0);           white

 glColor3f(1.0,1.0,1.0)
 # draw a square at (50,50) with width 200, height 200
 drawSquare(10,10,450,450)

 glColor3f(0.0,0.0,0.0)
 drawSquare(30,30,400,400)

 glColor3f(1.0,1.0,1.0)
 drawSquare(50,50,350,350)

 glColor3f(0.0,0.0,0.0)
 drawSquare(70,70,300,300)

 glColor3f(1.0,1.0,1.0)
 drawSquare(90,90,250,250)

 glColor3f(0.0,0.0,0.0)
 drawSquare(110,110,200,200)

 glColor3f(1.0,1.0,1.0)
 drawSquare(130,130,150,150)

 glColor3f(0.0,0.0,0.0)
 drawSquare(150,150,100,100)

 glColor3f(1.0,1.0,1.0)
 drawSquare(170,170,50,50)
 


 glutSwapBuffers() # important for double buffering

def refresh2d(width, height):
 glViewport(0,0, width, height)
 glMatrixMode(GL_PROJECTION)
 glLoadIdentity()
 glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
 glMatrixMode (GL_MODELVIEW)
 glLoadIdentity()


# initialization
glutInit() 							#initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)
glutInitWindowSize(width, height) 				#set window size
glutInitWindowPosition(0, 0) 					#set window position
wind = glutCreateWindow("Visual Illusion") 		#create window with title
glutDisplayFunc(drawScene) 						#set showScreen function callback
glutIdleFunc(drawScene) 						#draw all the time
glutMainLoop() 							#start everything
