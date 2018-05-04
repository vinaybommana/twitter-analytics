# twitter-analytics
twitter scrapers for analysis

* for running the scripts given in the steps following libraries are used.

* `tweepy`
* `jsonpickle`

### for downloading required libraries
```bash
pip3 install -r requirements.txt
```

* for machines with only a single python installed we can use `pip` directly instead of `pip3`

## for step one

### format for the step one

|serial_number | screen_name| user_id| tweet_id| retweet_count| date| tweet|
| ----         |  ----------| -------| --------| --------     | --- | ---- |
|              |            |        |         |              |     |      |

```python3
python3 extract_tweets.py input
```
* This will download the tweets in `problem_large.txt` file.
* Then run the following command.

```python3
python3 txt_to_csv.py
```
* This will produce `output.csv` file.

### Running the scraper
```python3
python3 main_scraper_twitter.py input
```

* this will download the tweets based on the input file
* we can change the no of tweets that can be scraped.
* Just change the maxqueries in the `main_scraper_twitter.py`
* The `main_scraper_twitter.py` uses `tweepy` and `jsonpickle`
* This will produce the `large.txt` file

### for obtaining the no of tweet count
```bash
python3 no_of_tweets_column.py large.txt
```

* This will produce `top_4.txt` and `added_column.txt`
* The `top_4.txt` has the top 4 persons who has tweeted most tweeted most
* The `added_column.txt` has the list of all the persons who has tweeted
  in the order of their tweet count.


### Problem 1
* scraping large number of users from twitter
* who tweeted about a particular topic in a specified interval of time

### Problem 2
* arranging the users in the order of the number of tweets they made.

### Problem 3
* finding the users who tweeted the most in a specified interval of time.
* giving their tweets

```bash
python3 third_problem_output.py large.txt
```

* this will produce a txt file `third_problem.txt`
