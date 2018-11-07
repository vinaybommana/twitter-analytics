'''
read every cluster_<num>.csv in full and three_fifth
arrange based on local influential score
'''

import csv
from give_tables_for_clusters import read_csv


def main():
    for i in range(10):
        rows = read_csv('./full_tweets/cluster_' + str(i) + '.csv')
        rows = sorted(rows, key=lambda x: float(x[5]), reverse=True)
        with open('cluster_' + str(i) + '_with_rank.csv', 'w') as c:
            c.write("Descending order of local infl score" + "," + "user@mention" + "," + "Rank\n")
            count = 1
            for row in rows:
                line = str(row[5]) + "," + str(row[0]) + "," + str(count) + "\n"
                c.write(line)
                count += 1

    for i in range(10):
        rows = read_csv('./three_fifth_of_the_tweets/three_fifth_cluster_' + str(i) + '.csv')
        rows = sorted(rows, key=lambda x: float(x[5]), reverse=True)
        with open('three_fifth_cluster_' + str(i) + '_with_rank.csv', 'w') as c:
            c.write("Descending order of local infl score" + "," + "user@mention" + "," + "Rank\n")
            count = 1
            for row in rows:
                line = str(row[5]) + "," + str(row[0]) + "," + str(count) + "\n"
                c.write(line)
                count += 1


if __name__ == "__main__":
    main()

