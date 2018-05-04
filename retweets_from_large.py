import codecs

retweets = list()
with codecs.open("./problem_large.txt", "r") as s:
    # for neglecting the first name user_id row
    next(s)
    for line in s:
        tweet_list = line.split("---")
        try:
            if tweet_list[3].startswith("RT"):
                retweets.append(tweet_list[3])
        except IndexError:
            pass

# print(len(retweets))
# writing the entire retweets to file
# retweets.txt

with open("retweets.txt", "w", encoding="utf-8") as r:
    r.write("Number" + "\t\t" + "Tweet\n")
    for i, v in enumerate(retweets):
        r.write(str(i) + "\t\t" + v)

    r.write("\n\n")
