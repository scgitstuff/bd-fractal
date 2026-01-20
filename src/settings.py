from dataclasses import dataclass

# from collections import namedtuple

"""
this file will be the parameters used to tweak the behavior of first.py

start with the defaults that I like
then add code to save/load from a file to remember user changes
"""

# TODO: look into
# @dataclass(frozen=True)


@dataclass(kw_only=True)
class Params:

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
    recursionLimit = 3

    lineColor = "white"
    # lineColor = "blueviolet"
    backColor = "black"


def getParams() -> Params:
    p = _load()
    _validate(p)

    return p


# TODO: add all the range checks for each param
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


# TODO: the crap below is some stuff I want to look into, not real code


# @dataclass
# class Point:
#     x: float
#     y: float
#     z: float = 0.0


# p = Point(1.5, 2.5)
# print(p)  # Point(x=1.5, y=2.5, z=0.0)


# # this is garbage
# MyStruct = namedtuple("MyStruct", ["field1", "field2", "field3"])  # type: ignore
# m = MyStruct("foo", "bar", "baz")
# m = MyStruct(field1="foo", field2="bar", field3="baz")
