from tkinter import *  # type: ignore
from tkinter import ttk
from tkinter import colorchooser
from typing import Callable
from params import Params
from point import Point


class Widgets:
    def __init__(self, p: Params):
        self._doStuff = None
        self._saveImage = None
        self.p = p
        self.center = Point()

    def setDoStuffEvent(self, func: Callable[[], None] | None):
        self._doStuff = func

    def setSaveImageEvent(self, func: Callable[[], None] | None):
        self._saveImage = func

    def fillLeftFrame(self, leftFrame: ttk.Frame):
        self.canvas = Canvas(leftFrame)
        self.canvas.grid(column=0, row=0)

    def fillRightFrame(self, rightFrame: ttk.Frame):

        if self._doStuff is None or self._saveImage is None:
            return

        self._canvasSettings(rightFrame, parentRow=0)
        self._spokeSettings(rightFrame, parentRow=1)
        self._branchSettings(rightFrame, parentRow=2)

        ttk.Button(
            rightFrame,
            text="Save image",
            command=self._saveImage,
        ).grid(column=0, row=3, sticky=W)

        ttk.Button(
            rightFrame,
            text="Do Stuff",
            command=self._doStuff,
            padding=(10, 10, 10, 10),
        ).grid(column=0, row=3, sticky=E)

        self._padKids(rightFrame)

    def configCanvas(self):
        imageSize = self.p.imageSize.get()
        self.center = Point(imageSize // 2, imageSize // 2)

        self.canvas.delete("all")
        self.canvas.configure(
            height=imageSize,
            width=imageSize,
            background=self.p.backColor.get(),
        )

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
        ttk.Spinbox(
            parent,
            from_=100,
            to=self.p.maxHeight.get(),
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

        ttk.Checkbutton(
            parent,
            text="Random color spokes",
            variable=self.p.spokeRandomColor,
            onvalue=True,
            offvalue=False,
        ).grid(column=0, row=2, columnspan=2, sticky=W)

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
