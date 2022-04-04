from turtle import Vec2D
from linear_algebra import Vector


def num_differences(v1: Vector, v2: Vector) -> int:
    assert len(v1) == len(v2)
    return len([x1 for x1,x1 in zip(v1,v2) if x1!=x2])

