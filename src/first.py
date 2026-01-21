import math
from window import Window
from point import Point
from line import Line
from settings import Params, getParams
import trig
import time
import random

_branchColor = [
    "white",
    "red",
    "green",
    "purple",
]


# TODO: the UI should have all the settings as radio/check and spin
# with buttons to launch a separate window for the image and save
def doStuff():
    # print("Hello from bd-fractal!")

    p = getParams()
    # TODO: move size to settings
    win = Window(500, 500, "bd-fractal first algorithm", p.backColor)
    length = (win.height // 2) - 25  # end branches were being clipped
    start = Point(0, 0)
    endPoints: list[Point] = _getEndPoints(start, p.spokeAngle, length)

    for end in endPoints:
        win.redraw()

        line = Line(start, end)
        _drawBranches(p, win, line, 0)

        if p.doSleep:
            time.sleep(0.1)

    win.wait()


def _drawBranches(p: Params, win: Window, origin: Line, recursionLevel: int):

    # TODO: some color stuff I was playing with
    color = "blueviolet"
    color = _randomColor()
    color = _branchColor[recursionLevel % len(_branchColor)]
    _ = color

    if p.doRecursionLimit and recursionLevel > p.recursionLimit:
        return
    recursionLevel += 1

    win.drawLine(origin, p.lineColor)

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

        _drawBranches(p, win, rightLine, recursionLevel)
        _drawBranches(p, win, leftLine, recursionLevel)


def _randomColor() -> str:
    red = "%02x" % random.randint(0, 255)
    green = "%02x" % random.randint(0, 255)
    blue = "%02x" % random.randint(0, 255)
    color = f"#{red}{green}{blue}"
    # color = "white"
    # print(color)

    return color


def _getEndPoints(start: Point, angle: int, length: int) -> list[Point]:
    endPoints: list[Point] = []

    isValidAngle = 360 % angle == 0
    if not isValidAngle:
        raise AssertionError("angle must be a factor of 360")

    count = 360 // angle

    for i in range(count):
        endPoints.append(trig.getEndPoint(start, i * angle, length))

    return endPoints
