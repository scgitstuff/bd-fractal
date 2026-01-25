from tkinter import IntVar, StringVar

"""
the parameters used to tweak the behavior of first.py
"""


# TODO: each field comment needs to be put into _validate()
# TODO: using dataclass caused errors in tkinter creating IntVar
# had to switch to normal class, constructor
# TODO: finish converting fields, did a few POC first pass
# TODO: I hate the coupling
# setting up the UI left me with 2 choices
# either use the tkinter data classes that bind to UI elements
# or duplicate the structure and write a bridge to copy all the values
# out of UI into primitives; both suck
class Params:
    def __init__(self):
        # hard min, resolution dependent max
        self.imageSize = IntVar(value=800)

        # lineColor = "red"
        # lineColor = "blueviolet"
        self.lineColor = StringVar(value="white")
        self.backColor = StringVar(value="black")

        # pause between spokes
        self.doSleep = True

        # limit this to 15-90 in 15 degree increments
        # also valid edge cases 0, 180, 120 for 1, 2, or 3 spokes
        self.spokeAngle = 30

        # Branch settings *******************************

        # limit this to 0-90 in 5 degree increments
        self.branchAngle = 30

        # Limit recursion depth
        self.doRecursionLimit = False
        self.recursionLimit = 2

        # dynamic branches, default behavior
        self.branchCount = 6
        self.minBranchInterval = 3
        # static branches, boring
        self.doFixedBranchInterval = False
        self.branchInterval = 20

        # invert the direction of branches
        self.doInvert = False

        # start at origin vs first interval
        self.doStartCenter = False


def getParams() -> Params:
    p = _load()

    _validate(p)

    return p


def _validate(p: Params):
    if p.backColor.get() == p.lineColor.get():
        raise AssertionError("line and background colors cannot be the same")


# TODO: load from file
def _load() -> Params:
    p = Params()

    return p


# TODO: save to file
# TODO: call from UI when it has buttons to do stuff
def setParams(p: Params):
    pass
