# ULL - Evaluating Word Embeddings

Evaluates three word embeddings BoW2, BoW5 and Deps obtained with Skip-Gram using different contexts. The goal of this repository is to be used as demos for comparing the three embeddings.

## Examples

The following python notebooks serves as example evaluations on different tasks, similarity, analogy and clustering. 

## Instructions

Once the repository is cloned run the python notebooks for quantitative and qualitative embedding evaluations


### Similarity.ipynb: 

Description:
Evaluates embeddings based on word similarity tasks. 
Computes Spearman and Pearson correlations against the SimLex and MEN datasets for each embedding.

Instructions: Other data sets could be evaluated by replacing 'word_pairs' dataframe with a new set, after loading.

### Analogy.ipynb: 

Description:
Evaluates embdeddings based on word analogy tasks.
Computes the analogous word for each question in the Google analogy test set. 
Performs quantitative evaluation of the predictions using Mean Reciprocal Rank and accuracy

Instructions: Other sets could be evaluated by replacing the 'data/questions_words.txt' file.

### Clustering.ipynb


