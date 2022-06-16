import time

from graphics import *
from math import *
import threading


def better_range(n, flip=False):
    if not flip:
        return range(n)
    else:
        flippedList = []
        for j in range(n):
            flippedList.append(n - j)
        return flippedList


win = GraphWin(width=1000, height=1000)

center = Point(win.width / 2, win.height / 2)

circle1 = Circle(center, 10)
circle1.draw(win)

circle2 = Circle(center, 10)
circle2.draw(win)

change_time = 0.00005


def color_loop():
    for i in better_range(255, True):
        circle1.setFill(color_rgb(i, 255 - i, 0))
        circle1.setOutline(color_rgb(i, 255 - i, 0))
        time.sleep(change_time)
    for i in better_range(255, True):
        circle1.setFill(color_rgb(0, i, 255 - i))
        circle1.setOutline(color_rgb(0, i, 255 - i))
        time.sleep(change_time)
    for i in better_range(255, True):
        circle1.setFill(color_rgb(255 - i, 0, i))
        circle1.setOutline(color_rgb(255 - i, 0, i))
        time.sleep(change_time)


radius = 80
refreshRate = 10


def movement_loop(graphics_object):
    for angle in range(360):
        dx = (center.x + cos(angle) * radius) - graphics_object.getCenter().x
        dy = (center.y + sin(angle) * radius) - graphics_object.getCenter().y
        graphics_object.move(dx, dy)
        time.sleep(1 / refreshRate)


if __name__ == "__main__":
    thread1 = threading.Thread(target=color_loop)
    thread2 = threading.Thread(target=movement_loop, args=(circle2,))

    while True:
        thread1.start()
        thread2.start()

win.getMouse()

win.close()
