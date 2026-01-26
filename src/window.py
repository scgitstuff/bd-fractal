from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from line import Line
from point import Point
from params import newParams
from typing import Callable


# TODO: add button to save image
class Window:
    def __init__(self, root: Tk, title: str):
        # TODO: catch validation errors and display in UI
        self.p = newParams()
        self.callBack = None
        self.root = root
        root.title(title)

    def setCallBack(self, func: Callable[[], None] | None = None):
        self.callBack = func

    def createStuff(self):
        imageSize = self.p.imageSize.get()
        self._center = Point(imageSize // 2, imageSize // 2)
        self.canvas = Canvas(
            self.root,
            width=imageSize,
            height=imageSize,
            background=self.p.backColor.get(),
        )
        self.canvas.grid(column=0, row=0)

        if self.callBack is not None:
            self.callBack()

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
