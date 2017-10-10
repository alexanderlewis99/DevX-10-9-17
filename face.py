#Alec Wang
#face.py
#Python 3.6.1
#This program makes a cat's face appear when run

from graphics import *

#colors the interior and outline
def paint(object, color):
	object.setFill(color)
	object.setOutline(color)

#constructs, paints, and draws ovals
def oval_maker(p1, p2, color, GraphWin):
	oval = Oval(p1, p2)
	paint(oval, color)
	oval.draw(GraphWin)	

#constructs, paints, and draws triangles
def triangle_maker(p1, p2, p3, color, GraphWin):
	triangle = Polygon(p1, p2, p3)
	paint(triangle, color)
	triangle.draw(GraphWin)

#constructs, paints, and draws lines
def line_maker(p1, p2, color, GraphWin):
	line = Line(p1, p2)
	paint(line, color)
	line.draw(GraphWin)

#constructs, resizes, and draws text
def lyman_speak(anchorpoint, text, GraphWin):
	message = Text(anchorpoint, text)
	message.setSize(36)
	message.draw(GraphWin)


def main():
	#defines the window 
	win = GraphWin("Lyman the cat", 600, 450)
	
	#transforms the coordinates
	win.setCoords(0.0, 0.0, 10.0, 10.0)
	
	#draws the basic head
	catColor = color_rgb(255, 153, 0)
	oval_maker(Point(3.1, 2.5), Point(6.9, 7.5), catColor, win)
	
	#draws the nose
	noseColor = color_rgb(179, 107, 0)
	triangle_maker(Point(4.3, 5.0), Point(5.7, 5.0), Point(5.0, 3.8), noseColor, win)
	
	#draws the outer ears
	#left ear
	triangle_maker(Point(3.3, 6.0), Point(4.2, 7.0), Point(3.4, 7.9), catColor, win)
	#right ear
	triangle_maker(Point(10 - 3.3, 6.0), Point(10 - 4.2, 7.0), Point(10 - 3.4, 7.9), catColor, win)
	
	#draws the inner ear parts
	innerEarColor = color_rgb(255, 153, 204)
	#inner left ear
	triangle_maker(Point(3.9, 7.1), Point(3.45, 6.7), Point(3.5, 7.6), innerEarColor, win)
	#inner right ear
	triangle_maker(Point(10-3.9, 7.1), Point(10-3.45, 6.7), Point(10-3.5, 7.6), innerEarColor, win)
	
	#left eye
	#white of the eye
	oval_maker(Point(3.6, 6.6), Point(4.6, 5.6), "white", win)
	#left iris
	oval_maker(Point(3.6+.2, 6.58), Point(4.6-0.2, 5.6), "green", win)
	#left pupil
	oval_maker(Point(3.6+.4, 6.6-.3), Point(4.6-0.4, 5.6+.3), "black", win)
	
	#right eye
	#white of the eye
	oval_maker(Point(10 - 3.6, 6.6), Point(10 - 4.6, 5.6), "white", win)
	#right iris
	oval_maker(Point(10-(3.6+.2), 6.58), Point(10-(4.6-0.2), 5.6), "green", win)
	#right pupil
	oval_maker(Point(10-(3.6+.4), 6.6-.3), Point(10-(4.6-0.4), 5.6+.3), "black", win)
	
	#draws the mouth
	line_maker(Point(4.6, 3.0), Point(5.0, 3.3), "black", win)
	line_maker(Point(5.4, 3.0), Point(5.0, 3.3), "black", win)
	line_maker(Point(5.0, 3.3), Point(5.0, 3.6), "black", win)
	#upward/smiling pieces
	line_maker(Point(4.6, 3.0), Point(4.3, 3.3), "black", win)
	line_maker(Point(5.4, 3.0), Point(5.7, 3.3), "black", win)
	
	#left whiskers
	line_maker(Point(4.5, 4.6), Point(3.5, 4.9), "white", win)
	line_maker(Point(4.7, 4.3), Point(3.7, 4.5), "white", win)
	line_maker(Point(4.85, 4.0), Point(3.85, 4.1), "white", win)
	#right whiskers
	line_maker(Point(10-4.5, 4.6), Point(10-3.5, 4.9), "white", win)
	line_maker(Point(10-4.7, 4.3), Point(10-3.7, 4.5), "white", win)
	line_maker(Point(10-4.85, 4.0), Point(10-3.85, 4.1), "white", win)
	
	#on screen text
	lyman_speak(Point(5.0, 9.0), "I AM LYMAN", win)
	lyman_speak(Point(5.0, 1.0), "FEED ME COOKIES", win)
	
	#waits for user input to close
	input("press <Enter> to quit: ")
	win.close
	
main()