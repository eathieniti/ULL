__author__ = 'efiathieniti'
# Functions 
from typing import List
from itertools import islice
import numpy as np
Vector = List[float]


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


def evaluate_similarity(word_pairs, word_vectors):

    """Evaluates similarity for a set of word pairs

    Parameters
    ----------
    word_pairs -- a list of word pairs eg.simlex shape: (n_pairs, 2)
    word_vectors -- the vectors for each word from the embedding


    Returns
    -------
    list with cosine similarity values for each pair (n_pairs)

    """
    cosine_similarities = []
    for index, row in word_pairs.iterrows():
        if row[0] in word_vectors.keys() and row[1] in word_vectors.keys():
            cos_sim = analyze.cosine_similarity(word_vectors[row[0]], word_vectors[row[1]])
            cosine_similarities.append(cos_sim)
        else:
            cosine_similarities.append(np.nan)

    return cosine_similarities







