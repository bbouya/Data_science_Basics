from ast import Call
import imp
from pickletools import floatnl
from pydoc import importfile
from typing import List

from numpy import identity

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

def dot(v: Vector, w: Vector) -> float:
    """Computes v_1 * w_1 + .... + v_n*w_n """
    assert len(v) == len(w) , "Vectors must have the same len"
    return sum(v_i* w_i for v_i,w_i in zip(v,w))

assert dot([1,2,3],[4,5,6]) == 32 # 1*4 +2*5 +3*6

def sum_of_squares(v: Vector) -> float:
    """returns v_1 * v_1"""
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14 

import math 

def magnitude(v:Vector) -> float:
    """Returns the magnitude (or length) of v"""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3,4]) == 5


def distance(v:Vector, w:Vector) -> float:
    return magnitude(subtract(v,w))

# Anather type alias
Matrix = List[List[float]]

A = [[1,2,3],
     [4,5,6]]
B = [[1,2],
     [3,4],
     [5,6]]

from typing import Tuple

def shape(A: Matrix) -> Tuple[int,int]:
    """Returns (# of rows of A, # of columns of A"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row
    return num_rows, num_cols

assert shape([[1,2,3],[4,5,6]]) == [2,3]

def get_row(A:Matrix, i: int) -> Vector:
    """Returns the i-th row of A (as a Vector)"""
    return A[i] # A[i] is already the ith row

def get_column(A: Matrix, j:int) -> Vector:
    """Return the j*th column of A (as a vector)"""
    return [A_i[j] for A_i in A]

from typing import Callable

def make_matrix(num_rows: int, num_cols: int, entry_fn: Callable[[int,int], float]) -> Matrix:
    """Return a num_rows x num_cols matrix whose (i,j) -th entry is entry_fn(i,j)"""
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n: int) -> Matrix:
    """Return the n x n identity matrix"""
    return make_matrix(n,n, lambda i, j : 1 if i==j else 0)

assert identity_matrix(5) == [[1,0,0,0,0],
                                [0,1,0,0,0],
                                [0,0,1,0,0]
                                [0,0,0,1,0]
                                [0,0,0,0,1]]

data = [[70,170,40],
        [65,120,26],
        [77,250,19],
        # .........
        ]
