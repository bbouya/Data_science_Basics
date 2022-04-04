from turtle import Vec2D

from sklearn.cluster import k_means
from linear_algebra import Vector


def num_differences(v1: Vector, v2: Vector) -> int:
    assert len(v1) == len(v2)
    return len([x1 for x1,x2 in zip(v1,v2) if x1!=x2])

assert num_differences([1,2,3], [2,1,3]) == 2, 'number not equel to 2'
assert num_differences([1,2],[1,2]) == 0

def vector_equal(v1: Vector, v2:Vector) -> Vector:
    assert len(v1) == len(v2), 'the vectors not equal'
    return [x1 for x1,x2 in zip(v1,v2) if x1==x2]

assert vector_equal([1,2,3],[2,1,3]) == [3] , 'not equal'
assert vector_equal([1,2],[1,2]) == [1,2], 'not equal'

from typing import List
from linear_algebra import vector_mean
import random 
def cluster_means(k: int, 
                  inputs: List[Vector],
                  assignments: List[int]) -> List[Vector]:
    clusters = [[] for i in range(k)]
    for input, assignment in zip(inputs, assignments):
        clusters[assignment].append(input)
    
    #if a cluster is empty, just use a random point
    return [vector_mean(cluster) if cluster else random.choice(inputs) for cluster in clusters]

import itertools
import random
import tqdm 
from linear_algebra import squared_distance

class KMeans:
    def __init__(self, k: int) -> None:
        self.k = k                      # number of clusters
        self.means = None

    def classify(self, input: Vector) -> int:
        """return the index of the cluster closest to the input"""
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs: List[Vector]) -> None:
        # Start with random assignments
        assignments = [random.randrange(self.k) for _ in inputs]

        with tqdm.tqdm(itertools.count()) as t:
            for _ in t:
                # Compute means and find new assignments
                self.means = cluster_means(self.k, inputs, assignments)
                new_assignments = [self.classify(input) for input in inputs]

                # Check how many assignments changed and if we're done
                num_changed = num_differences(assignments, new_assignments)
                if num_changed == 0:
                    return

                # Otherwise keep the new assignments, and compute new means
                assignments = new_assignments
                self.means = cluster_means(self.k, inputs, assignments)
                t.set_description(f"changed: {num_changed} / {len(inputs)}")
