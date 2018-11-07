import os
import codecs
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
from utils.FileReader import FileReader


def main():
    cluster_rows = dict()
    for i in range(10):
        filereader = FileReader(f"./full_tweets/cluster_{i}.csv")
        cluster_rows[i] = filereader.get_rows()
        with codecs.open("cluster_rows.csv", "w+") as o:
            o.write("Cluster Number" + "," + "User Name" + "," + "user_id\t" + "," + "No of Tweets\t\t" + "," + "Tweet_id\t" + ","
                    "Retweet Count\t" + "," + "Inf Score\t" + "," + "Tweet\n")
            for key, value in cluster_rows.items():
                lines = ""
                for v in value:
                    line = str(key)
                    line += ","
                    line += ",".join(v)
                    line += "\n"
                    lines += line
                o.write(lines)


if __name__ == "__main__":
    main()
