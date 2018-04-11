__author__ = 'efiathieniti'
# Functions 
from typing import List
from itertools import islice
import numpy as np
Vector = List[float]


# text: holds the word
# holds the vector (values)
class Word:
    def __init__(self, text: str, vector: Vector) -> None:
        self.text = text
        self.vector = vector


#
# Evaluate cosine similarity
#

def vector_len(v: Vector) -> float:
    return np.sqrt(sum([x*x for x in v]))

def dot_product(v1: Vector, v2: Vector) -> float:
    assert len(v1) == len(v2)
    return sum([x*y for (x,y) in zip(v1, v2)])

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """
    Returns the cosine of the angle between the two vectors.
    Results range from -1 (very different) to 1 (very similar).
    """
    return dot_product(v1, v2) / (vector_len(v1) * vector_len(v2))




#### General python dict functions

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
