from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from window import Window
from line import Line
from point import Point
import trig


def main():
    testPoint()
    testLine()
    testWindow()


def testPoint():
    p = Point(45, 60)
    print("\ntestPoint")
    print(p)
    print(p.asTuple())


def testLine():
    print("\ntestLine")
    print(trig.calcAngle360(10, 0))
    print(trig.calcAngle360(10, 10))
    print(trig.calcAngle360(0, 10))
    print(trig.calcAngle360(-10, 10))
    print(trig.calcAngle360(-10, 0))

    print(trig.calcAngle360(-10, -10))
    print(trig.calcAngle360(0, -10))
    print(trig.calcAngle360(10, -10))

    line = Line(Point(10, 10), Point(200, 200))
    print(line)
    line = Line(Point(10, -10), Point(200, -200))
    print(line)

    line = Line(Point(-10, 10), Point(-200, 200))
    print(line)
    line = Line(Point(-10, -10), Point(-200, -200))
    print(line)


def testWindow():
    root = Tk()
    win = Window(root, "testWindow")
    win.p.imageSize.set(500)
    start = Point(0, 0)

    print("\ntestWindow")
    for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
        line = Line(start, trig.getEndPoint(start, angle, 200))
        win.drawLine(line)

    line = Line(Point(50, 50), Point(100, 100), 3)
    win.drawLine(line, "blue")
    line = Line(Point(50, -50), Point(100, -100), 3)
    win.drawLine(line, "red")

    line = Line(Point(-50, 50), Point(-100, 100), 3)
    win.drawLine(line, "blue")
    line = Line(Point(-50, -50), Point(-100, -100), 3)
    win.drawLine(line, "red")

    root.mainloop()


if __name__ == "__main__":
    main()
