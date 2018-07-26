# collect tweets of those influential users from output two
# and count no of tweets posted by influential users
import csv
import codecs


def read_eighth_output():
    '''
    returns list from step_eight_output_rank
    '''
    eighth_rows = list()
    with open("step_eight_output_rank.csv", "r") as e:
        csvreader = csv.reader(e)
        next(csvreader)
        for row in csvreader:
            eighth_rows.append(row)
    return eighth_rows


def read_four_output():
    '''
    returns list from step_four_output
    fourth_rows
    '''
    fourth_rows = list()
    with open("step_four_output.csv", "r") as f:
        csvreader = csv.reader(f)
        next(csvreader)
        for row in csvreader:
            fourth_rows.append(row)
    return fourth_rows


def read_two_output():
    second_rows = list()
    with open("step_two_output.csv", "r") as t:
        csvreader = csv.reader(t)
        next(csvreader)
        for row in csvreader:
            second_rows.append(row)
    return second_rows


def list_all_influential_users(eighth_rows):
    user_influential = list()
    for row_8 in eighth_rows:
        user_influential.append(row_8[1])
    return user_influential


def make_tweet_user_dict(second_rows):
    user_tweet_dict = dict()
    for row in second_rows:
        user_tweet_dict[row[1]] = row[5]
    return user_tweet_dict


def make_tweetid_tweet_dict(second_rows):
    tweetid_user_dict = dict()
    for row in second_rows:
        tweetid_user_dict[row[1]] = row[2]
    return tweetid_user_dict


def make_inf_user_dict(eighth_rows):
    inf_score_user_dict = dict()
    for row in eighth_rows:
        inf_score_user_dict[row[1]] = row[0]
    return inf_score_user_dict


def main():
    eighth_rows = read_eighth_output()
    user_influential = list_all_influential_users(eighth_rows)
    fourth_rows = read_four_output()
    second_rows = read_two_output()
    user_tweet_dict = make_tweet_user_dict(second_rows)
    tweetid_user_dict = make_tweetid_tweet_dict(second_rows)
    inf_score_user_dict = make_inf_user_dict(eighth_rows)
    influential_list = list()
    # retrieving the influential users from the list
    for row_4 in fourth_rows:
        if row_4[1] in user_influential:
            influential_list.append(row_4)

    # print(influential_list)
    # # print(len(influential_list))
    # assert False
    output_list = list()
    for row in influential_list:
        inner_list = list()
        inner_list.append(row[1])  # user name
        inner_list.append(row[2])  # No of tweets
        inner_list.append(tweetid_user_dict[row[1]])  # tweet_id
        inner_list.append(row[3])  # retweet_count
        inner_list.append(user_tweet_dict[row[1]])  # tweet
        inner_list.append(inf_score_user_dict[row[1]])  # global influential score
        output_list.append(inner_list)

    output_list = sorted(output_list, key=lambda x: float(x[5]), reverse=True)

    # print(output_list[0])
    # assert False

    with codecs.open('step_nine_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial Number\t" + "," + "Screen Name\t" + "," + "No of tweets\t" + "," + "tweet_id\t\t" + "," + "retweet_count\t" + "," + "Global Influence Score" + "," + "Tweet\n")
        count = 1
        comma = ","
        for row in output_list:
            line = (str(count) + comma + str(row[0]) + comma + str(row[1]) + comma + str(row[2]) +
                    comma + str(row[3]) + comma + str(row[5]) + comma + str(row[4]) + "\n")

            o.write(line)
            count += 1


if __name__ == "__main__":
    main()
