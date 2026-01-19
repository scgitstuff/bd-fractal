# TODO: should probably use Dataclasses


# does float make sense?
# I choose int because I think of points as representing pixels
# same as if I did a 2D array of pixels, like bit map


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"(x:{self.x}, y:{self.y})"

    def asTuple(self) -> tuple[int, int]:
        return (self.x, self.y)
