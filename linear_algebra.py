from typing import List

Vector = List[float]


height_weight_age = [70, # Inches
                     170,   # pounds
                     40 ] # years

grades = [
    95,
    80,
    75,
    62
]

def  add(v:Vector, w:Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same lenght"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

def subtract(v: Vector, w: Vector) -> Vector:
    """Subracts corresponding elements"""
    assert len(v) == len(w), "vector must be the same lenght"
    return [v_i -w_i for v_i,w_i in zip(v,w)]

assert subtract([5,7,9],[4,5,6]) == [1,2,3]

def vector_sum(vectors: List[Vectors])