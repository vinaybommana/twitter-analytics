import csv
import codecs
import math


def read_csv(filename):
    rows = list()
    with open(str(filename), "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows


def main():
    second_rows = read_csv("step_two_output.csv")
    third_rows = read_csv("step_three_output.csv")
    unique_users = list()
    no_of_tweets = list()
    dict_of_user_retweet = dict()
    users = list()
    for second_row in second_rows:
        user = second_row[1]
        retweet = second_row[3]
        if user not in users:
            dict_of_user_retweet[user] = int(retweet)
            users.append(user)
        else:
            dict_of_user_retweet[user] += int(retweet)

    for third_row in third_rows:
        unique_users.append(third_row[1])
        no_of_tweets.append(third_row[2])

    dict_user_number_tweet = dict(zip(unique_users, no_of_tweets))

    # print(dict_of_user_retweet)

    # serial_number, username@mention, userid, tweet_count, retweet_count, log(retweet_count)
    with codecs.open('step_four_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "No of Tweets" + "," +
                "No of retweets" + "," + "log base 2 (retweet_count)\n")
        count = 1
        for user, no_of_tweets in dict_user_number_tweet.items():
            line = str(count) + "," + str(user) + "," + str(no_of_tweets) + "," + \
                   str(dict_of_user_retweet[user]) + "," + str(math.log(int(dict_of_user_retweet[user]), 2)) + "\n"
            o.write(line)
            count += 1


if __name__ == '__main__':
    main()
