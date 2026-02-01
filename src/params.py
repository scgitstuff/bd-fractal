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
    SpokeAngles = (
        "5",
        "10",
        "15",
        "20",
        "30",
        "45",
        "60",
        "72",
        "90",
        "120",
        "180",
        "0",
    )

    def __init__(self):
        self.imageSize = IntVar(value=800)
        self.maxHeight = IntVar(value=-1)

        self.lineColor = StringVar(value="white")
        self.backColor = StringVar(value="black")

        # Spoke settings *******************************

        # pause between spokes
        self.doSleep = BooleanVar(value=False)

        # had to change to string because ttk.Combobox
        self.spokeAngle = StringVar(value="30")

        self.spokeRandomColor = BooleanVar(value=False)

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
        self.minBranchSpacing = IntVar(value=3)

        # static branches, boring
        self.doFixedBranchSpacing = BooleanVar(value=False)
        self.fixedBranchSpacing = IntVar(value=20)


# TODO: this should be a factory, a classmethod
# but linter is giving me shit about return type
def newParams() -> Params:
    p = _load()

    if p is None:
        p = Params()

    validate(p)

    return p


def validate(p: Params):
    # height is set by Window, new Params object has no value
    # so skip validation if it is not set
    if p.maxHeight.get() != -1 and (
        p.imageSize.get() < 100 or p.imageSize.get() > p.maxHeight.get()
    ):
        raise AssertionError(
            f"image size '{p.imageSize.get()}' out of range 100 - {p.maxHeight.get()}"
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
        raise AssertionError(f"branch count {p.branchCount.get()} out of range 1 - 100")

    if p.minBranchSpacing.get() < 2 or p.minBranchSpacing.get() > 50:
        raise AssertionError(
            f"min branch spacing {p.minBranchSpacing.get()} out of range 2 - 50"
        )

    # lower numbers cause too deep recursion, hang
    if p.fixedBranchSpacing.get() < 10 or p.fixedBranchSpacing.get() > 1000:
        raise AssertionError(
            f"fixed branch spacing {p.fixedBranchSpacing.get()} out of range 10 - 1000"
        )


# TODO: load from file if it exists
def _load() -> Params | None:
    return None


# TODO: save to file
def saveParams(p: Params) -> None:
    return None


# could use this to make SpokeAngles
def _makeList() -> List[int]:
    l: List[int] = [0]

    for i in range(1, 360):
        if 360 % i == 0:
            print(i)

    return l


_ = _makeList
