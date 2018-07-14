import csv
import codecs
from collections import Counter


def read_csv():
    rows = list()
    with open("step_two_output.csv", "r") as t:
        csvreader = csv.reader(t)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows


def get_mentions(rows):
    user_mentions = list()
    for row in rows:
        user_mention = row[1]
        user_mentions.append(user_mention)
    return user_mentions


def main():
    rows = read_csv()
    user_mentions = get_mentions(rows)
    number_tweets_dict = dict(Counter(user_mentions))
    count = 1
    with codecs.open('step_three_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "No of Tweets\n")
        for mention, number in number_tweets_dict.items():
            line = str(count) + "," + str(mention) + "," + str(number) + "\n"
            o.write(line)
            count += 1


if __name__ == "__main__":
    main()
