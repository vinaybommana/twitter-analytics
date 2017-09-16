# twitter-analytics
twitter scrapers for analysis

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
```python3
python3 no_of_tweets_column.py large
```

* This will produce `top_4.txt` and `added_column.txt`
* The `top_4.txt` has the top 4 persons who has tweeted most tweeted most
* The `added_column.txt` has the list of all the persons who has tweeted
  in the order of their tweet count.

### for downloading required libraries
```bash
pip3 install -r requirements.txt
```

* for machines with only a single python installed we can use `pip` directly instead of pip3
