# step 10
import csv
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def read_file():
    with open("step_10.1_output.csv", "r") as n:
        csvreader = csv.reader(n)
        next(csvreader)
        for row in csvreader:
            ninth_rows.append(row)


def clean_tweets(list_of_tweets):
    output_list = list()
    for i in list_of_tweets:
        if "RT @" in i:
            tweet = i.split(":")[1]
        else:
            tweet = i

        tweet = tweet.strip("…")
        tweet = tweet.replace("…", "")
        tweet = tweet.replace("'", "")
        output_list.append(tweet)

    return output_list


def make_list_tweet_ids():
    return [i[3] for i in ninth_rows]


def make_list_of_tweets():
    return [i[6] for i in ninth_rows]


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

        # cleaning stuff
        tweet = [i.replace("!", "") for i in tweet]
        tweet = [i.replace(":", "") for i in tweet]
        tweet = [i.replace(".", "") for i in tweet]
        tweet = [i.replace("#", "") for i in tweet]
        tweet = [i.replace("$", "") for i in tweet]
        tweet = [i.replace("?", "") for i in tweet]
        tweet = [i.replace(")", "") for i in tweet]
        tweet = [i.replace("(", "") for i in tweet]
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


ninth_rows = list()
list_of_tweets = list()
list_of_tweet_ids = list()


def main():
    read_file()
    list_of_tweets = make_list_of_tweets()
    list_of_tweet_ids = make_list_tweet_ids()
    list_of_tweets = clean_tweets(list_of_tweets)
    treated_tweets = treat_the_tweets(list_of_tweets)
    stop_words_removed_tweets = remove_stop_words(treated_tweets)
    stemmed_tweets = stem_the_tweets(stop_words_removed_tweets)
    # lemmatize the tweets
    lemmatized_tweets = lemmatize_the_tweets(stemmed_tweets)
    for i in lemmatized_tweets:
        print(i)
    dict_of_tweets_and_ids = dict(zip(list_of_tweet_ids, treated_tweets))


if __name__ == "__main__":
    main()
