import time
from tkinter import *  # type: ignore
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
from PIL import ImageGrab
from typing import Callable
from line import Line
from point import Point
from params import newParams, validate, saveParams
from widgets import Widgets


class Window:
    def __init__(self, root: Tk):
        self.p = newParams()
        self.w = Widgets(self.p)
        # TODO: need accurate number for max window
        self.p.maxHeight.set(root.winfo_screenheight() - 100)
        self.root = root
        self._doStuffHook = None

        self.mainFrame = ttk.Frame(self.root)
        self.mainFrame.grid(column=0, row=0, sticky=NSEW)

        self.leftFrame = ttk.Frame(self.mainFrame)
        self.leftFrame.grid(column=0, row=0, sticky=NSEW)

        self.rightFrame = ttk.Frame(self.mainFrame)
        self.rightFrame.grid(column=1, row=0, sticky=NSEW)

    def setDoStuffHook(self, func: Callable[[], None] | None):
        self._doStuffHook = func

    def createWidgets(self):
        if self._doStuffHook is not None:
            self.w.setDoStuffEvent(self.doStuffEvent)

        self.w.setSaveImageEvent(self.saveImageEvent)

        self.w.fillLeftFrame(self.leftFrame)
        self.w.fillRightFrame(self.rightFrame)
        self.w.configCanvas()  # render defaults

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def drawLine(self, line: Line, fillColor: str = ""):
        if fillColor == "":
            fillColor = self.p.lineColor.get()
        self.w.canvas.create_line(
            *self._offset(line.start).asTuple(),
            *self._offset(line.end).asTuple(),
            fill=fillColor,
            width=line.width,
        )

    def _offset(self, p: Point) -> Point:
        return Point(self.w.center.x + p.x, self.w.center.y - p.y)

    def doStuffEvent(self):
        # TODO: catch validation errors and display in UI
        validate(self.p)
        saveParams(self.p)

        self.w.configCanvas()

        if self._doStuffHook is not None:
            self._doStuffHook()

    # I kind of hate this
    # Canvas does not give an easy way to save content
    def saveImageEvent(self):
        self.root.withdraw()
        files = [("Image", "*.png")]
        file = asksaveasfilename(filetypes=files, defaultextension=".png")
        self.root.deiconify()
        self.redraw()

        if file == "":
            return

        # it was capturing the save dialog in the screen shot
        time.sleep(0.3)

        x0 = self.w.canvas.winfo_rootx()
        y0 = self.w.canvas.winfo_rooty()
        x1 = x0 + self.w.canvas.winfo_width()
        y1 = y0 + self.w.canvas.winfo_height()
        ImageGrab.grab().crop(  # pyright: ignore[reportUnknownMemberType]
            (x0, y0, x1, y1)
        ).save(file)
