"""
# gather around all the influential users from step_4
using these influential users, get tweets from step_2
first gather user and his tweet from step_2 <make a set of it>

then iterate over influential users and if the user is found in the tweet,
write it in the csv file
"""

import csv
from pprint import pprint


class FileReader(object):
    """ Read the <csv> file get the data in the form of rows """

    def __init__(self, filename):
        self.filename = filename
        self.rows = self.get_rows()

    def get_rows(self):
        rows = []
        with open(self.filename, "r") as f:
            csvreader = csv.reader(f)
            next(csvreader)
            for row in csvreader:
                rows.append(row)
        return rows

    def __repr__(self):
        return "Returns a list of rows in the given {} name".format(self.filename)

    def __str__(self):
        return "Returns a list of rows in the given {} name".format(self.filename)


class InfluentialUser(object):
    """ User containing global influence score more than threshold """

    def __init__(self, influential_rows):
        self.rows = influential_rows
        self.users = self.get_influential_users()

    def get_influential_users(self):
        users = []
        for row in self.rows:
            users.append(row[1])
        return users

    def __repr__(self):
        return "user containing global influence score more than threshold"

    def __str__(self):
        return "user containing global influence score more than threshold"


def make_user_n_tweet(rows):
    user_n_tweets = list()
    for row in rows:
        user_n_tweets.append((row[1], row[5]))

    return user_n_tweets


def main():
    filereader = FileReader("step_two_output.csv")
    # print(filereader)
    tweet_containing_rows = filereader.rows
    user_n_tweets = make_user_n_tweet(tweet_containing_rows)
    # print(tweet_containing_rows)
    filereader_2 = FileReader("step_five_output.csv")
    user_container = InfluentialUser(filereader_2.rows)
    influential_users = user_container.users
    # print(len(influential_users))
    print(len(tweet_containing_rows))
    # print(user_n_tweets)
    dict_of_user_n_his_tweets = dict()
    for user_name, tweet in user_n_tweets:
        if user_name in influential_users:
            if user_name not in dict_of_user_n_his_tweets:
                dict_of_user_n_his_tweets[user_name] = [tweet]
            else:
                tweet_list = dict_of_user_n_his_tweets[user_name]
                tweet_list.append(tweet)
                dict_of_user_n_his_tweets[user_name] = tweet_list

    # print(len(dict_of_user_n_his_tweets.keys()))
    # writing to a csv file
    with open("step_9_output_inf_user_tweets.csv", "w") as s:
        s.write("UserName, Tweets\n")
        for key, value in dict_of_user_n_his_tweets.items():
            line = ""
            line += key
            for tweet in value:
                line += ","
                line += tweet
            line += "\n"
            s.write(line)


if __name__ == "__main__":
    main()
