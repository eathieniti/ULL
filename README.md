# ULL - Evaluating Word Embeddings

Evaluates three word embeddings BoW2, BoW5 and DEPS obtained with Skip-Gram using different contexts. The goal of this repository is to be used as demos for comparing the three embeddings.

## Examples

The following python notebooks serves as example evaluations on different tasks, similarity, analogy and clustering. 

### Instructions

Once the repository is cloned run the python notebooks for quantitative and qualitative embedding evaluations. The zipped embedding files, bow2.words.bz2, bow5.words.bz2, deps.words.bz2 need to be added under 'data/' before running.

#### Similarity.ipynb: 

Description:
Evaluates embeddings based on word similarity tasks. 
Computes Spearman and Pearson correlations against the SimLex and MEN datasets for each embedding.

Instructions: Other data sets could be evaluated by replacing 'word_pairs' dataframe with a new set, after loading.

#### Analogy_qualitative.ipynb: 

Description:
Evaluates embdeddings based on word analogy tasks.
Computes the analogous word for each question in the Google analogy test set. 
Performs qualitative evaluation of the predictions by looking at 3 predicted answers from each model for selected queries

#### Analogy_Quantitative_with_batching2.ipynb: 

Description:
As the previous but performs quantitative evaluation of the predictions in the whole Google analogy test set using Mean Reciprocal Rank and accuracy. 
Uses batching to sample the Google analogy test set because of memory issues when the word analogy set vectors are large.

Instructions: Other sets could be evaluated by replacing the 'data/questions_words.txt' file.

#### Clustering.ipynb

Description:
This file performes the K-Means algorithm on the three embeddings, it can be tested with variations in the number of clusters. It outputs a csv file with the results. A collection of results for 100, 200, 300, 400 and 500 can be found in the repository under 'Results'.

Instructions: Different numbers of clusters can be filled and different embeddings can be used.


