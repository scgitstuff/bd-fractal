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


# TODO: the UI should have all the settings as radio/check, spinbox, input
# with buttons to render the image and save it
# not sure if it will render in a separate window or not
def doStuff():

    root = Tk()

    win = Window(root, "bd-fractal first algorithm")
    length = (win.p.imageSize.get() // 2) - 25  # end branches were being clipped
    start = Point(0, 0)
    endPoints: list[Point] = _getEndPoints(start, win.p.spokeAngle, length)

    for end in endPoints:
        win.redraw()

        line = Line(start, end)
        _drawBranches(win, line, 0)

        if win.p.doSleep:
            time.sleep(0.1)

    # win.wait()

    root.mainloop()


def _drawBranches(win: Window, origin: Line, recursionLevel: int):
    # TODO: I used to pass this in, didn't feel like refactoring usage yet
    p = win.p

    # TODO: some color stuff I started playing with
    color = "blueviolet"
    color = _randomColor()
    color = _branchColor[recursionLevel % len(_branchColor)]
    _ = color

    if p.doRecursionLimit and recursionLevel > p.recursionLimit:
        return
    recursionLevel += 1

    win.drawLine(origin, p.lineColor.get())

    originLength = math.ceil(origin.length)
    if p.doFixedBranchInterval:
        branchInterval = p.branchInterval
    else:
        branchInterval = originLength // p.branchCount
        if branchInterval < p.minBranchInterval:
            return

    # where to start branching
    # TODO: would like to expose this
    intervalMultiplier = 1
    if p.doStartCenter:
        intervalMultiplier = 0

    lineLength = originLength
    while lineLength >= branchInterval:

        branchlen = lineLength // 3
        # the branch has to shrink, otherwise infinite recursion
        if branchlen < 2:
            break

        lineConsumed = branchInterval * intervalMultiplier
        lineLength = originLength - lineConsumed
        intervalMultiplier += 1

        branchStartPoint = trig.getEndPoint(origin.start, origin.angle, lineConsumed)

        x = p.branchAngle
        if p.doInvert:
            x = 180 - p.branchAngle

        rightLine = Line(
            branchStartPoint,
            trig.getEndPoint(branchStartPoint, origin.angle - x, branchlen),
        )
        # print(f"rightLine: {rightLine}")
        leftLine = Line(
            branchStartPoint,
            trig.getEndPoint(branchStartPoint, origin.angle + x, branchlen),
        )
        # print(f"leftLine:  {leftLine}")

        # if rightLine.length != leftLine.length:
        #     print(f"{origin.angle} : {rightLine.length} vs {leftLine.length}")

        _drawBranches(win, rightLine, recursionLevel)
        _drawBranches(win, leftLine, recursionLevel)


def _randomColor() -> str:
    red = "%02x" % random.randint(0, 255)
    green = "%02x" % random.randint(0, 255)
    blue = "%02x" % random.randint(0, 255)
    color = f"#{red}{green}{blue}"

    return color


def _getEndPoints(start: Point, spokeAngle: int, length: int) -> list[Point]:
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
