import csv
import codecs
import math


def read_csv():
    with open("step_two_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


def read_step_three():
    with open("step_three_output.csv", "r") as p:
        csvreader = csv.reader(p)
        next(csvreader)
        for row in csvreader:
            three_rows.append(row)


def main():
    read_csv()
    read_step_three()
    for row in rows:
        tweets.append(row[6])
        unique_users.append(row[1])
        unique_user_ids.append(row[2])
        retweet_count.append(row[4])

    unique_user_dict = dict(zip(unique_users, unique_user_ids))
    retweet_count_dict = dict(zip(unique_users, retweet_count))

    # serial_number, username@mention, userid, tweet_count, retweet_count, log(retweet_count)
    with codecs.open('step_four_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "user_id\t\t" + "," + "No of Tweets" + "," +
                "No of retweets" + "," + "log base 2 (retweet_count)\n")
        count = 1
        for row in three_rows:
            line = str(count) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + \
                   str(retweet_count_dict[row[1]]) + "," + str(math.log(int(retweet_count_dict[row[1]]), 2)) + "\n"
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
three_rows = list()
# test_three = list()

if __name__ == '__main__':
    main()
