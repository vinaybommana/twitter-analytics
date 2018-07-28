import urllib.request as url_req
from bs4 import BeautifulSoup
import codecs
import time


def search_user_id(user_name):
    soup = BeautifulSoup(url_req.urlopen('http://gettwitterid.com/?user_name={}&submit=GET+USER+ID'.format(user_name)), 'html.parser')
    list_of_para = [i.get_text() for i in soup.find_all('p')]
    if len(list_of_para) > 2:
        return list_of_para[2]
    else:
        return None


def read_user_names():
    user_names = list()
    with codecs.open("step_nine_output.csv", encoding="utf-8") as o:
        next(o)
        for line in o:
            user_name = line.split(",")[1]
            user_names.append(user_name)
    return user_names


def main():
    user_names = read_user_names()
    user_ids = list()

    with codecs.open("user_user_id.csv", "w+", "utf-8") as u:
        line = "User Name\t" + "," + "User Id\t" + "\n"
        u.write(line)
        for user in user_names:
            user_id = search_user_id(user)
            if user_id is not None:
                user_ids.append(user_id)
                line = user + "," + user_id + "\n"
                u.write(line)
                time.sleep(1)
            else:
                pass


if __name__ == '__main__':
    main()
