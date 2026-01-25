from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from line import Line
from point import Point
from settings import getParams


class Window:
    def __init__(self, root: Tk, title: str):
        # TODO: catch validation errors and display in UI
        self.params = getParams()
        self.root = root

        root.title(title)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        self._center = Point(
            self.params.imageSize.get() // 2, self.params.imageSize.get() // 2
        )

        self.canvas = Canvas(
            root,
            width=self.params.imageSize.get(),
            height=self.params.imageSize.get(),
            background=self.params.backColor.get(),
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
