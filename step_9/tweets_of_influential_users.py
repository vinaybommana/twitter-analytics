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


def make_tweetid_tweet_dict():
    for row in second_rows:
        tweetid_user_dict[row[1]] = row[3]


def make_inf_user_dict():
    for row in eighth_rows:
        inf_score_user_dict[row[1]] = row[0]


def main():
    read_eighth_output()
    list_all_influential_users()
    read_four_output()
    make_tweet_user_dict()
    make_tweetid_tweet_dict()
    make_inf_user_dict()
    for row_4 in fourth_rows:
        if row_4[1] in user_influential:
            influential_list.append(row_4)

    # print(len(influential_list))
    output_list = list()
    for row in influential_list:
        inner_list = list()
        inner_list.append(row[1])
        inner_list.append(row[2])
        inner_list.append(tweetid_user_dict[row[1]])
        inner_list.append(row[4])
        inner_list.append(user_tweet_dict[row[1]])
        inner_list.append(inf_score_user_dict[row[1]])
        output_list.append(inner_list)

    output_list = sorted(output_list, key=lambda x: x[5], reverse=True)

    # print(output_list[0])

    with codecs.open('step_nine_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial Number\t" + "," + "Screen Name\t" + "," + "user_id\t\t" + "," + "tweet_id\t\t" + "," + "retweet_count\t" + "," + "Global Influence Score" + "," + "Tweet\n")
        count = 1
        comma = ","
        for row in output_list:
            line = (str(count) + comma + str(row[0]) + comma + str(row[1]) + comma + str(row[2]) +
                    comma + str(row[3]) + comma + str(row[5]) + comma + str(row[4]) + "\n")

            o.write(line)
            count += 1


influential_list = list()
user_influential = list()
eighth_rows = list()
fourth_rows = list()
second_rows = list()
tweetid_user_dict = dict()
user_tweet_dict = dict()
inf_score_user_dict = dict()


if __name__ == "__main__":
    main()
