# collect tweets of those influential users from output two
# and count no of tweets posted by influential users
import csv
import codecs


def read_eighth_output():
    with open("step_eight_output_rank.csv", "r") as e:
        csvreader = csv.reader(e)
        next(csvreader)
        for row in csvreader:
            eighth_rows.append(row)


def read_four_output():
    with open("step_four_output.csv", "r") as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for row in csvreader:
            fourth_rows.append(row)


def read_two_output():
    with open("step_two_output.csv", "r") as t:
        csvreader = csv.reader(t)
        next(csvreader)
        for row in csvreader:
            second_rows.append(row)


def list_all_influential_users():
    for row_8 in eighth_rows:
        user_influential.append(row_8[1])


def make_tweet_user_dict():
    read_two_output()
    for row in second_rows:
        user_tweet_dict[row[1]] = row[6]


def main():
    read_eighth_output()
    list_all_influential_users()
    read_four_output()
    make_tweet_user_dict()
    for row_4 in fourth_rows:
        if row_4[1] in user_influential:
            influential_list.append(row_4)

    # print(len(influential_list))


influential_list = list()
user_influential = list()
eighth_rows = list()
fourth_rows = list()
second_rows = list()
user_tweet_dict = dict()


if __name__ == "__main__":
    main()
