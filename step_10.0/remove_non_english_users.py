import csv
import codecs


def read_file():
    with open("step_nine_output.csv", "r") as n:
        csvreader = csv.reader(n)
        next(csvreader)
        for row in csvreader:
            ninth_rows.append(row)


def read_ten_zero():
    with open("step_10.0_output.csv", "r") as t:
        csvreader = csv.reader(t)
        next(csvreader)
        for row in csvreader:
            tenth_rows.append(row)


def find_any_non_english_in_sentence(sentence):
    # print(sentence)
    for i in sentence:
        if ord(i) > 128 and ord(i) != 8211 and ord(i) != 8230:
            # print(ord(i), end=' ')
            # print()
            return True
    # print(sentence)
    return False


def remove_non_english_users():
    for i in ninth_rows:
        if find_any_non_english_in_sentence(i[6]):
            # print(i[6])
            pass
        else:
            english_rows.append(i)


def remove_repeated_users(english_rows):
    for i in english_rows:
        line = i[1] + "," + i[2] + "," + i[3] + "," + i[4] + "," + str(float(i[5])) + "," + i[6] + "\n"
        non_repeated_rows.append(line)
    # print(len(non_repeated_rows))
    rows = set(non_repeated_rows)
    # print(len(rows))
    return rows


# def get_list_of_tweet_id(english_rows):
#     for i in english_rows:
#         tweet_ids.append(i[2])


# def reduce_repeated_tweet_ids(tweet_ids):
#     print(len(tweet_ids))
#     tweet_ids = set(tweet_ids)
#     print(len(tweet_ids))
#     return tweet_ids


def write_ten_zero_file(english_rows):
    english_rows = remove_repeated_users(english_rows)
    # print(len(english_rows))
    with codecs.open("step_10.0_output.csv", "w+", "utf-8") as o:
        o.write("Screen Name\t" + "," + "user_id\t\t" + "," + "tweet_id\t\t" + "," + "retweet_count\t" + "," + "Global Influence Score" + "," + "Tweet\n")
        for i in english_rows:
            o.write(i)


def write_ten_one_file(rows):
    with codecs.open("step_10.1_output.csv", "w+", "utf-8") as t:
        t.write("Rank\t" + "," + "Screen Name\t" + "," + "user_id\t\t" + "," + "tweet_id\t\t" + "," + "retweet_count\t" + "," + "Global Influence Score" + "," + "Tweet\n")
        count = 1
        for i in rows:
            line = str(count) + "," + i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "," + i[4] + "," + i[5] + "\n"
            t.write(line)
            count += 1


ninth_rows = list()
english_rows = list()
non_repeated_rows = list()
tweet_ids = list()
tenth_rows = list()


def main():
    read_file()
    remove_non_english_users()
    write_ten_zero_file(english_rows)
    read_ten_zero()
    output_rows = sorted(tenth_rows, key=lambda x: float(x[4]), reverse=True)
    # print(output_rows[0])
    # print(len(output_rows))
    write_ten_one_file(output_rows)


if __name__ == "__main__":
    main()
