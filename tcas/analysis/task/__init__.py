# -*- coding: utf-8 -*-
# TODO: implement unsupervised clustering function (probably k-means or k-median)
# TODO: use top-scoring terms from LDA of topical websites as bases for clustering?
# TODO: construct matrix where a goal is a row and a column is a term

import numpy as np
import nltk
from sklearn.datasets import fetch_20newsgroups
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import logging
from optparse import OptionParser
import sys
import numpy as np

from tcas.analysis.helper.unmet_needs_provider import unmet_needs_provider
from tcas.config import ENGLISH_PICKLE, GOAL_TOKENS
from sklearn.feature_extraction.text import CountVectorizer

from tcas.analysis.helper.goal_extractor import tokenized_goals
from tcas.task_manager import task_manager


@task_manager.task()
def cluster_goals():
    """Run clustering task.


    Parameters
    ----------

    Returns
    -------

    """
    # needs = [
    #     'household',
    #     'supports',
    #     'insurance',
    #     'financial',
    #     'medical',
    #     'mental health',
    #     'substance use'
    # ]
    n_samples = len(tokenized_goals)
    n_features = sum([len(g) for g in tokenized_goals])
    random_state = 170
    k = 4
    count_vectorizer = CountVectorizer(
        max_features=n_features,
        stop_words='english',
        binary=True
    )
    bigram_vectorizer = CountVectorizer(
        ngram_range=(1, 2),
        token_pattern=r'\b\w+\b'
    )
    tfidf_vectorizer = TfidfVectorizer(
        max_features=n_features,
        stop_words='english'
    )
    transformer = TfidfTransformer(smooth_idf=False)
    count_vectorizer_x = count_vectorizer.fit_transform(tokenized_goals)
    bigram_vectorizer_x = bigram_vectorizer.fit_transform(tokenized_goals)
    tfidf_vectorizer_x = tfidf_vectorizer.fit_transform(tokenized_goals)

    # svd = TruncatedSVD(n_components=100)
    # normalizer = Normalizer(copy=False)
    # lsa = make_pipeline(svd, normalizer)
    # count_vectorizer_x_lsa = lsa.fit_transform(count_vectorizer_x)
    # explained_variance = svd.explained_variance_ratio_.sum()
    # print("Explained variance of the SVD step: {}%".format(
    #     int(explained_variance * 100)))

    km = KMeans(
        n_clusters=k,
        n_init=1,
        max_iter=100,
        verbose=True
    )
    km.fit(tfidf_vectorizer_x)

    # original_space_centroids = svd.inverse_transform(km.cluster_centers_)
    # order_centroids = original_space_centroids.argsort()[:, ::-1]
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = tfidf_vectorizer.get_feature_names()
    clusters = []
    centroids = []
    for i in range(k):
        clusters.append("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            centroids.append(' %s' % terms[ind])
    return clusters, centroids


    # TODO: implement search module as an async task (e.g., for searching index of case notes for mention of VSSP)
