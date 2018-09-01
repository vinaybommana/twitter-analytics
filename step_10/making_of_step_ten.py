from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import csv
import math
import pandas as pd
import re


def read_file(filename):
    rows = list()
    with open(str(filename), "r") as n:
        csvreader = csv.reader(n)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows


def clean_tweets(list_of_tweets):
    output_list = list()
    for i in list_of_tweets:
        if "RT @" in i:
            tweet = re.sub("RT @[A-Za-z0-9:]+\s", "", i)
        else:
            tweet = i

        if "@" in tweet:
            tweet = re.sub("@[A-Za-z0-9]+\s", "", tweet)

        tweet = tweet.strip("…")
        tweet = tweet.replace("…", "")
        tweet = tweet.replace("'", "")
        output_list.append(tweet)

    return output_list


def make_list_tweet_ids(ninth_rows):
    return [i[4] for i in ninth_rows]


def make_list_of_tweets(ninth_rows):
    return [i[7] for i in ninth_rows]


def treat_the_tweets(list_of_tweets):
    treated_tweets = list()
    for i in list_of_tweets:
        # splitting the sentences to words
        tweet = i.split()
        # making entire words lower case
        tweet = [i.lower() for i in tweet]
        # removing single quotes
        for i in tweet:
            if "'" in i:
                i_position = tweet.index(i)
                i = i.replace("'", "")
                tweet[i_position] = i

        # removing the https:// link
        tweet = [i for i in tweet if "https://" not in i]
        tweet = [i for i in tweet if "http" not in i]

        # removing digits from the tweet
        for i in tweet:
            if str(i[0]).isdigit():
                i_position = tweet.index(i)
                i = re.sub("[0-9]+", "", i)
                tweet[i_position] = i

        # removing pic.twitter.com/<word>
        for i in tweet:
            if "pic.twitter.com" in i:
                i_position = tweet.index(i)
                i = re.sub("pic.twitter.com/[A-Za-z0-9]+", "", i)
                tweet[i_position] = i

        # cleaning stuff
        tweet = [i.replace("!", "") for i in tweet]
        tweet = [i.replace(":", "") for i in tweet]
        tweet = [i.replace(".", "") for i in tweet]
        tweet = [i.replace("#", "") for i in tweet]
        tweet = [i.replace("$", "") for i in tweet]
        tweet = [i.replace("?", "") for i in tweet]
        tweet = [i.replace(")", "") for i in tweet]
        tweet = [i.replace("(", "") for i in tweet]
        tweet = [i.replace("{", "") for i in tweet]
        tweet = [i.replace("}", "") for i in tweet]
        tweet = [i for i in tweet if "&amp" not in i]
        tweet = [i for i in tweet if "|" not in i]
        tweet = [i for i in tweet if "@" not in i]
        tweet = [i for i in tweet if "&" not in i]
        tweet = [i for i in tweet if "-" not in i]
        tweet = [i for i in tweet if not i.isdigit()]
        # print(tweet)
        treated_tweets.append(tweet)

    return treated_tweets


# stop words removal
def remove_stop_words(treated_tweets):
    stop_words_removed_tweets = list()
    stop_words = stopwords.words('english')
    for tweet in treated_tweets:
        tweet = [i for i in tweet if i not in stop_words]
        stop_words_removed_tweets.append(tweet)

    return stop_words_removed_tweets


# stemming
def stem_the_tweets(tweets):
    ps = PorterStemmer()
    stemmed_tweets = list()
    for tweet in tweets:
        tweet = [ps.stem(i) for i in tweet]
        stemmed_tweets.append(tweet)

    return stemmed_tweets


# lemmatizing
def lemmatize_the_tweets(tweets):
    lm = WordNetLemmatizer()
    lemmatized_tweets = list()
    for tweet in tweets:
        tweet = [lm.lemmatize(i) for i in tweet]
        lemmatized_tweets.append(tweet)

    return lemmatized_tweets


# gathering all the tweets
def tweet_dump(lemmatized_tweets):
    tweet_dump = list()
    for tweet in lemmatized_tweets:
        for i in tweet:
            tweet_dump.append(i)

    # print(len(tweet_dump))
    tweet_dump = set(tweet_dump)
    # print(len(tweet_dump))
    return tweet_dump


# giving the count of word in a list
def count_the_word(list_of_words, word):
    return list_of_words.count(word)


def count_list(dictionary_of_tweets_and_ids, word):
    '''
    returns list of term frequencies for a particular word
    '''
    output_list = list()
    for i in dictionary_of_tweets_and_ids.keys():
        # print(dictionary_of_tweets_and_ids[i])
        output_list.append(count_the_word(dictionary_of_tweets_and_ids[i], word))

    return output_list


def inverse_document_frequency(word, dictionary_of_tweets_and_ids):
    '''
    returns a floating point number of log(tweets containing word / total tweets)
    '''
    tweet_number = 0
    for i in dictionary_of_tweets_and_ids:
        if word in dictionary_of_tweets_and_ids[i]:
            tweet_number += 1

    # print(tweet_number)
    # print(len(dictionary_of_tweets_and_ids.keys()))
    # inverse document frequency = log(number of tweets containing the word / total)
    return math.log(tweet_number / len(dictionary_of_tweets_and_ids.keys()))


ninth_rows = list()
list_of_tweets = list()
list_of_tweet_ids = list()


def main():
    ninth_rows = read_file("step_nine_output.csv")
    list_of_tweets = make_list_of_tweets(ninth_rows)
    list_of_tweet_ids = make_list_tweet_ids(ninth_rows)
    list_of_tweets = clean_tweets(list_of_tweets)
    treated_tweets = treat_the_tweets(list_of_tweets)
    stop_words_removed_tweets = remove_stop_words(treated_tweets)
    stemmed_tweets = stem_the_tweets(stop_words_removed_tweets)
    # lemmatize the tweets
    lemmatized_tweets = lemmatize_the_tweets(stemmed_tweets)
    # print(lemmatized_tweets)

    dict_of_tweets_and_ids = dict(zip(list_of_tweet_ids, lemmatized_tweets))
    all_the_tweets = tweet_dump(lemmatized_tweets)
    # print(len(all_the_tweets))
    data_dictionary = {'tweet_id': list_of_tweet_ids}
    df = pd.DataFrame(data_dictionary)
    for i in all_the_tweets:
        if len(i) > 0:
            idf_score = float(inverse_document_frequency(i, dict_of_tweets_and_ids))
            # term_df[str(i)] = count_list(dict_of_tweets_and_ids, i)
            count = count_list(dict_of_tweets_and_ids, i)
            count = [float(i * idf_score) for i in count]
            df[str(i)] = count

    # have to add total tvii score
    print(df.head())
    # for index, row in df.iterrows():
    #     print(df.head())

    total_tvii = list()
    for row in df.itertuples():
        tvii = list(row)
        tvii = tvii[2:]
        total = 0
        for i in tvii:
            total += i ** 2
        norm_total = math.sqrt(total)
        total_tvii.append(norm_total)
        print(len(total_tvii))

    df["total_tvii_score"] = total_tvii

    df.to_csv('step_10_output.csv')


if __name__ == "__main__":
    main()
