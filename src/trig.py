from point import Point
import math
import numpy


def getEndPoint(start: Point, angle: int, length: int) -> Point:
    """
    :param length:
        this is more of a requested length
        the Line constructor will calculate the real value
    """

    # special case needed for branches as they shrink
    if length <= 0:
        return start

    angle = angle % 360

    # float problems, 0.5 -> 0.444444444444444449
    # had to round precision, I arbitrarily picked 8
    # sometimes the y coordinate was off
    # manifest as the left branch being shorter than right

    # x calculation
    x = length * round(math.cos(math.radians(angle)), 8)
    # offset from wherever the line started
    x = round(x) + start.x

    y = length * round(math.sin(math.radians(angle)), 8)
    y = round(y) + start.y

    return Point(x, y)


def hypotenuse(base: int, opp: int) -> float:
    h = base**2 + opp**2
    h = math.sqrt(h)
    h = round(h, 4)

    return h


# I want to work with degrees not radians
def calcAngle360(base: int, opp: int) -> int:
    """
    calculate angle of hypotenuse
    translate it to 360
    """

    if base == 0 and opp == 0:
        raise AssertionError("no angle possible")

    # divide by 0
    if base == 0:
        if opp > 0:
            return 90
        if opp < 0:
            return 270
    # undefined tan
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


def theta(base: int, opp: int) -> int:
    """
    calculate angle of hypotenuse and base
    """

    if base == 0:
        raise AssertionError("stop passing bad stuff")

    x = numpy.arctan(opp / base)
    x = math.degrees(x)
    x = round(x)

    return x
