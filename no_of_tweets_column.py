import codecs
# import fileinput
import sys
import io
from collections import Counter

list_of_names = []
for_top_4 = []


def read_file(input_file):
    with codecs.open(str(input_file), 'r', 'utf-8') as f:
        for line in f:
            list_of_names.append(line)


def main():
    read_file(sys.argv[1])
    # print(list_of_names[1])
    c = Counter()
    for word in list_of_names:
        c[word] += 1

    # print(c)
    with io.open("added_column.txt", "w", encoding='utf-8') as f:
        f.write("Name" + "\t" + "Screen_Name" +
                "Id" + "\t" + "No_of_tweets" + "\n")
        for item in c:
            # print(c[item])
            # item = item.strip("\n")
            f.write(item.strip("\n") + "---" + str(c[item]) + "\n")

    with io.open("descending_order_of_no_of_tweets.txt", "w",
                 encoding='utf-8') as file:
        file.write("Name" + "\t\t" + "Screen_Name" + "\t\t" +
                   "Id" + "\t\t" + "No_of_tweets" + "\n")
        sorted_list = sorted(c, key=c.get, reverse=True)
        for key in sorted_list:
            file.write(key.strip("\n") + "---" + str(c[key]) + "\n")

    with codecs.open('descending_order_of_no_of_tweets.txt',
                     'r', 'utf-8') as i:
        four = open("top_4.txt", "w")
        four.write("Name" + "\t\t" + "Screen_Name" + "\t\t" +
                   "Id" + "\t\t" + "No_of_tweets" + "\n")
        for line in i:
            for_top_4.append(line)

        for i in range(1, 6):
            four.write(for_top_4[i])


if __name__ == '__main__':
    main()
