from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from tkinter import colorchooser  # type: ignore
from line import Line
from point import Point
from params import Params, newParams, validate
from typing import Callable

# TODO: tkinter code is a bloated mess of repetitive shit


class Window:
    def __init__(self, root: Tk):
        self.p = newParams()
        self.doStuffCallBack = None
        self.root = root

        self._setupFrames()

    def _setupFrames(self):
        self.mainFrame = ttk.Frame(self.root)
        self.mainFrame.grid(column=0, row=0, sticky=NSEW)

        self.leftFrame = ttk.Frame(self.mainFrame)
        self.leftFrame.grid(column=0, row=0, sticky=NSEW)

        self.rightFrame = ttk.Frame(self.mainFrame)
        self.rightFrame.grid(column=1, row=0, sticky=NSEW)

    def setDoStuffCallBack(self, func: Callable[[], None] | None = None):
        self.doStuffCallBack = func

    def doStuff(self):
        # TODO: catch validation errors and display in UI
        validate(self.p)

        self._configCanvas()

        if self.doStuffCallBack is not None:
            self.doStuffCallBack()

    def createWidgets(self):
        self._fillLeftFrame()
        self._fillRightFrame()
        self._configCanvas()  # render defaults

    def _fillLeftFrame(self):
        self.canvas = Canvas(self.leftFrame)
        self.canvas.grid(column=0, row=0)

    def _fillRightFrame(self):
        self._canvasSettings(self.rightFrame, parentRow=0)
        self._spokeSettings(self.rightFrame, parentRow=1)
        self._branchSettings(self.rightFrame, parentRow=3)

        ttk.Button(
            self.rightFrame,
            text="Do Stuff",
            command=self.doStuff,
            padding=(10, 10, 10, 10),
        ).grid(column=0, row=4, columnspan=2)

        self._padKids(self.rightFrame)

    def _canvasSettings(self, parent: ttk.Frame | ttk.LabelFrame, parentRow: int):
        parent = ttk.LabelFrame(
            parent,
            borderwidth=2,
            relief="solid",
            text="Canvas settings",
        )
        parent.grid(column=0, row=parentRow, sticky=NSEW)

        ttk.Label(
            parent,
            text="Canvas size",
        ).grid(column=0, row=0, sticky=W)
        # TODO: detect screen height for max
        ttk.Spinbox(
            parent,
            from_=100,
            to=1000,
            width=6,
            textvariable=self.p.imageSize,
        ).grid(column=1, row=0, sticky=E)

        self._makeColorField(parent, self.p.backColor, "Background Color", row=1)
        self._makeColorField(parent, self.p.lineColor, "Line Color", row=2)

        self._padKids(parent)

    def _spokeSettings(self, parent: ttk.Frame | ttk.LabelFrame, parentRow: int):
        parent = ttk.LabelFrame(
            parent,
            borderwidth=2,
            relief="solid",
            text="Spoke settings",
        )
        parent.grid(column=0, row=parentRow, sticky=NSEW)

        ttk.Checkbutton(
            parent,
            text="Pause between spokes",
            variable=self.p.doSleep,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=0, columnspan=2, sticky=W)

        ttk.Label(parent, text="Angle of spokes").grid(column=0, row=1, sticky=W)
        ttk.Combobox(
            parent,
            width=4,
            textvariable=self.p.spokeAngle,
            values=Params.SpokeAngles,
            state="readonly",
        ).grid(column=1, row=1, sticky=E)

        self._padKids(parent)

    def _branchSettings(self, parent: ttk.Frame | ttk.LabelFrame, parentRow: int):
        parent = ttk.LabelFrame(
            parent,
            borderwidth=2,
            relief="solid",
            text="Branch settings",
        )
        parent.grid(column=0, row=parentRow, sticky=NSEW)

        ttk.Label(parent, text="Angle of branches 0-90").grid(column=0, row=0, sticky=W)
        ttk.Spinbox(
            parent,
            from_=0,
            to=90,
            width=4,
            textvariable=self.p.branchAngle,
        ).grid(column=1, row=0, sticky=E)

        ttk.Checkbutton(
            parent,
            text="Limit recursion",
            variable=self.p.doRecursionLimit,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=1, sticky=W)
        ttk.Spinbox(
            parent,
            from_=0,
            to=10,
            width=4,
            textvariable=self.p.recursionLimit,
        ).grid(column=1, row=1, sticky=E)

        ttk.Checkbutton(
            parent,
            text="Start branching at center",
            variable=self.p.doStartCenter,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=2, columnspan=2, sticky=W)

        ttk.Checkbutton(
            parent,
            text="Invert branch direction",
            variable=self.p.doInvert,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=3, columnspan=2, sticky=W)

        ttk.Label(parent, text="Dynamic branch spacing:").grid(
            column=0, row=4, columnspan=2, sticky=W
        )
        ttk.Label(parent, text="Branch count").grid(column=0, row=5, sticky=E)
        ttk.Spinbox(
            parent,
            from_=1,
            to=100,
            width=4,
            textvariable=self.p.branchCount,
        ).grid(column=1, row=5, sticky=W)
        ttk.Label(parent, text="Min branch spacing").grid(column=0, row=6, sticky=E)
        ttk.Spinbox(
            parent,
            from_=2,
            to=50,
            width=4,
            textvariable=self.p.minBranchSpacing,
        ).grid(column=1, row=6, sticky=W)

        ttk.Checkbutton(
            parent,
            text="Fixed branch spacing",
            variable=self.p.doFixedBranchSpacing,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=7, sticky=W)
        ttk.Spinbox(
            parent,
            from_=10,
            to=1000,
            width=4,
            textvariable=self.p.fixedBranchSpacing,
        ).grid(column=1, row=7, sticky=E)

        self._padKids(parent)

    def _configCanvas(self):
        imageSize = self.p.imageSize.get()

        self._center = Point(imageSize // 2, imageSize // 2)

        self.canvas.delete("all")
        self.canvas.configure(
            height=imageSize,
            width=imageSize,
            background=self.p.backColor.get(),
        )

    def _makeColorField(
        self, parent: ttk.Frame | ttk.LabelFrame, color: StringVar, label: str, row: int
    ):
        ttk.Button(
            parent,
            text=label,
            command=lambda: self._chooseColor(color),
        ).grid(column=0, row=row, sticky=W)

        backgroundField = ttk.Entry(parent, width=10, textvariable=color)
        backgroundField.grid(column=1, row=row, sticky=E)

    def _chooseColor(self, color: StringVar):
        colorCode = colorchooser.askcolor(color=color.get(), title="Choose color")
        if colorCode[1] is None:
            return
        color.set(colorCode[1])

    def _padKids(self, parent: ttk.Frame | ttk.LabelFrame, x: int = 5, y: int = 5):
        for child in parent.winfo_children():
            child.grid_configure(padx=x, pady=y)  # type: ignore

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
