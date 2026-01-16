from point import Point
import math
import numpy


"""
for this code Line is the hypotenuse of a right triangle
on a coordinate plane over the canvas
I started with 2 Points, as I get further I need more info
I'm having a problem drawing branches, the angle calculations 
are still off
"""


class Line:
    def __init__(self, start: Point, end: Point):
        isRetard = start.x == 0 and start.y == 0 and end.x == 0 and end.y == 0
        # TODO: this assert alway executes.  Why?
        # assert isRetard, "fuck off with your zeros"
        if isRetard:
            raise AssertionError("fuck off with your zeros")

        self.start = start
        self.end = end
        self.base = end.x - start.x
        self.opp = end.y - start.y
        self.length = _hypotenuse(self.base, self.opp)
        self.angle = lineAngle(self.base, self.opp)

    def __str__(self) -> str:
        return (
            f"start:{self.start} end:{self.end} length:{self.length} angle:{self.angle}"
        )


def getEndPoint(start: Point, angle: int, length: int) -> Point:
    # x calculation
    x = length * math.cos(math.radians(angle))
    # offset from wherever the line started
    x = round(x) + start.x

    y = length * math.sin(math.radians(angle))
    y = round(y) + start.y

    end = Point(x, y)

    return end


# I could use __len__ instead
# but I hate any kind of operator overload functions
# because they hide code, I prefer explicit
def _hypotenuse(base: int, opp: int) -> int:
    h = base**2 + opp**2
    h = round(math.sqrt(h))

    return h


def lineAngle(base: int, opp: int) -> int:
    """ """
    # divide by 0 and undefined tan
    if base == 0:
        if opp > 0:
            return 90
        if opp < 0:
            return -90

    x = theta(base, opp)

    return x


def lineAngleCircle(base: int, opp: int) -> int:
    """
    translate angle to 360
    """
    # divide by 0 and undefined tan
    if base == 0:
        if opp > 0:
            return 90
        if opp < 0:
            return 270
    if opp == 0:
        if base > 0:
            return 0
        if base < 0:
            return 180

    x = theta(base, opp)

    # Q1
    if base > 0 and opp > 0:
        return x

    # Q2
    if base < 0 and opp > 0:
        return 180 - abs(x)

    # Q3
    if base < 0 and opp < 0:
        return 180 + abs(x)

    # Q4
    if base > 0 and opp < 0:
        return 360 - abs(x)

    # this will never execute, but Pylance cries about it
    return x


def theta(base: int, opp: int):
    x = numpy.arctan(opp / base)
    x = math.degrees(x)
    x = round(x)

    return x
