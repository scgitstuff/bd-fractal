from window import Window
from point import Point
from line import Line, getEndPoint


"""
it should be like a pinwheel of christmas trees


"""


def doStuff(win: Window, start: Point, length: int):

    endPoints: list[Point] = []

    # Q1
    endPoints.append(getEndPoint(start, 0, length))
    endPoints.append(getEndPoint(start, 30, length))
    endPoints.append(getEndPoint(start, 60, length))
    # endPoints.append(getEndPoint(start, 45, length))
    endPoints.append(getEndPoint(start, 90, length))

    # Q2
    endPoints.append(getEndPoint(start, 120, length))
    endPoints.append(getEndPoint(start, 150, length))
    # endPoints.append(getEndPoint(start, 135, length))
    endPoints.append(getEndPoint(start, 180, length))

    # Q3
    endPoints.append(getEndPoint(start, 210, length))
    endPoints.append(getEndPoint(start, 240, length))
    # endPoints.append(getEndPoint(start, 225, length))
    endPoints.append(getEndPoint(start, 270, length))

    # Q4
    endPoints.append(getEndPoint(start, 300, length))
    endPoints.append(getEndPoint(start, 330, length))
    # endPoints.append(getEndPoint(start, 315, length))

    for end in endPoints:
        line = Line(start, end)
        drawBranches(win, line)


def drawBranches(win: Window, origin: Line):

    win.drawLine(origin)
    # print(f"Origin: {origin}")

    if origin.length < 6:
        return

    angle = 45
    branchCount = 8
    branchInterval = origin.length // branchCount
    if branchInterval < 2:
        return

    i = 0
    line = origin
    while True:

        branchlen = line.length // 3
        # have to be at least 2
        # otherwise you try to create a line that is 1 point, crash stuff
        if branchlen < 2:
            break

        branchStartPoint = getEndPoint(line.start, line.angle, branchInterval)

        rightLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle - angle, branchlen),
        )
        leftLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle + angle, branchlen),
        )

        # print(f"Right: {rightLine}")
        # win.drawLine(rightLine)
        drawBranches(win, rightLine)

        # print(f"Left: {leftLine}")
        # win.drawLine(leftLine)
        drawBranches(win, leftLine)

        i += 1
        if i >= branchCount:
            break

        line = Line(branchStartPoint, origin.end)
