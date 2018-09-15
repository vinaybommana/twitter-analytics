'''
make tables for different clusters

cluster 0
---------
| user@mention | user_id | # tweet count|retweet_count| local influential score (yi)|
| ----         |  ------ | -------      | --------    | ------------------------    |
|              |         |              |             |                             |
'''
from cluster_no_of_tweets_table import read_json
import csv


def read_csv(filename):
    """
    :input: filename of the csv file to read from
    :return: list of rows
    """
    rows = list()
    with open(filename, "r") as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows


def make_dict_of_cluster_n_tweet_ids(cluster_dictionary, ids_dictionary):
    """
    :input:
    cluster_dictionary --> dictionary containing cluster_index
                           and list_of_indexes in the cluster
    ids_dictionary --> dictionary containing index_num and tweet_id
    :return: <class 'dict'> containing cluster_index and list of tweet_ids
    """
    dict_of_cluster_n_tweet_ids = dict()

    for key, value in cluster_dictionary.items():
        list_of_tweet_ids = list()
        for index in value:
            list_of_tweet_ids.append(ids_dictionary[index])

        dict_of_cluster_n_tweet_ids[key] = list_of_tweet_ids

    return dict_of_cluster_n_tweet_ids


def make_tweet_rows_dict(ninth_output_rows):
    """
    :input: list of step_nine_output.csv rows
    :return:
    # this dictionary is to identify the rows of tweets from
    # just the tweet_id
    # {
    #  '<tweet_id>': [<rows respective of tweet_id>] 
    # }
    """
    output_dict = dict()
    for row in ninth_output_rows:
        output_dict[str(row[4])] = row

    return output_dict


def main():
    dict_of_full_index = read_json(file_name='./full_tweets/cluster_num_n_index.json')
    dict_of_three_fifth_indexes = read_json(file_name='./three_fifth_of_the_tweets/cluster_num_n_index_3_5.json')
    dict_of_index_ids = read_json(file_name='./full_tweets/indices_ids.json')
    dict_of_index_ids_3_5 = read_json(file_name='./three_fifth_of_the_tweets/indices_ids_3_5.json')

    nine_output_rows = read_csv('step_nine_with_id_output.csv')
    tweet_and_rows = make_tweet_rows_dict(nine_output_rows)
    # -------------------------------------
    # full tweets
    # -------------------------------------

    dict_of_cluster_n_tweet_ids = make_dict_of_cluster_n_tweet_ids(dict_of_full_index, dict_of_index_ids)
    # print(dict_of_cluster_n_tweet_ids)
    for key, value in dict_of_cluster_n_tweet_ids.items():
        with open("cluster_" + str(key) + ".csv", "w+") as c:
            csvwriter = csv.writer(c)
            csvwriter.writerow(['user@mention', 'user_id', 'No of tweets', 'tweet_id', 'retweet_count', 'local influence score',
                                'Tweet'])
            for tweet_id in value:
                rows = tweet_and_rows[tweet_id]
                csvwriter.writerow(rows[1:])


    # -------------------------------------
    # three fifth of tweets
    # ------------------------------------

    dict_clus_n_twt_ids_3_5 = make_dict_of_cluster_n_tweet_ids(dict_of_three_fifth_indexes, dict_of_index_ids_3_5)
    # print(dict_clus_n_twt_ids_3_5)

    for key, value in dict_clus_n_twt_ids_3_5.items():
        with open("three_fifth_cluster_" + str(key) + ".csv", "w+") as c:
            csvwriter = csv.writer(c)
            csvwriter.writerow(['user@mention', 'user_id', 'No of tweets', 'tweet_id', 'retweet_count', 'local influence score',
                                'Tweet'])
            for tweet_id in value:
                rows = tweet_and_rows[tweet_id]
                csvwriter.writerow(rows[1:])


if __name__ == "__main__":
    main()
