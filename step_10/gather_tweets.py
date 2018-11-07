"""
Gather tweets from step_9 output
seperate the words from tweet
normalise the tweets
"""

import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join('..')))

from utils.FileReader import FileReader
from pprint import pprint
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


class RowSeperater(object):
    """ makes a dictionary when rows of usernames and tweets are given
    :input: list of lists consisting of [username, tweet_n]
    """

    def __init__(self, rows):
        self.rows = rows

    def seperate_rows(self):
        """
        {
            "user_name": {
                "tweet_id0": "Tweet0",
                "tweet_id1": "Tweet1"
            }
        }
        """
        dict_of_users = dict()
        for row in self.rows:
            user_name = row[0]
            tweets = row[1:]
            dict_of_tweets = dict()
            for tweet in tweets:
                tweet_id = tweet.split("---")[0]
                text = tweet.split("---")[1]
                dict_of_tweets[tweet_id] = text
            dict_of_users[user_name] = dict_of_tweets

        return dict_of_users


class TweetNormalizer(object):
    """ takes a string <tweet> cleans them
        removing unnecessary words
        returns a list of words

        :return: list of words
    """

    def __init__(self, tweet):
        self.tweet = tweet
        _words = self.make_words()
        _words = self.remove_mention_word(_words)
        _words = self.remove_characters(_words)
        _words = self.remove_links(_words)
        self.words = self.remove_numbers(_words)

    def make_words(self):
        """
        words should be lowercase
        """
        words = self.tweet.split()
        words = [i.lower() for i in words]
        return words

    @staticmethod
    def remove_mention_word(_words):
        words = []
        for word in _words:
            if "RT @" in word:
                word = re.sub("RT @[a-z0-9:]+", "", word)
            if "@" in word:
                word = re.sub("^@[a-z0-9:]+", "", word)
            words.append(word)
        words = [i for i in words if len(i) > 0]
        return words

    @staticmethod
    def remove_characters(_words):
        words = []
        for word in _words:
            if "…" in word:
                word = word.replace("…", "")
            if "'" in word:
                word = word.replace("'", "")
            if "#" in word:
                word = word.replace("#", "")
            if "$" in word:
                word = word.replace("$", "")
            if "?" in word:
                word = word.replace("?", "")
            if ")" in word:
                word = word.replace(")", "")
            if "(" in word:
                word = word.replace("(", "")
            if "{" in word:
                word = word.replace("{", "")
            if "}" in word:
                word = word.replace("}", "")
            if "&amp" in word:
                word = word.replace("&amp", "")
            if "|" in word:
                word = word.replace("|", "")
            if "@" in word:
                word = word.replace("@", "")
            if "&" in word:
                word = word.replace("&", "")
            if "-" in word:
                word = word.replace("-", "")
            if "!" in word:
                word = word.replace("!", "")
            words.append(word)
        words = [i for i in words if len(words) > 0]
        return words

    @staticmethod
    def remove_numbers(_words):
        words = []
        for word in _words:
            if not word.isdigit():
                words.append(word)
        return words

    @staticmethod
    def remove_links(_words):
        words = []
        for word in _words:
            if "http://" in word:
                word = word.split("http://")[0]
            if "https://" in word:
                word = word.split("https://")[0]
            if "pic.twitter.com" in word:
                word = word.split("pic.twitter.com")[0]
            if ".twitter.com" in word:
                word = word.split(".twitter.com")[0]
            if ":" in word:
                word = word.replace(":", "")
            if "." in word:
                word = word.replace(".", "")
            if "“" in word:
                word = word.replace("“", "")
            if "”" in word:
                word = word.replace("”", "")
            if "’" in word:
                word = word.replace("’", "")
            if "_" in word:
                word = word.replace("_", "")
            words.append(word)
            words = [i for i in words if len(i) > 0]
            words = [i for i in words if not i.startswith("//twittercom/")]
        return words


class StopWordsRemover(object):
    """ removes english stop words from tweet dump """

    def __init__(self, tweet_dump):
        self.tweet_dump = tweet_dump
        self.reduced_words = self.remove_stop_words()

    def remove_stop_words(self):
        stop_words = stopwords.words('english')
        return [i for i in self.tweet_dump if i not in stop_words]


class WordStemmer(object):
    """ stems the input words """

    def __init__(self, tweet_dump):
        self.tweet_dump = tweet_dump

    def implement_stemming(self):
        ps = PorterStemmer()
        return [ps.stem(word) for word in self.tweet_dump]


class WordLemmatizer(object):
    """ lemmatizes the input words """

    def __init__(self, tweet_dump):
        self.tweet_dump = tweet_dump

    def implement_lemmatizing(self):
        lm = WordNetLemmatizer()
        return [lm.lemmatize(word) for word in self.tweet_dump] 


def main():
    os.chdir("../step_9")
    reader = FileReader("step_9_output_inf_user_tweets.csv")
    user_n_tweets = reader.rows
    dict_of_users = RowSeperater(user_n_tweets).seperate_rows()
    tweet_dump = []
    dict_of_id_words = {}
    for key, value in dict_of_users.items():
        for k, v in value.items():
            words_list = TweetNormalizer(v).words
            words_list = StopWordsRemover(words_list).reduced_words
            stemmed_words = WordStemmer(words_list).implement_stemming()
            lem_words = WordLemmatizer(stemmed_words).implement_lemmatizing()
            lem_words = list(set(lem_words))
            dict_of_id_words[k] = lem_words
            tweet_dump += lem_words

    tweet_dump = list(set(tweet_dump))
    # print(len(tweet_dump))

    pprint(dict_of_id_words)


if __name__ == "__main__":
    main()
