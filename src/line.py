from point import Point
import trig

"""
I'm using Line as if it were immutable
any time I need to re-size a line
just make a new one with getEndPoint()

"""


class Line:
    def __init__(self, start: Point, end: Point, width: int = 1):
        # TODO: fix this, it should be allowed
        if start.x == end.x and start.y == end.y:
            raise AssertionError("a Line cannot be a single Point")

        self.start = start
        self.end = end
        self.width = width
        self.length = trig.hypotenuse(end.x - start.x, end.y - start.y)
        self.angle = trig.calcAngle360(end.x - start.x, end.y - start.y)

    def __str__(self) -> str:
        return f"start:{self.start} end:{self.end} length:{round(self.length, 2)} angle:{self.angle}"
