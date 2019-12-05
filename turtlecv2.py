import cv2
import numpy as np
import matplotlib.pyplot as plt

from google.colab.patches import cv2_imshow
img = np.zeros([500,500,3],dtype=np.uint8)
img.fill(200)
img[:] = (0, 0, 255)

import math
import time

is_pen_down=1


def initializeTurtle():
  global turtle_pos
  turtle_pos=(200,250)
  global thecolor
  thecolor = (255,200,0,255)
  global turtle_degree
  turtle_degree=-90
  global is_pen_down
  is_pen_down=1

def width(thk):
  global thethickness
  thethickness=thk

#def _updateDrawing():
    #if drawing_window == None:
    #    raise AttributeError("Display has not been initialized yet. Call initializeTurtle() before using.")
    #time.sleep(timeout)
    #drawing_window.update(HTML(_generateSvgDrawing()))

# helper function for managing any kind of move to a given 'new_pos' and draw lines if pen is down
def _moveToNewPosition(new_pos):
  global turtle_pos
  global thecolor

  start_pos = turtle_pos
  if is_pen_down:
    x1=int(start_pos[0])
    y1=int(start_pos[1])
    x2=int(new_pos[0])
    y2=int(new_pos[1])
    cv2.line(img, (x1,y1), (x2,y2), thecolor, thickness=thethickness) 

  #time.sleep(1)
  turtle_pos = new_pos
  #_updateDrawing()


# makes the turtle move forward by 'units' units
def forward(units):
    if not (isinstance(units, int) or isinstance(units, float)):
        raise ValueError('units should be int or float')

    alpha = math.radians(turtle_degree)
    ending_point = (turtle_pos[0] + units * math.cos(alpha), turtle_pos[1] + units * math.sin(alpha))

    _moveToNewPosition(ending_point)

# makes the turtle move right by 'degrees' degrees (NOT radians)
def right(degrees):
  global turtle_degree

  if not (isinstance(degrees, int) or isinstance(degrees, float)):
      raise ValueError('degrees should be a number')

  turtle_degree = (turtle_degree + degrees) % 360
  #time.sleep(1)
  #imgplot = plt.imshow(img)
  #_updateDrawing()

def left(degrees):
  global turtle_degree

  if not (isinstance(degrees, int) or isinstance(degrees, float)):
      raise ValueError('degrees should be a number')

  turtle_degree = (turtle_degree - degrees) % 360
  #plt.imshow(img)
  #plt.draw()
  #plt.pause(0.00001)
  #_updateDrawing()

def color2(r,g,b):
  global thecolor
  thecolor=(b,g,r)
  
def color(col):
  global thecolor
  thecolor=col

def bgcolor2(r,g,b):
  #img.fill(col)
  img[:] = (b,g,r)

def bgcolor(col):
  global thecolor
  img[:] = col
  
def circle(rad):
  global turtle_pos
  global thecolor

  start_pos = turtle_pos
  if is_pen_down:
    cv2.circle(img, turtle_pos, rad, thecolor) 
