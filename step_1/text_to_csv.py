import fileinput
import codecs

tweets_list = list()


def read_file():
    with codecs.open("problem_large.txt", "r") as r:
        for line in r:
            tweets_list.append(line)


def strip_unwanted(tweet):
    quote = '"'
    comma = ','
    tweet = tweet.replace(quote, "")
    tweet = tweet.replace(comma, "")
    return tweet


# serial_number , screen_name, user_id, tweet_id, retweet_count, date, tweet
# with codecs.open("step_one_output.csv", "a", "utf-8") as o:
#     o.write(str(tweet_variables[0]) + "," + str(tweet_variables[1]) + "," +
#             str(tweet_variables[2]) + "," + str(tweet_variables[3]) + "," +
#             str(tweet_variables[4]) + "," + str(tweet_variables[5]) + "," +
#             str(tweet_variables[6]) + "\n")


def main():
    read_file()
    with codecs.open("output.csv", "w+", "utf-8") as o:
        # serial_number , screen_name, user_id, tweet_id, retweet_count, date, tweet
        o.write("serial_number\t" + "," + "screen_name\t" + "," + "user_id\t" + "," + "tweet_id\t\t" + ","
                "retweet_count\t" + "," + "date\t" + "," + "tweet\n")

        for line in tweets_list:
            try:
                int(line.split("---")[0])
                tweet_variables = line.split("---")

                serial_number = tweet_variables[0]
                screen_name = tweet_variables[1]
                user_id = tweet_variables[2]
                tweet_id = tweet_variables[3]
                retweet_count = tweet_variables[4]
                date = tweet_variables[5]
                # removing unwanted commas and quotes
                # so that extra columns and merges do not occur
                tweet = tweet_variables[6]
                tweet = strip_unwanted(tweet)

                line = str(serial_number) + "," + str(screen_name) + "," + str(user_id) + "," + str(tweet_id) + "," + str(retweet_count) + "," + str(date) + "," + str(tweet)

                o.write(line)
                # o.write("\n")
            except:
                pass
    # for line in tweets_list:
    #     print(line)

if __name__ == "__main__":
    main()
