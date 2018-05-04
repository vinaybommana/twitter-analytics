import tweepy
import sys
import jsonpickle
import fileinput
from datetime import datetime
# import io
import codecs
# import csv
# import os
# Replace the API_KEY and API_SECRET with your application's key and secret.
APP_KEY = 'BlHVe4NazxtdbPgx386iUV6MZ'
APP_SECRET = 'f2Hhq39zzPeIaU3mQZgqki2he4ncTXEE8dOglTJtDOl193LK3l'

auth = tweepy.AppAuthHandler(APP_KEY, APP_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)

# csv_file = csv.writer(open("output.csv", "w"))
# csv_file.writerow(["Name", "Screen Name", "Id", "Friends Count"])
# this is what we're searching for
maxTweets = 10000000
# Some arbitrary large number
tweetsPerQry = 100
list_of_names = []
tags = []
tweets_text = []
user_ids = []


def read_file(input_file):
    with fileinput.input(files=(str(input_file))) as f:
        for line in f:
            tags.append(line)

def fetch_date(input_string):
    date_string = input_string.split()
    return str(date_string[2]) + str(date_string[1]) + str(date_string[5])


def main():
    # only a single main function is not cool
    read_file(sys.argv[1])
    for value in tags:
        value = value.strip()
        values = value.split("\t")
        search_item = values[0]
        start_date = values[1]
        end_date = values[2]
        startDateTime = datetime.strptime(start_date, '%Y-%m-%d')
        endDateTime = datetime.strptime(end_date, '%Y-%m-%d')
        startDateTime = startDateTime.date()
        endDateTime = endDateTime.date()
        sinceId = None
        max_id = -1

        tweetCount = 0
        print("Downloading max {0} tweets".format(maxTweets))
        count = 1
        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=search_item,
                                                count=tweetsPerQry,
                                                since=str(startDateTime),
                                                until=str(endDateTime),
                                                show_user=True)
                    else:
                        new_tweets = api.search(q=search_item,
                                                count=tweetsPerQry,
                                                since_id=sinceId,
                                                since=str(startDateTime),
                                                until=str(endDateTime),
                                                show_user=True)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=search_item,
                                                count=tweetsPerQry,
                                                since=str(startDateTime),
                                                until=str(endDateTime),
                                                max_id=str(max_id - 1),
                                                show_user=True)
                    else:
                        new_tweets = api.search(q=search_item,
                                                count=tweetsPerQry,
                                                since=str(startDateTime),
                                                until=str(endDateTime),
                                                max_id=str(max_id - 1),
                                                since_id=sinceId,
                                                show_user=True)
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    # print(tweet['user']['screen_name'])
                    # print(tweet['user']['name'])
                    Tweet = jsonpickle.encode(tweet._json, unpicklable=False)
                    Tweet = jsonpickle.decode(Tweet)
                    tweet_id = Tweet['id_str']
                    user_id_str = Tweet['user']['id_str']
                    date = fetch_date(str(Tweet['created_at']))
                    user_ids.append(user_id_str)

                    # using the delimiter --- for no reason except
                    # for delimiting
                    # serial_number , screen_name, user_id, tweet_id, retweet_count, date, tweet

                    list_of_names.append(str(count) + "---" + Tweet['user']['screen_name'] + "---" +
                                         user_id_str + "---" + tweet_id + "---" + str(Tweet['retweet_count']) + 
                                         str("---") + date + str("---") + str(Tweet['text']).rstrip('\n') + "\n")

                    # print(str(user_id_str))
                    # csv_file is converting large ids to E^10 values
                    # changed the output to text file
                    # csv_file.writerow([
                    #     Tweet['user']['name'],
                    #     Tweet['user']['screen_name'],
                    #     user_id_str,
                    #     str(Tweet['user']['friends_count'])])

                    count += 1
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                print(len(set(list_of_names)))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

            with codecs.open("problem_large.txt", "w", "utf-8") as o:
                # o.write("Name" + "\t\t\t" +
                #         "screen_name" + "\t\t" + "user_id\n")
                for line in list_of_names:
                    # print(type(line))
                    o.write(line + "\n")

    # users_and_their_tweets = dict(zip(user_ids, tweets_text))
    # print(users_and_their_tweets)

    print("Downloaded {0} tweets, Saved to {1}".format(tweetCount,
                                                       "problem_large.txt"))


if __name__ == '__main__':
    main()
