import codecs
import csv


csv_file = csv.writer(open("descending_order.csv", "w"))
csv_file.writerow(["Name", "Screen_Name", "Id", "No of Tweets"])

list_in_the_lines = []

with codecs.open("descending_order_of_no_of_tweets.txt", "r") as f:
    header_line = next(f)
    for line in f:
        list_in_the_lines = line.split("---")
        # list_in_the_lines = list_in_the_lines[1:]
        list_in_the_lines = [str(i).strip("\n") for i in list_in_the_lines]
        # print(list_in_the_lines)
        csv_file.writerow(list_in_the_lines)

csv_file = csv.writer(open("top_4.csv", "w"))
csv_file.writerow(["Name", "Screen_Name", "Id", "No of Tweets"])

with codecs.open("top_4.txt", "r") as f:
    header_line = next(f)
    for line in f:
        list_in_the_lines = line.split("---")
        # list_in_the_lines = list_in_the_lines[1:]
        list_in_the_lines = [str(i).strip("\n") for i in list_in_the_lines]
        # print(list_in_the_lines)
        csv_file.writerow(list_in_the_lines)
