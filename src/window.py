# from tkinter import Tk, BOTH, Canvas, ttk
from tkinter import Tk, Canvas
from line import Line
from point import Point


class Window:
    def __init__(
        self, width: int, height: int, title: str = "Fractal", background: str = "white"
    ):
        self.width = width
        self.height = height

        self.center = Point(width // 2, height // 2)

        self.root = Tk()
        self.root.title(title)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        # self.root.resizable(True, True)

        self.canvas = Canvas(
            self.root,
            width=self.width,
            height=self.height,
            background=background,
        )
        self.canvas.pack()

        self.isRunning = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()

    def close(self):
        self.isRunning = False

    def drawLine(self, line: Line, fillColor: str = "black"):
        self.canvas.create_line(
            *self._offset(line.start).asTuple(),
            *self._offset(line.end).asTuple(),
            fill=fillColor,
            width=line.width,
        )

    def _offset(self, p: Point) -> Point:
        return Point(self.center.x + p.x, self.center.y - p.y)
