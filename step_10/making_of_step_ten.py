# step 10
import csv


def read_file():
    with open("step_10.1_output.csv", "r") as n:
        csvreader = csv.reader(n)
        next(csvreader)
        for row in csvreader:
            ninth_rows.append(row)


def clean_tweets(list_of_tweets):
    for i in list_of_tweets:
        if "RT @" in i:
            tweet = i.split(":")[1]
        else:
            tweet = i

        tweet = tweet.strip("…")
        print(tweet)


ninth_rows = list()
list_of_tweets = list()


def main():
    read_file()
    list_of_tweets = [i[6] for i in ninth_rows]
    clean_tweets(list_of_tweets)


if __name__ == "__main__":
    main()
