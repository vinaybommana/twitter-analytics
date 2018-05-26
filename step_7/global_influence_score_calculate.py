import csv
import codecs


def read_csv():
    with open("step_five_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


rows = list()


def main():
    read_csv()
    with codecs.open('step_seven_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "user_id\t\t" + "," + "No of Tweets" + "," +
                "No of retweets" + "," + "global influence score\n")
        for row in rows:
            line = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + \
                   str(row[3]) + "," + str(row[4]) + "," + str(int(row[4]) / int(row[3])) + "\n"
            o.write(line)


if __name__ == "__main__":
    main()


