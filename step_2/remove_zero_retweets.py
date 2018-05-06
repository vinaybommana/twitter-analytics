import csv
import codecs


def read_csv():
    with open("output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)


def main():
    read_csv()
    with codecs.open("step_two_output.csv", "w+", "utf-8") as o:
        # serial_number , screen_name, user_id, tweet_id, retweet_count, date, tweet
        o.write("serial_number\t" + "," + "screen_name\t" + "," + "user_id\t" + "," + "tweet_id\t\t" + ","
                "retweet_count\t" + "," + "date\t" + "," + "tweet\n")
        for row in rows:
            if row[4] != '0':
                line = ""
                for string in row:
                    line += string
                    line += ","
                line += "\n"
                o.write(line)
    

rows = list()
if __name__ == "__main__":
    main()
