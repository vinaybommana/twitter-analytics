#!/usr/bin/env python

'''
KMeans Clustering application
KMeans is an unsupervised learning clustering algorithm
'''

from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import json


def cluster_indices_numpy(cluster_num, labels_array):
    """
    returns the indices of a particular cluster
    :return: numpy array
    """
    return np.where(labels_array == cluster_num)[0]


def main():
    df = pd.read_csv('~/backups/step_10_output.csv')
    # this is because the last time index is saved in the csv
    # and we are getting two index columns which are totally unnecessary
    df = df.drop(df.columns[0], axis=1)
    df.set_index('tweet_id', inplace=True)
    print(df.head())
    list_of_words = list()
    list_of_ids = df.index.values

    for row in df.itertuples(index=True, name='Pandas'):
        list_of_words.append(np.array(row[1:]))

    print(len(list_of_words))

    # clustering block
    # for full data
    kmeans = KMeans(n_clusters=10)
    kmeans.fit(list_of_words)

    print(kmeans.labels_)

    list_of_ids = [str(i) for i in list_of_ids]
    list_of_words = [list(i) for i in list_of_words]
    dict_of_ids_words = dict(zip(list_of_ids, list_of_words))

    # dumping all the information into json files
    # this json consists of tweet_id and respective numeric
    # format of words
    # {'<tweet_id>': [<numeric_format>]}
    with open("tweet_ids_n_words.json", "w+") as t:
        json.dump(dict_of_ids_words, t)

    indices = [str(i) for i in range(len(list_of_ids))]
    dict_of_indices_ids = dict(zip(indices, list_of_ids))

    # this json file consists of indices and ids <important>
    # format of json
    # {'index<0>': 'tweet_id'}
    with open("indices_ids.json", "w+") as i:
        json.dump(dict_of_indices_ids, i)
    dict_of_cluster_num_n_index = dict()

    for i in range(10):
        cluster_list = cluster_indices_numpy(i, kmeans.labels_)
        cluster_list = [str(i) for i in cluster_list]
        dict_of_cluster_num_n_index[str(i)] = cluster_list
        print(cluster_indices_numpy(i, kmeans.labels_))

    # this json file consists of cluster number,
    # and the indices of the data <list_of_words> from kmeans
    with open("cluster_num_n_index.json", "w+") as c:
        json.dump(dict_of_cluster_num_n_index, c)


    # ------------------------------------------------------
    # Three fifth Block
    # ------------------------------------------------------

    # applying KMeans for 3/5th of the words
    three_fifth_of_ids = list_of_ids[: int(len(list_of_ids) * (3 / 5))]

    indices_3_5 = [str(i) for i in range(len(three_fifth_of_ids))]
    dict_of_indices_ids_3_5 = dict(zip(indices_3_5, three_fifth_of_ids))

    # this json file consists of indices and ids <important>
    # format of json
    # {'index<0>': 'tweet_id'}
    with open("indices_ids_3_5.json", "w+") as d:
        json.dump(dict_of_indices_ids_3_5, d)

    three_fifth_of_words = list_of_words[: int(len(list_of_words) * (3 / 5))]
    kmeans.fit(three_fifth_of_words)

    print(kmeans.labels_)

    dict_of_cluster_num_n_index_3_5 = dict()

    for i in range(10):
        cluster_list = cluster_indices_numpy(i, kmeans.labels_)
        cluster_list = [str(i) for i in cluster_list]
        dict_of_cluster_num_n_index_3_5[str(i)] = cluster_list
        print(cluster_indices_numpy(i, kmeans.labels_))

    # this json file consists of cluster number,
    # and the indices of the data <list_of_words> from kmeans
    with open("cluster_num_n_index_3_5.json", "w+") as f:
        json.dump(dict_of_cluster_num_n_index_3_5, f)
    

if __name__ == "__main__":
    main()

