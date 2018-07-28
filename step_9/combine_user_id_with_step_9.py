import csv
import codecs


def read_file(filename):
    rows = list()
    with open(filename, "r") as f:
        csvreader = csv.reader(f)
        next(f)
        for row in csvreader:
            rows.append(row)
    return rows


def main():
    step_nine_rows = read_file("step_nine_output.csv")
    ids = read_file("user_user_id.csv")
    user_names = [i[0] for i in ids]
    user_ids = [i[1] for i in ids]
    user_names_and_ids = dict(zip(user_names, user_ids))
    # print(user_names_and_ids)
    user_names_from_nine = [i[1] for i in step_nine_rows]
    user_name_list = [i[2:] for i in step_nine_rows]
    user_names_nine = dict(zip(user_names_from_nine, user_name_list))
    with codecs.open('step_nine_with_id_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial Number\t" + "," + "Screen Name\t" + "," + "User Id\t" + "," + "No of tweets\t" + "," + "tweet_id\t\t" + "," + "retweet_count\t" + "," + "Global Influence Score" + "," + "Tweet\n")
        count = 1
        for user_name, user_id in user_names_and_ids.items():
            try:
                list_of_elements = user_names_nine[user_name]
                line = str(count) + "," + str(user_name) + "," + str(user_id) + "," + str(list_of_elements[0]) + "," + str(list_of_elements[1]) + "," + str(list_of_elements[2]) + "," + str(list_of_elements[3]) + "," + str(list_of_elements[4]) + "\n"
                o.write(line)
                count += 1
            except KeyError:
                pass


if __name__ == "__main__":
    main()
