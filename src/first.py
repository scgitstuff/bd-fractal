from tkinter import *  # type: ignore
from tkinter import ttk  # type: ignore
from window import Window
from point import Point
from line import Line
import trig
import time
import random
import math

_branchColor = [
    "white",
    "red",
    "green",
    "purple",
]


# I switched to a class is for the callback function for the button event in the UI
class First:
    def __init__(self, win: Window):
        self.win = win

    def drawSpokes(self) -> None:
        length = self.win.p.imageSize.get() // 2
        # because end branches were being clipped
        length = round(length * 0.9)

        start = Point(0, 0)
        endPoints: list[Point] = self._getEndPoints(
            start, int(self.win.p.spokeAngle.get()), length
        )

        for end in endPoints:
            self.win.redraw()

            line = Line(start, end)
            self._drawBranches(line, 0)

            if self.win.p.doSleep.get():
                time.sleep(0.1)

    def _drawBranches(self, origin: Line, recursionLevel: int):
        p = self.win.p

        # some color stuff I started playing with
        color = "blueviolet"
        color = self._randomColor()
        color = _branchColor[recursionLevel % len(_branchColor)]
        _ = color

        if p.doRecursionLimit.get() and recursionLevel > p.recursionLimit.get():
            return
        recursionLevel += 1

        self.win.drawLine(origin, p.lineColor.get())

        originLength = math.ceil(origin.length)
        if p.doFixedBranchInterval.get():
            branchInterval = p.branchInterval.get()
        else:
            branchInterval = originLength // p.branchCount.get()
            if branchInterval < p.minBranchInterval.get():
                return

        # where to start branching
        # TODO: would like to expose this
        intervalMultiplier = 1
        if p.doStartCenter.get():
            intervalMultiplier = 0

        lineLength = originLength
        while lineLength >= branchInterval:

            # the branch has to shrink, otherwise infinite recursion
            # magic number 3 makes a size I like
            # TODO: may want to expose this
            branchlen = lineLength // 3
            if branchlen < 2:
                break

            lineConsumed = branchInterval * intervalMultiplier
            lineLength = originLength - lineConsumed
            intervalMultiplier += 1

            branchStartPoint = trig.getEndPoint(
                origin.start, origin.angle, lineConsumed
            )

            x = p.branchAngle.get()
            if p.doInvert.get():
                x = 180 - x

            rightLine = Line(
                branchStartPoint,
                trig.getEndPoint(branchStartPoint, origin.angle - x, branchlen),
            )
            leftLine = Line(
                branchStartPoint,
                trig.getEndPoint(branchStartPoint, origin.angle + x, branchlen),
            )

            self._drawBranches(rightLine, recursionLevel)
            self._drawBranches(leftLine, recursionLevel)

    def _randomColor(self) -> str:
        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        color = f"#{red}{green}{blue}"

        return color

    def _getEndPoints(self, start: Point, spokeAngle: int, length: int) -> list[Point]:
        endPoints: list[Point] = []

        # if you only want 1 spoke, avoid divide by 0
        if spokeAngle == 0:
            spokeAngle = 360

        isValidAngle = 360 % spokeAngle == 0
        if not isValidAngle:
            raise AssertionError("spoke angle must be a factor of 360")

        count = 360 // spokeAngle

        for i in range(count):
            endPoints.append(trig.getEndPoint(start, i * spokeAngle, length))

        return endPoints


def doStuff():
    root = Tk()
    root.title("bd-fractal first algorithm")

    win = Window(root)
    f = First(win)
    win.setDoStuffCallBack(f.drawSpokes)
    win.createWidgets()
    win.doStuff()

    root.mainloop()
