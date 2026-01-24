from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from line import Line
from point import Point


class Window:
    def __init__(
        self,
        root: Tk,
        width: int,
        height: int,
        title: str = "Fractal",
        background: str = "white",
    ):
        self.root = root

        self._center = Point(width // 2, height // 2)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.title(title)

        self.canvas = Canvas(
            root,
            width=width,
            height=height,
            background=background,
        )
        self.canvas.grid(column=0, row=0)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def drawLine(self, line: Line, fillColor: str = "black"):
        self.canvas.create_line(
            *self._offset(line.start).asTuple(),
            *self._offset(line.end).asTuple(),
            fill=fillColor,
            width=line.width,
        )

    def _offset(self, p: Point) -> Point:
        return Point(self._center.x + p.x, self._center.y - p.y)
