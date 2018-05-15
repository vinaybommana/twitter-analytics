import csv
import codecs
import re
from collections import Counter


def read_csv():
    with open("step_two_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


# just for testing the output
# def read_step_three_output():
#     with open("step_three_output.csv", "r") as t:
#         csvreader = csv.reader(t)
#         next(csvreader)
#         for row in csvreader:
#             test_three.append(row[2])
#     return len(test_three)


def regular_search(tweet):
    e = re.compile('RT\s@\w*:')
    user = e.search(tweet)
    if user is None:
        return '0'
    else:
        return user.group()
 
    
def main():
    read_csv()
    for row in rows:
        tweets.append(row[6])
        unique_users.append(row[1])
        unique_user_ids.append(row[2])
        retweet_count.append(row[4])

    unique_user_dict = dict(zip(unique_users, unique_user_ids))
    retweet_count_dict = dict(zip(unique_users, retweet_count))

    for tweet in tweets:
        # print(tweet)
        tweeted_user = regular_search(tweet).strip(':')
        tweeted_users.append(tweeted_user.lstrip('RT @'))

    users = [i for i in tweeted_users if i != '0']

    # for user in tweeted_users:
    #     print(user)
    c = Counter(users)
    # serial_number, username@mention, userid, tweet_count
    with codecs.open('step_three_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "user_id\t\t" + "," + "No of Tweets\n")
        count = 1
        for i in c.keys():
            if i in unique_user_dict:
                line = str(count) + "," + str(i) + "," + str(unique_user_dict[i]) + "," + str(c[i]) + "\n"
                o.write(line)
                count += 1

        for i in unique_users:
            # can't ignore users with more retweets
            if (int(retweet_count_dict[i]) > 30) and (i not in c):
                line = str(count) + "," + str(i) + "," + str(unique_user_dict[i]) + "," + str(1) + "\n"
                o.write(line)
                count += 1

    # print(read_step_three_output())


rows = list()
output_users = list()
tweets = list()
tweeted_users = list()
unique_users = list()
unique_user_ids = list()
retweet_count = list()
# test_three = list()

if __name__ == '__main__':
    main()
