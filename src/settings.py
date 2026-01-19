from dataclasses import dataclass
from collections import namedtuple

"""
this file will be the parameters used to tweak the behavior of first
I want to have defaults the way I like, then create/save settings on use to remember

the crap below is some stuff I want to look into, not real code
"""

# TODO: look into using these
# @dataclass(frozen=True)
# @dataclass(kw_only=True)


@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0


p = Point(1.5, 2.5)
print(p)  # Point(x=1.5, y=2.5, z=0.0)


# this is garbage
MyStruct = namedtuple("MyStruct", ["field1", "field2", "field3"])  # type: ignore
m = MyStruct("foo", "bar", "baz")
m = MyStruct(field1="foo", field2="bar", field3="baz")
