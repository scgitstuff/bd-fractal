from tkinter import BooleanVar, IntVar, StringVar
from typing import List

"""
the parameters used to tweak the behavior of first.py
"""


# using dataclass caused errors in tkinter creating IntVar...
# static members don't work, had to switch to normal class, constructor
# RuntimeError: Too early to create variable: no default root window


class Params:

    # this has to be limited to factors of 360, because calculations
    SpokeAngles = ("0", "15", "30", "45", "60", "75", "90", "120", "180")

    def __init__(self):
        self.imageSize = IntVar(value=800)

        self.lineColor = StringVar(value="white")
        self.backColor = StringVar(value="black")

        # pause between spokes
        self.doSleep = BooleanVar(value=True)

        # had to change to string because ttk.Combobox
        self.spokeAngle = StringVar(value="30")

        # Branch settings *******************************

        self.branchAngle = IntVar(value=30)

        # invert the direction of branches
        self.doInvert = BooleanVar(value=False)

        # Limit recursion depth
        self.doRecursionLimit = BooleanVar(value=False)
        self.recursionLimit = IntVar(value=2)

        # start at origin vs first interval
        self.doStartCenter = BooleanVar(value=False)

        # dynamic branches, default behavior
        self.branchCount = IntVar(value=6)
        self.minBranchInterval = IntVar(value=3)

        # static branches, boring
        self.doFixedBranchInterval = BooleanVar(value=False)
        self.branchInterval = IntVar(value=20)


# TODO: this should be a factory, a classmethod
# but linter is giving me shit about return type
def newParams() -> Params:
    p = _load()

    validate(p)

    return p


def validate(p: Params):

    # TODO: resolution dependent max
    if p.imageSize.get() < 100 or p.imageSize.get() > 1000:
        raise AssertionError(
            f"image size '{p.imageSize.get()}' out of range 100 - 1000"
        )

    if p.backColor.get() == p.lineColor.get():
        raise AssertionError("line and background colors cannot be the same")

    if p.spokeAngle.get() not in Params.SpokeAngles:
        raise AssertionError(
            f"spoke angle {p.spokeAngle.get()} not in list: {Params.SpokeAngles}"
        )

    if p.branchAngle.get() < 0 or p.branchAngle.get() > 90:
        raise AssertionError(f"branch angle {p.branchAngle.get()} out of range 0 - 90")

    if p.recursionLimit.get() < 0 or p.recursionLimit.get() > 10:
        raise AssertionError(
            f"recursion limit {p.recursionLimit.get()} out of range 0 - 10"
        )

    if p.branchCount.get() < 1 or p.branchCount.get() > 100:
        raise AssertionError(
            f"branch interval {p.branchCount.get()} out of range 1 - 100"
        )

    if p.minBranchInterval.get() < 2 or p.minBranchInterval.get() > 50:
        raise AssertionError(
            f"branch interval {p.minBranchInterval.get()} out of range 2 - 50"
        )

    # lower numbers cause too deep recursion, hang
    if p.branchInterval.get() < 10 or p.branchInterval.get() > 1000:
        raise AssertionError(
            f"branch interval {p.branchInterval.get()} out of range 10 - 1000"
        )


# TODO: load from file if it exists
# otherwise new instance with defaults
def _load() -> Params:
    p = Params()

    return p


# TODO: save to file
# TODO: call from UI when it has buttons to do stuff
def saveParams(p: Params):
    pass


# TODO: could use this to make SpokeAngles better
def makeList() -> List[int]:
    l: List[int] = [0]

    for i in range(1, 360):
        if 360 % i == 0:
            print(i)

    return l
