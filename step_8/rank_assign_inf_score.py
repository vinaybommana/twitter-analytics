import csv
import codecs


def read_csv():
    with open("step_seven_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


rows = list()


def main():
    read_csv()
    sorted_rows = sorted(rows, key=lambda x: x[5], reverse=True)
    # print(sorted_rows)

    # step eight output with only given table format
    with codecs.open('step_eight_output_rank.csv', 'w+', 'utf-8') as o:
        o.write("Global_influence_score\t" + "," + "screen_name\t" + "," + "Global_rank\n")
        rank = 1
        for row in sorted_rows:
            line = str(row[5]) + "," + str(row[1]) + "," + str(rank) + str("\n")
            o.write(line)
            rank += 1

    # step eight output with no of tweets and retweets
    with codecs.open('step_eight_output_info', 'w+', 'utf-8') as o:
        o.write("Global_rank\t" + "," + "screen_name\t" + "," + "user_id\t\t" + "," + "No of Tweets\t" + "," + "No of retweets\t" + "," + "Global_influence_score\n")
        rank = 1
        for row in sorted_rows:
            line = str(rank) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "," + str(row[5])
            line += str("\n")
            o.write(line)
            rank += 1


if __name__ == "__main__":
    main()
