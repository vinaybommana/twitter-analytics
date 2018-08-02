import urllib.request as url_req
from bs4 import BeautifulSoup
import csv
import codecs
import time
import tweepy
import sys

APP_KEY = 'BlHVe4NazxtdbPgx386iUV6MZ'
APP_SECRET = 'f2Hhq39zzPeIaU3mQZgqki2he4ncTXEE8dOglTJtDOl193LK3l'

auth = tweepy.AppAuthHandler(APP_KEY, APP_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)


def read_ninth_csv_file():
    user_names = list()
    with codecs.open("step_nine_output.csv", encoding="utf-8") as o:
        csvreader = csv.reader(o)
        next(csvreader)
        for row in csvreader:
            user_names.append(row[1])

    return user_names


def get_users_from_web():
    user_names = list()
    user_ids = list()
    with codecs.open("step_nine_output.csv", encoding="utf-8") as o:
        next(o)
        for line in o:
            user_name = line.split(",")[1]
            # print(user_name)
            user_names.append(user_name)
            # print(line[1])

    for user in user_names:
        soup = BeautifulSoup(url_req.urlopen('http://gettwitterid.com/?user_name={}&submit=GET+USER+ID'.format(user)), 'html.parser')
        time.sleep(2)
        # for para in soup.find_all('p'):
        #     list_of_nothing = [i for i in para.get_text()]
        list_of_nothing = [i.get_text() for i in soup.find_all('p')]
        try:
            user_id = list_of_nothing[2]
            print(user, end=' ')
            print(user_id)
        except IndexError:
            print(list_of_nothing)
            print(user)
        user_ids.append(user_id)

    print(len(user_ids))


def main():
    user_names = read_ninth_csv_file()
    user_ids = list()
    i = 0
    while i <= len(user_names):
        screen_names = user_names[i: i + 100]  # 100 user names
        user_ids.append(get_user_ids_from_api(screen_names))
        print(len(user_ids))
        i += 100

    user_ids = [x for i in user_ids for x in i]

    with codecs.open("user_user_id.csv", "w+", "utf-8") as u:
        line = "User Name\t" + "," + "User Id\t" + "\n"
        u.write(line)
        for user_id_tuple in user_ids:
            line = str(user_id_tuple[0]) + "," + str(user_id_tuple[1]) + "\n"
            u.write(line)


def get_user_ids_from_api(users):
    user_objects = api.lookup_users(screen_names=users)
    list_of_ids = [(user.screen_name, user.id_str) for user in user_objects]
    return list_of_ids


if __name__ == '__main__':
    main()
