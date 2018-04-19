__author__ = 'efiathieniti'
import analyze
import numpy as np


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

