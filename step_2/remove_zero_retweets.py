import csv
import codecs


def read_csv():
    with open("step_1_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


def main():
    read_csv()
    # print(len(rows))
    with codecs.open("step_two_output.csv", "w", "utf-8") as o:
        # serial_number , screen_name, user_id, tweet_id, retweet_count, date, tweet
        o.write("Serial Number\t" + "," + "User Name\t" + "," + "@mention\t" + "," + "Tweet_id\t\t" + ","
                "Retweet Count\t" + "," + "Date\t" + "," + "Tweet\n")

        for row in rows:
            if row[4] != '0':
                line = ""
                for string in row[1:]:
                    line += string
                    line += ","
                line += "\n"
                # print(line)
                o.write(line)


rows = list()
if __name__ == "__main__":
    main()
