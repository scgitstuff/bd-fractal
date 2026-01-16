from window import Window
from line import Line, lineAngle
from point import Point


def main():
    print("Testing")
    testPoint()
    testLine()
    testWindow()


def testPoint():
    p = Point(45, 60)
    print()
    print(p)
    print(p.asTuple())


def testLine():

    print(lineAngle(10, 0))
    print(lineAngle(10, 10))
    print(lineAngle(0, 10))
    print(lineAngle(-10, 10))
    print(lineAngle(-10, 0))

    print(lineAngle(-10, -10))
    print(lineAngle(0, -10))
    print(lineAngle(10, -10))

    line = Line(Point(10, 10), Point(200, 200))
    print(line)
    line = Line(Point(10, -10), Point(200, -200))
    print(line)

    line = Line(Point(-10, 10), Point(-200, 200))
    print(line)
    line = Line(Point(-10, -10), Point(-200, -200))
    print(line)


def testWindow():
    win = Window(500, 500, "testWindow")
    # lines = List[Line]

    # for this to work, have to use lineAngleCircle() in Line constructor
    # for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
    #     line = getLineFromAngle(Point(0, 0), angle, 200)
    #     win.drawLine(line, "blue")

    line = Line(Point(10, 10), Point(200, 200))
    win.drawLine(line, "blue")
    line = Line(Point(10, -10), Point(200, -200))
    win.drawLine(line, "red")

    line = Line(Point(-10, 10), Point(-200, 200))
    win.drawLine(line, "blue")
    line = Line(Point(-10, -10), Point(-200, -200))
    win.drawLine(line, "red")

    win.wait()


if __name__ == "__main__":
    main()
