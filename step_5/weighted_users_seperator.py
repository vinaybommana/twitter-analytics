import csv
import codecs


def read_csv():
    rows = list()
    with open("step_four_output.csv", "r") as c:
        csvreader = csv.reader(c)
        next(csvreader)
        for row in csvreader:
            rows.append(row)
    return rows


def main():
    rows = read_csv()
    for i in rows:
        if float(i[4]) > 1.5:
            weighted_rows.append(i)

    with codecs.open('step_five_output.csv', 'w+', 'utf-8') as o:
        o.write("Serial_number\t" + "," + "screen_name\t" + "," + "No of Tweets" + "," +
                "No of retweets" + "," + "weighted_users\n")
        count = 1
        for row in weighted_rows:
            line = str(count) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + \
                   str(row[4])+ "\n"
            o.write(line)
            count += 1


weighted_rows = list()


if __name__ == "__main__":
    main()
