from window import Window
from point import Point
from line import Line, getEndPoint
import time
import random

branchColor = [
    "white",
    "red",
    "green",
    "purple",
]


def doStuff():
    # print("Hello from bd-fractal!")
    win = Window(800, 800, "Hello from bd-fractal!", "black")
    length = (win.height // 2) - 25  # end branches were being clipped
    start = Point(0, 0)
    spokeAngle = 30
    endPoints: list[Point] = _getEndPoints(start, spokeAngle, length)

    for end in endPoints:
        win.redraw()

        line = Line(start, end)
        color = _randomColor()
        color = "white"
        _drawDynamicBranches(win, line, 0, color)

        # TODO: make this an option in UI
        time.sleep(0.1)

    win.wait()


def _drawDynamicBranches(
    win: Window, origin: Line, level: int = 0, color: str = "white"
):
    # color = "blueviolet"
    # color = _randomColor()
    # color = branchColor[level % len(branchColor)]
    level += 1

    win.drawLine(origin, color)

    # TODO: I want to make these variables a params struct passed in by UI
    branchAngle = 30

    # density - number of branches per line
    branchCount = 6
    # density - space between branches
    branchInterval = origin.length // branchCount
    # limit branch density, have to have space between branches, or it looks like shit
    minBranchSpace = 3
    # override for fixed version that I like less
    # branchInterval = 20

    # invert the direction of branches
    doInvert = False
    # start at origin vs first interval
    doStartCenter = False

    # where to start branching
    intervalMultiplier = 1
    if doStartCenter:
        intervalMultiplier = 0

    if branchInterval < minBranchSpace:
        return

    lineLength = origin.length

    while lineLength >= branchInterval:

        branchlen = lineLength // 3
        # the branch has to shrink, otherwise infinite recursion
        if branchlen < 2:
            break

        lineConsumed = branchInterval * intervalMultiplier
        lineLength = origin.length - lineConsumed
        intervalMultiplier += 1

        branchStartPoint = getEndPoint(origin.start, origin.angle, lineConsumed)

        x = branchAngle
        if doInvert:
            x = 180 - branchAngle

        rightLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, origin.angle - x, branchlen),
        )
        leftLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, origin.angle + x, branchlen),
        )

        _drawDynamicBranches(win, rightLine, level, color)
        _drawDynamicBranches(win, leftLine, level, color)


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
        endPoints.append(getEndPoint(start, i * angle, length))

    return endPoints
