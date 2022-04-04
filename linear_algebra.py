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

def vector_sum(vectors: List[Vector])-> Vector:
    """Sums all corresponding elements"""
    # CHeck that vectors is not empty
    assert vectors, "no verctors provided"
    # CHeck the vectors are all the same size
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes."
    # the i-th element of the result is the sum of every vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]

def scalar_multiply(c: float , v:Vector) -> Vector:
    """Multiplies every element by c"""
    return [c * v_i for v_i in v]

assert scalar_multiply(2,[1,2,3]) == [2,4,6],'ayoub'

def vector_mean(vectors: List[Vector]) -> Vector:
    """Computer the element-wise average"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

