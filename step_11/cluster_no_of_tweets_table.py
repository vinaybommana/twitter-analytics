'''
|cluster_number | # No of tweets|
| ----          |  ----------   |
|               |               |

Make table like above after clustering
for all the tweets and
3/5th of the tweets
'''

import json

def read_json(file_name):
    """
    :input: <class 'str'> a string containing name of the file
    """
    return_dict = dict()
    with open(file_name) as f:
        return_dict = json.load(f)

    return return_dict

def write_csv_from_dict(dictionary, filename):
    """ Takes a dictionary containing cluster_numbers
    indexes in the particular cluster
    makes a csv <table> accordingly

    |cluster_number | # No of tweets|
    | ----          |  ----------   |
    |               |               |
    :input: <class 'dict'> a dictionary containing cluster number
            and list of indexes
    :return: None
    """
    list_of_clusno_no_tweets = list()
    for key, value in dictionary.items():
        list_of_clusno_no_tweets.append((key, len(value)))

    with open(filename, "w") as c:
        c.write("Cluster Number" + "," + "No of Tweets\n")

        for element in list_of_clusno_no_tweets:
            line = str(element[0]) + "," + str(element[1]) + "\n"
            c.write(line)


def main():
    dict_of_full_index = read_json(file_name='./full_tweets/cluster_num_n_index.json')
    dict_of_three_fifth_indexes = read_json(file_name='./three_fifth_of_the_tweets/cluster_num_n_index_3_5.json')
    write_csv_from_dict(dict_of_full_index, "cluster_num_of_tweets.csv")
    write_csv_from_dict(dict_of_three_fifth_indexes, "cluster_num_of_tweets_3_5.csv")


if __name__ == "__main__":
    main()
