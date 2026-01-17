from window import Window
from first import doStuff
from line import Line, getEndPoint
from point import Point


def main():

    # print("Hello from bd-fractal!")
    win = Window(500, 500, "Hello from bd-fractal!")

    length = win.height // 2
    start = Point(0, 0)
    endPoints: list[Point] = []

    # Q1
    endPoints.append(getEndPoint(start, 0, length))
    endPoints.append(getEndPoint(start, 30, length))
    endPoints.append(getEndPoint(start, 60, length))
    # endPoints.append(getEndPoint(start, 45, length))
    endPoints.append(getEndPoint(start, 90, length))

    # Q2
    endPoints.append(getEndPoint(start, 120, length))
    endPoints.append(getEndPoint(start, 150, length))
    # endPoints.append(getEndPoint(start, 135, length))
    endPoints.append(getEndPoint(start, 180, length))

    # Q3
    endPoints.append(getEndPoint(start, 210, length))
    endPoints.append(getEndPoint(start, 240, length))
    # endPoints.append(getEndPoint(start, 225, length))
    endPoints.append(getEndPoint(start, 270, length))

    # Q4
    endPoints.append(getEndPoint(start, 300, length))
    endPoints.append(getEndPoint(start, 330, length))
    # endPoints.append(getEndPoint(start, 315, length))

    for end in endPoints:
        line = Line(start, end)
        doStuff(win, line)

    # Q1
    # line = Line(Point(0, 0), Point(0, length))
    # doStuff(win, line)
    # line = Line(Point(0, 0), Point(length, length))
    # doStuff(win, line)
    # line = Line(Point(0, 0), Point(length, 0))
    # doStuff(win, line)

    # Q2
    # line = Line(Point(0, 0), Point(-length, length))
    # doStuff(win, line)
    # line = Line(Point(0, 0), Point(-length, 0))
    # doStuff(win, line)

    win.wait()


if __name__ == "__main__":
    main()
