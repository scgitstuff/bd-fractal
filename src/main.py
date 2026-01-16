from window import Window
from first import doStuff
from line import Line
from point import Point


def main():
    # print("Hello from bd-fractal!")
    win = Window(500, 500, "Hello from bd-fractal!")

    line = Line(Point(0, 0), Point(0, 200))
    # print(line)
    doStuff(win, line)

    line = Line(Point(0, 0), Point(0, -200))
    # print(line)
    doStuff(win, line)

    line = Line(Point(0, 0), Point(200, 0))
    # print(line)
    doStuff(win, line)

    line = Line(Point(0, 0), Point(-200, 0))
    # print(line)
    doStuff(win, line)

    win.wait()


if __name__ == "__main__":
    main()
