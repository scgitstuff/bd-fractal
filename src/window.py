from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from line import Line
from point import Point
from params import newParams


class Window:
    def __init__(self, root: Tk, title: str):
        # TODO: catch validation errors and display in UI
        self.p = newParams()
        self.root = root

        root.title(title)
        # root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)

        self._center = Point(self.p.imageSize.get() // 2, self.p.imageSize.get() // 2)

        self.canvas = Canvas(
            root,
            width=self.p.imageSize.get(),
            height=self.p.imageSize.get(),
            background=self.p.backColor.get(),
        )
        self.canvas.grid(column=0, row=0)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def drawLine(self, line: Line, fillColor: str = ""):
        if fillColor == "":
            fillColor = self.p.lineColor.get()
        self.canvas.create_line(
            *self._offset(line.start).asTuple(),
            *self._offset(line.end).asTuple(),
            fill=fillColor,
            width=line.width,
        )

    def _offset(self, p: Point) -> Point:
        return Point(self._center.x + p.x, self._center.y - p.y)
