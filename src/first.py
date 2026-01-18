from window import Window
from point import Point
from line import Line, getEndPoint
import time


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
        win.redraw()
        line = Line(start, end)
        # drawBranchesConstant(win, line)
        drawBranches(win, line)
        time.sleep(0.1)


def drawBranchesConstant(win: Window, origin: Line):

    win.drawLine(origin)

    angle = 45
    branchInterval = 20
    doStartCenter = False

    line = origin
    while line.length >= branchInterval:

        # the branch has to shrink, otherwise infinite recursion
        branchlen = line.length // 3
        if branchlen < 2:
            break

        branchStartPoint = line.start
        if not doStartCenter:
            branchStartPoint = getEndPoint(line.start, line.angle, branchInterval)

        x = angle
        # to invert direction
        # x = 180 - angle

        rightLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle - x, branchlen),
        )
        leftLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle + x, branchlen),
        )

        drawBranchesConstant(win, rightLine)
        drawBranchesConstant(win, leftLine)

        if doStartCenter:
            branchStartPoint = getEndPoint(line.start, line.angle, branchInterval)

        # if you end up with a single point Line, not a problem, just means I'm done
        try:
            line = Line(branchStartPoint, origin.end)
        except:
            break


def drawBranches(win: Window, origin: Line):

    win.drawLine(origin)

    # TODO: I want to make these variables a params struct passed in by UI
    angle = 45
    # density - number of branches per line
    branchCount = 8
    # density - space between branches
    branchInterval = origin.length // branchCount
    # limit branch density, have to have space between branches, or it looks like shit
    minBranchSpace = 3
    # invert the direction of branches; I do not like the look
    doInvert = False
    # start at origin vs first interval
    doStartCenter = False

    if branchInterval < minBranchSpace:
        return

    line = origin
    while line.length >= branchInterval:

        # the branch has to shrink, otherwise infinite recursion
        branchlen = line.length // 3
        # have to be at least 2; a little higher seems to filter out some noise
        # otherwise you try to create a line that is 1 point
        if branchlen < 2:
            break

        branchStartPoint = line.start
        if not doStartCenter:
            branchStartPoint = getEndPoint(line.start, line.angle, branchInterval)

        x = angle
        if doInvert:
            x = 180 - angle

        rightLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle - x, branchlen),
        )
        leftLine = Line(
            branchStartPoint,
            getEndPoint(branchStartPoint, line.angle + x, branchlen),
        )

        drawBranches(win, rightLine)
        drawBranches(win, leftLine)

        if doStartCenter:
            branchStartPoint = getEndPoint(line.start, line.angle, branchInterval)

        # if you end up with a single point Line, not a problem, just means I'm done
        try:
            line = Line(branchStartPoint, origin.end)
        except:
            break
