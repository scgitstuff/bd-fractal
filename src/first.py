from window import Window
from point import Point
from line import Line, getEndPoint


"""
find a point on the line to start branches
use existing angle +- 45 for branches
have to add calculated end point to branch start point to get absolute point

cos(x) = b / h


pass line into recursive function
    move 5, make that next origin
    call left & right with half length
    45 degree angle
    stop when len < 5
it should be like a pinwheel of christmas trees

"""


def doStuff(win: Window, origin: Line):

    win.drawLine(origin)
    # print(f"Origin: {origin}")

    if origin.length < 6:
        return

    # I want to work with degrees
    angle = 45

    # split line into X parts
    # each part having branches decreasing in length

    branchCount = 5
    branchStart = origin.length // branchCount

    # i = 0
    # line: Line = origin
    # while i < branchCount:

    # branches are a fraction of the length of the starting line
    branchlen = origin.length // 3

    branchStartPoint = getEndPoint(origin.start, origin.angle, branchStart)

    rightLine = Line(
        branchStartPoint,
        getEndPoint(branchStartPoint, origin.angle - angle, branchlen),
    )
    leftLine = Line(
        branchStartPoint,
        getEndPoint(branchStartPoint, origin.angle + angle, branchlen),
    )

    # line = Line(branchStartPoint, origin.end)
    # i += 1

    # print(f"Right: {rightLine}")
    win.drawLine(rightLine)
    # doStuff(win, rightLine)

    # print(f"Left: {leftLine}")
    win.drawLine(leftLine)
    # doStuff(win, leftLine)


def getLine(origin: Point) -> Line:

    p = Point(origin.x, origin.y)

    return Line(origin, p)


def getNext(parent: Line) -> tuple[int, int]:

    return (0, 0)
