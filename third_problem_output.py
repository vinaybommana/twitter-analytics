import codecs
# import fileinput
import sys
# import io
from collections import Counter

list_of_names = []
for_top_4 = []
names = []
people_tweets = dict()


def read_file(input_file):
    with codecs.open(str(input_file), 'r', 'utf-8') as f:
        for line in f:
            list_of_names.append(line)


def main():
    read_file(sys.argv[1])
    # print(list_of_names[1])
    c = Counter()
    for line in list_of_names:
        if list_of_names.index(line) > 0:
            lines = line.split("---")
            if len(lines) == 4:
                if lines[0] in people_tweets:
                    people_tweets[lines[0]].append(lines[3].strip("\n"))
                else:
                    people_tweets[lines[0]] = [lines[3].strip("\n")]

                names.append(lines[0])

    for word in names:
        c[word] += 1

    sorted_list = sorted(c, key=c.get, reverse=True)
    count = 1
    with open("third_problem.txt", "w", encoding="utf-8") as f:
        f.write("Name" + "\t\t" + "Number of Tweets" + "\n")
        for name in sorted_list:
            # print(name + "\t" + str(c[name]))
            if count < 5:
                for_top_4.append(str(name) + "---" + str(c[name]))
                f.write(str(name) + "\t\t" + str(c[name]) + "\n")
            else:
                break

            count += 1

        f.write("\n\n")

        for user in for_top_4:
            for name in people_tweets:
                user_name = user.split("---")[0]
                if name == user_name:
                    f.write("\t\t" + user_name + "\n")
                    f.write("--------------------------------")
                    # print(name + "\n")
                    f.write("\nTweets:\n")
                    list_of_tweets = people_tweets[name]
                    for i, tweet in enumerate(list_of_tweets):
                        f.write(str(i + 1) + "  " + tweet)
                        f.write("\n\n")

                    f.write("\n\n")


if __name__ == '__main__':
    main()
