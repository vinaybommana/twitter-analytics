import json
import subprocess
import codecs


def find_any_non_english_in_sentence(sentence):
    sentence = sentence.strip()
    for i in sentence:
        if ord(i) > 128 and ord(i) != 8211 and ord(i) != 8230:
            return True

    return False


def remove_unicode_characters(sentence):
    pass


def read_input_file():
    '''
    input file will be in the format
    <query_text> <begin_date> <end_date>
    <query_text> <begin_date> <end_date>
    '''
    input_details = list()
    with open("input", "r") as o:
        for line in o:
            input_details.append(line)

    return input_details


def read_json_file():
    with open('eng_tweets.json') as o:
        data = json.load(o)

    return data


def extract_tweets():
    input_details = read_input_file()
    for i in input_details:
        query_text = i.split()[0]
        begin_date = i.split()[1]
        end_date = i.split()[2]
        subprocess.call('twitterscraper {} --limit 100000 --lang en -bd {} -ed {} \
                        --output eng_tweets.json'.format(query_text, begin_date, end_date), shell=True)


def strip_unwanted(text):
    text = text.strip()
    text = text.replace(',', '')
    text = text.replace("'", "")
    text = text.replace('"', '')
    text = text.replace('\n', '')
    text = text.replace('\n\n', '')
    text = ''.join(text.splitlines())
    return text


def write_tweets_csv(data):
    with codecs.open("step_1_output.csv", "w+", "utf-8") as o:
        o.write("Serial_number" + "," + "User Name" + "," + "Screen_name\t" + "," + "Tweet Id\t\t" + ","
                "Retweet Count\t" + "," + "Date\t" + "," + "Tweet\n")
        count = 1
        for tweet in data:
            full_name = tweet['fullname'].strip()
            full_name = strip_unwanted(full_name)
            user = tweet['user']
            user = strip_unwanted(user)
            retweets = tweet['retweets']
            text = tweet['text'].strip()
            text = strip_unwanted(text)
            timestamp = tweet['timestamp']
            id = tweet['id']

            line = str(count) + "," + str(full_name) + "," + str(user) + "," + str(id) + "," + \
                   str(retweets) + "," + str(timestamp) + "," + str(text) + "\n"

            o.write(line)
            count += 1


def main():
    extract_tweets()
    write_tweets_csv(read_json_file())


if __name__ == "__main__":
    main()
