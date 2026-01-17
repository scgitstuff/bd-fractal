from point import Point
import math
import numpy

"""
at first I'm using Line as if it were immutable
any time I need to re-size a line, just make a new one with getEndPoint()
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
        self.length = _hypotenuse(end.x - start.x, end.y - start.y)
        self.angle = lineAngleCircle(end.x - start.x, end.y - start.y)

    def __str__(self) -> str:
        return (
            f"start:{self.start} end:{self.end} length:{self.length} angle:{self.angle}"
        )


def getEndPoint(start: Point, angle: int, length: int) -> Point:
    """
    this is effectively another constructor, because Python blows

    I'm not returning a line because the initial use was to find a
    point at given length along an existing line
    """

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


# def _lineAngle(base: int, opp: int) -> int:
#     """ """
#     # divide by 0 and undefined tan
#     if base == 0:
#         if opp > 0:
#             return 90
#         if opp < 0:
#             return -90

#     x = _theta(base, opp)

#     return x


def lineAngleCircle(base: int, opp: int) -> int:
    """
    translate angle to 360
    this is the only way I could get my head around it
    it makes the angle calculation for branches simple
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

    x = _theta(base, opp)

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


def _theta(base: int, opp: int):
    x = numpy.arctan(opp / base)
    x = math.degrees(x)
    x = round(x)

    return x
