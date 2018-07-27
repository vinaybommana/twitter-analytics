import urllib.request as url_req
from bs4 import BeautifulSoup
import codecs


def main():
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
        # for para in soup.find_all('p'):
        #     list_of_nothing = [i for i in para.get_text()]
        list_of_nothing = [i.get_text() for i in soup.find_all('p')]
        try:
            user_id = list_of_nothing[2]
        except IndexError:
            print(list_of_nothing)
            print(user)
        user_ids.append(user_id)

    print(len(user_ids))


if __name__ == '__main__':
    main()
