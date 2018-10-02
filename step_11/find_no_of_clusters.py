#!/usr/bin/env python

'''
find the number of clusters suitable for KMeans
'''
import scikitplot
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('~/backups/step_10_output.csv')
    df = df.drop(df.columns[0], axis=1)
    df.set_index('tweet_id', inplace=True)
    print(df.head())

    list_of_words = list()
    for row in df.itertuples(index=True, name='Pandas'):
        list_of_words.append(np.array(row[1:]))

    print(len(list_of_words))

    # clustering block
    kmeans_elbow_check = KMeans()
    scikitplot.cluster.plot_elbow_curve(kmeans_elbow_check, X=list_of_words, cluster_ranges=range(1, 15))


if __name__ == "__main__":
    main()
