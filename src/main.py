from window import Window
from first import doStuff
from point import Point


def main():

    # print("Hello from bd-fractal!")
    win = Window(800, 800, "Hello from bd-fractal!")
    length = win.height // 2
    start = Point(0, 0)

    doStuff(win, start, length)

    win.wait()


if __name__ == "__main__":
    main()
