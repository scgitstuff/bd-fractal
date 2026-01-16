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
    print(f"Origin: {origin}")

    if origin.length < 6:
        return

    # I want to work with degrees, because radians suck
    angle = 45

    # shorter line for branches
    branchlen = origin.length // 3
    # start branches away from origin
    branchStart = origin.length // 10

    branchStartPoint = getEndPoint(origin.start, origin.angle, branchStart)
    rightLine = Line(
        branchStartPoint,
        getEndPoint(branchStartPoint, origin.angle - angle, branchlen),
    )
    leftLine = Line(
        branchStartPoint,
        getEndPoint(branchStartPoint, origin.angle + angle, branchlen),
    )

    print(f"Right: {rightLine}")
    win.drawLine(rightLine)
    # doStuff(win, rightLine)

    print(f"Left: {leftLine}")
    win.drawLine(leftLine)
    # doStuff(win, leftLine)


def getLine(origin: Point) -> Line:

    p = Point(origin.x, origin.y)

    return Line(origin, p)


def getNext(parent: Line) -> tuple[int, int]:

    return (0, 0)
