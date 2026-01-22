from dataclasses import dataclass

# from collections import namedtuple

"""
the parameters used to tweak the behavior of first.py
"""


# TODO: each field comment needs to be put into _validate()
@dataclass(kw_only=True)
# @dataclass(frozen=True)
class Params:

    # hard min, resolution dependent max
    imageSize = 800

    # limit this to 15-90 in 15 degree increments
    spokeAngle = 30
    # limit this to 0-90 in 5 degree increments
    branchAngle = 30

    # dynamic branches, default behavior
    branchCount = 6
    minBranchInterval = 3

    # static branches, boring
    doFixedBranchInterval = False
    branchInterval = 20

    # invert the direction of branches
    doInvert = False
    # start at origin vs first interval
    doStartCenter = False
    # pause between spokes
    doSleep = True

    # Limit recursion depth
    doRecursionLimit = False
    recursionLimit = 2

    lineColor = "white"
    # lineColor = "blueviolet"
    backColor = "black"


def getParams() -> Params:
    p = _load()
    _validate(p)

    return p


def _validate(p: Params):
    if p.backColor == p.lineColor:
        raise AssertionError("line and background colors cannot be the same")


# TODO: load from file
def _load() -> Params:
    p = Params()

    return p


# TODO: save to file
# TODO: call from UI when it has buttons to do stuff
def setParams(p: Params):
    pass
