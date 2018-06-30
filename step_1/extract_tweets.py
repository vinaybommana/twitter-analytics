import tweepy
from datetime import datetime
import json
import sys
import urllib
import codecs


APP_KEY = 'bNgGRKZ0TAGN3jxnFj9yEfIYq'
APP_SECRET = '7Ex0TfHpLBImWnE76JBFjuGGPeP0okuT0r5j1NVmDjNWIpnnou'

auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)


max_tweets = 100
tweets = list()


def read_input_file():
    with open("input", "r") as i:
        list_of_input_lines = list()
        for input_line in i:
            topic, start_date, end_date = input_line.split()
            list_of_input_lines.append([topic, start_date, end_date])
    return list_of_input_lines


def extract_tweets(list_of_input_lines):
    input_line_tweets = list()
    for input_line in list_of_input_lines:
        topic, start_date, end_date = input_line
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        try:
            for tweet in tweepy.Cursor(api.search, q=topic, since=start_date, until=end_date).items():
                tweet = json.dumps(tweet._json)
                tweet = json.loads(tweet)
                tweet_text = tweet['text']
                if not find_any_non_english_in_sentence(tweet_text):
                    tweets.append(tweet)

                if len(tweets) > max_tweets:
                    break

        except urllib.error.HTTPError as e:
            print(e)

        input_line_tweets.append(tweets)

    return input_line_tweets


def find_any_non_english_in_sentence(sentence):
    sentence = sentence.strip()
    for i in sentence:
        if ord(i) > 128 and ord(i) != 8211 and ord(i) != 8230:
            return True

    return False


def process_tweets(input_line_tweets):
    for tweets in input_line_tweets:
        count = 1

        with codecs.open("step_1_output.csv", "w+", "utf-8") as o:
            o.write("Serial_number\t" + "," + "Screen_name\t" + "," + "User Id\t" + "," + "Tweet Id\t\t" + ","
                    "Retweet Count\t" + "," + "Date\t" + "," + "Tweet\n")

            for tweet in tweets:
                tweet_user = tweet['user']['screen_name']
                user_id = tweet['user']['id']
                tweet_id_str = tweet['id_str']
                retweet_count = tweet['retweet_count']
                tweet_text = tweet['text']
                tweet_text = tweet_text.strip()
                tweet_text = tweet_text.replace('\n', '').replace('\r', '')
                tweet_date = tweet['created_at']

                if not find_any_non_english_in_sentence(tweet_text):
                    # write to file
                    line = str(count) + "," + str(tweet_user) + "," + str(user_id) + "," + str(tweet_id_str) + "," + \
                           str(retweet_count) + "," + str(tweet_date) + "," + str(tweet_text) + "\n"

                    o.write(line)
                    count += 1



def main():
    list_of_input_lines = read_input_file()
    input_line_tweets = extract_tweets(list_of_input_lines)
    process_tweets(input_line_tweets)


if __name__ == "__main__":
    main()
