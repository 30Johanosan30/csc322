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

# For it to be drawn the other direction 
def drawTriangle2(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x,y + height)
 glVertex2f(x,y)
 glVertex2f(x + width,y)
 glEnd()

 # For it to be drawn different direction 
def drawTriangle3(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x,y)
 glVertex2f(x,y + height)
 glVertex2f(x + width,y + height)
 glEnd()

def drawTriangle4(x,y,width,height):
 glBegin(GL_TRIANGLES)
 glVertex2f(x + width,y)
 glVertex2f(x,y + height)
 glVertex2f(x + width,y + height)
 glEnd()

# To draw a circle, error has occured here 
def drawCircle(x, y, radius, diameter):
    glBegin(GL_POLYGON)
    glVertex2f((x - radius),(y - radius), diameter, diameter) 
    glEnd()


# To draw a rectangle
def drawRectangle(x,y,width,height):
 glBegin(GL_QUADS) 
 glVertex2f(x,y) 
 glVertex2f(x + width,y) 
 glVertex2f(x + width,y + height) 
 glVertex2f(x, y + height) 
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

 glColor3f(1.0,0.0,1.0)
 # draw a square at (50,50) with width 200, height 200
 drawSquare(50,30,220,200)  
 
 glColor3f(0.0,1.0,1.0)
 # draw a "roof" out of triangle 
 drawTriangle(50,230,100,100)

 glColor3f(0.0,1.0,1.0)
 # draw a "roof" out of triangle 
 drawTriangle2(150,230,120,100)

 glColor3f(1.0,1.0,1.0)
 # draw a "door" out of rectangle 
 drawRectangle(125,30,50,90)

# draw a "star" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(400,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(430,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(430,420,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(400,420,30,30)

 # draw a "star" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(320,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(350,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(350,420,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(320,420,30,30)

  # draw a "star" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(240,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(270,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(270,420,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(240,420,30,30)

  # draw a "star" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(160,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(190,450,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(190,420,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(160,420,30,30)

  # draw a "window" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(60,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(60,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(60,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(60,100,30,30)

 # draw a "window" out of triangles 
 glColor3f(1.0,1.0,1.0)
 drawTriangle(220,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle2(220,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle3(220,100,30,30)
 glColor3f(1.0,1.0,1.0) 
 drawTriangle4(220,100,30,30)

 # draw a "chimney" from a rectangle 
 glColor3f(1.0,1.0,1.0) 
 drawRectangle(50,230,50,90)

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
wind = glutCreateWindow("A House and Stars") 		#create window with title
glutDisplayFunc(drawScene) 						#set showScreen function callback
glutIdleFunc(drawScene) 						#draw all the time
glutMainLoop() 							#start everything
