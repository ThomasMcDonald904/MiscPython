from graphics import *
from math import *


win = GraphWin(width=400, height=400)

point = Point(win.width + 20, win.height)
point.draw(win)

while True:
    for angle in range(360):
        point.move(cos(angle)*20, cos(angle)*20)

win.close()
