
# Step one

Collect one lakh tweets on a specific domain name and duration as input

#### Example

##### input
sports

##### output format:

|serial_number | screen_name| user_id| tweet_id| retweet_count| date| tweet|
| ---          |  ----------| -------| --------| --------     | --- | ---- |
| 1            | lorem      | ip     | 12      | 1            | 23  | xh   |


we'll be using [`twitterscraper`](https://github.com/taspinar/twitterscraper) for this purpose.



```bash
%%bash
twitterscraper python --limit 1000 --lang en --output ~/backups/today\'stweets.json
```

    INFO: queries: ['python since:2006-03-21 until:2006-11-12', 'python since:2006-11-12 until:2007-07-06', 'python since:2007-07-06 until:2008-02-27', 'python since:2008-02-27 until:2008-10-20', 'python since:2008-10-20 until:2009-06-13', 'python since:2009-06-13 until:2010-02-04', 'python since:2010-02-04 until:2010-09-29', 'python since:2010-09-29 until:2011-05-23', 'python since:2011-05-23 until:2012-01-14', 'python since:2012-01-14 until:2012-09-06', 'python since:2012-09-06 until:2013-04-30', 'python since:2013-04-30 until:2013-12-22', 'python since:2013-12-22 until:2014-08-15', 'python since:2014-08-15 until:2015-04-09', 'python since:2015-04-09 until:2015-12-01', 'python since:2015-12-01 until:2016-07-24', 'python since:2016-07-24 until:2017-03-17', 'python since:2017-03-17 until:2017-11-08', 'python since:2017-11-08 until:2018-07-02', 'python since:2018-07-02 until:2019-02-24']
    INFO: Querying python since:2006-03-21 until:2006-11-12
    INFO: Querying python since:2006-11-12 until:2007-07-06
    INFO: Querying python since:2007-07-06 until:2008-02-27
    INFO: Querying python since:2008-02-27 until:2008-10-20
    INFO: Querying python since:2008-10-20 until:2009-06-13
    INFO: Querying python since:2009-06-13 until:2010-02-04
    INFO: Querying python since:2010-02-04 until:2010-09-29
    INFO: Querying python since:2011-05-23 until:2012-01-14
    INFO: Querying python since:2010-09-29 until:2011-05-23
    INFO: Querying python since:2012-01-14 until:2012-09-06
    INFO: Querying python since:2012-09-06 until:2013-04-30
    INFO: Querying python since:2013-04-30 until:2013-12-22
    INFO: Querying python since:2013-12-22 until:2014-08-15
    INFO: Querying python since:2014-08-15 until:2015-04-09
    INFO: Querying python since:2015-12-01 until:2016-07-24
    INFO: Querying python since:2015-04-09 until:2015-12-01
    INFO: Querying python since:2017-11-08 until:2018-07-02
    INFO: Querying python since:2017-03-17 until:2017-11-08
    INFO: Querying python since:2016-07-24 until:2017-03-17
    INFO: Querying python since:2018-07-02 until:2019-02-24
    INFO: Got 5 tweets for python%20since%3A2006-03-21%20until%3A2006-11-12.
    INFO: Got 5 tweets (5 new).
    INFO: Got 60 tweets for python%20since%3A2008-10-20%20until%3A2009-06-13.
    INFO: Got 65 tweets (60 new).
    INFO: Got 54 tweets for python%20since%3A2015-12-01%20until%3A2016-07-24.
    INFO: Got 119 tweets (54 new).
    INFO: Got 60 tweets for python%20since%3A2017-03-17%20until%3A2017-11-08.
    INFO: Got 179 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2010-02-04%20until%3A2010-09-29.
    INFO: Got 239 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2013-12-22%20until%3A2014-08-15.
    INFO: Got 299 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2010-09-29%20until%3A2011-05-23.
    INFO: Got 359 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2014-08-15%20until%3A2015-04-09.
    INFO: Got 419 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2006-11-12%20until%3A2007-07-06.
    INFO: Got 479 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2015-04-09%20until%3A2015-12-01.
    INFO: Got 539 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2009-06-13%20until%3A2010-02-04.
    INFO: Got 599 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2007-07-06%20until%3A2008-02-27.
    INFO: Got 659 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2018-07-02%20until%3A2019-02-24.
    INFO: Got 719 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2011-05-23%20until%3A2012-01-14.
    INFO: Got 779 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2016-07-24%20until%3A2017-03-17.
    INFO: Got 839 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2013-04-30%20until%3A2013-12-22.
    INFO: Got 899 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2017-11-08%20until%3A2018-07-02.
    INFO: Got 959 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2012-09-06%20until%3A2013-04-30.
    INFO: Got 1019 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2012-01-14%20until%3A2012-09-06.
    INFO: Got 1079 tweets (60 new).
    INFO: Got 60 tweets for python%20since%3A2008-02-27%20until%3A2008-10-20.
    INFO: Got 1139 tweets (60 new).



```python
import codecs
import json
import pandas as pd
from typing import List, Dict

def load_json_file(file_path: str) -> Dict:
    with codecs.open(file_path, "r", "utf-8") as f:
        return json.load(f, encoding="utf-8")
    
tweets = load_json_file("/home/vinay/backups/today\'stweets.json")

list_tweets = [list(elem.values()) for elem in tweets]
list_columns = list(tweets[0].keys())

twitter_data = pd.DataFrame(list_tweets, columns=list_columns)
twitter_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>url</th>
      <th>text</th>
      <th>user</th>
      <th>html</th>
      <th>retweets</th>
      <th>replies</th>
      <th>fullname</th>
      <th>id</th>
      <th>likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-11-08T11:46:29</td>
      <td>/larskflem/status/59306</td>
      <td>coding python. happy time</td>
      <td>larskflem</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>Lars K. Flem</td>
      <td>59306</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-11-06T21:20:39</td>
      <td>/sergio_101/status/57683</td>
      <td>Trying to figure out what phone to get next.. ...</td>
      <td>sergio_101</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>sergio t. ruiz</td>
      <td>57683</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-10-23T00:21:20</td>
      <td>/thomasknoll/status/46836</td>
      <td>Learning python while kim watches city of god</td>
      <td>thomasknoll</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>Thomas Knoll</td>
      <td>46836</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-08-02T02:07:24</td>
      <td>/marceloeduardo/status/15613</td>
      <td>Finishing some turbogears experience, writing ...</td>
      <td>marceloeduardo</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>1</td>
      <td>0</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-07-16T18:03:45</td>
      <td>/nitin/status/10584</td>
      <td>Heading to peets in emryvil to hack python tnx...</td>
      <td>nitin</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>1</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



We can drop columns `html`, `url`, `likes`, `replies`.

We need to modify `timestamp` column, add `user` and `fullname` columns.
and get user_ids of the `user`.

order the columns, based on the given output format


```python
# making timestamp YYYY-MM-DD
twitter_data['timestamp'] = twitter_data['timestamp'].apply(lambda x: x.split('T')[0])

# dropping html, url, likes and replies
twitter_data.drop(columns=['html', 'url', 'likes', 'replies'], inplace=True)

# twitter_data.head()
twitter_data.columns
```




    Index(['timestamp', 'text', 'user', 'retweets', 'fullname', 'id'], dtype='object')




```python
# renaming column names
twitter_data.columns = ['Date', 'Tweet', 'user', 'retweets', 'fullname', 'Tweet_id']

twitter_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Tweet</th>
      <th>user</th>
      <th>retweets</th>
      <th>fullname</th>
      <th>Tweet_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-11-08</td>
      <td>coding python. happy time</td>
      <td>larskflem</td>
      <td>0</td>
      <td>Lars K. Flem</td>
      <td>59306</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-11-06</td>
      <td>Trying to figure out what phone to get next.. ...</td>
      <td>sergio_101</td>
      <td>0</td>
      <td>sergio t. ruiz</td>
      <td>57683</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-10-23</td>
      <td>Learning python while kim watches city of god</td>
      <td>thomasknoll</td>
      <td>0</td>
      <td>Thomas Knoll</td>
      <td>46836</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-08-02</td>
      <td>Finishing some turbogears experience, writing ...</td>
      <td>marceloeduardo</td>
      <td>1</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-07-16</td>
      <td>Heading to peets in emryvil to hack python tnx...</td>
      <td>nitin</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
    </tr>
  </tbody>
</table>
</div>



## Step 2
from the step 1 output observe( 5th column of the table) i.e number of re tweets obtained for each tweet . If number of re tweets obtained for the given tweet is 0 then discard the tweet other wise print the tweet in the above format.

Output : print only the tweets which got re tweets and discard the tweets with no re tweets

This will contain the tweets with more than zero retweets.


```python
twitter_data = twitter_data[twitter_data.retweets != "0"]
twitter_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Tweet</th>
      <th>user</th>
      <th>retweets</th>
      <th>fullname</th>
      <th>Tweet_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2006-08-02</td>
      <td>Finishing some turbogears experience, writing ...</td>
      <td>marceloeduardo</td>
      <td>1</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-07-16</td>
      <td>Heading to peets in emryvil to hack python tnx...</td>
      <td>nitin</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
    </tr>
    <tr>
      <th>66</th>
      <td>2016-07-23</td>
      <td>tethne 0.8.1.dev8: Bibliographic network and c...</td>
      <td>mastercodeonlin</td>
      <td>1</td>
      <td>MasterCode.Online</td>
      <td>757001950088957952</td>
    </tr>
    <tr>
      <th>71</th>
      <td>2016-07-23</td>
      <td>Thank @mandarlimaye 4 your follow and welcom #...</td>
      <td>lennincaro</td>
      <td>3</td>
      <td>Lennin Caro</td>
      <td>757000314071478272</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016-07-23</td>
      <td>Thank @h1ng 4 your follow and welcom #PostgreS...</td>
      <td>lennincaro</td>
      <td>4</td>
      <td>Lennin Caro</td>
      <td>757000213622030336</td>
    </tr>
  </tbody>
</table>
</div>



## for step three

Step 3: Find out number of users who has been tweeted those tweets in step 2, because one user may post multiple tweets.

Input: output of step 2

Output:

|serial_number | user_name @mention | user_id | tweets (no of tweets posted by user) |
| ----         |  ----------        | ------- | --------                             |
|              |                    |         |                                      |


```python
# for step 3 date column is irrelevant
# remove first date column
twitter_data_with_date = twitter_data
twitter_data.drop(columns=['Date', 'Tweet'], inplace=True)
twitter_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>retweets</th>
      <th>fullname</th>
      <th>Tweet_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>marceloeduardo</td>
      <td>1</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
    </tr>
    <tr>
      <th>4</th>
      <td>nitin</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
    </tr>
    <tr>
      <th>66</th>
      <td>mastercodeonlin</td>
      <td>1</td>
      <td>MasterCode.Online</td>
      <td>757001950088957952</td>
    </tr>
    <tr>
      <th>71</th>
      <td>lennincaro</td>
      <td>3</td>
      <td>Lennin Caro</td>
      <td>757000314071478272</td>
    </tr>
    <tr>
      <th>72</th>
      <td>lennincaro</td>
      <td>4</td>
      <td>Lennin Caro</td>
      <td>757000213622030336</td>
    </tr>
  </tbody>
</table>
</div>




```python
# rather than dropping duplicated we can `groupby` in pandas
# twitter_data.duplicated(subset='user', keep='first').sum()
tweet_count = twitter_data.groupby(twitter_data.user.tolist(),as_index=False).size()
tweet_count['mastercodeonlin']
```




    2




```python
def get_tweet_count(user: str) -> int:
    return tweet_count[user]

get_tweet_count('mastercodeonlin')
```




    2




```python
twitter_data['no_of_tweets'] = twitter_data['user'].apply(lambda x: get_tweet_count(x))

twitter_data_without_tweet_count = twitter_data.drop_duplicates(subset='user', keep="first")
twitter_data_without_tweet_count.reset_index(drop=True, inplace=True)
twitter_data_without_tweet_count.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user</th>
      <th>retweets</th>
      <th>fullname</th>
      <th>Tweet_id</th>
      <th>no_of_tweets</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>marceloeduardo</td>
      <td>1</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>nitin</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>mastercodeonlin</td>
      <td>1</td>
      <td>MasterCode.Online</td>
      <td>757001950088957952</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lennincaro</td>
      <td>3</td>
      <td>Lennin Caro</td>
      <td>757000314071478272</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>devbattles</td>
      <td>9</td>
      <td>Dev Battles</td>
      <td>756996796786900993</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# in order to get user_id for a user
# we need to use tweepy, need to work on getting user_ids twitterscraper way.

import tweepy

configs = load_json_file("configs.json")

APP_KEY = configs['APP_KEY']
APP_SECRET = configs['APP_SECRET']

# authenticate api
auth = tweepy.AppAuthHandler(APP_KEY, APP_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)
```


```python
# get user_id from screen name
def get_user_id_from_screen_name(screen_name: str, api: object) -> int:
    try:
        id = api.get_user(screen_name=screen_name).id
#         print(id)
        return id
    except tweepy.TweepError:
        return None

get_user_id_from_screen_name("nitin", api)
```




    988




```python
twitter_data_without_tweet_count['user_id'] = twitter_data_without_tweet_count['user'].apply(lambda x: int(get_user_id_from_screen_name(x, api)))
```


```python
twitter_data_without_tweet_count.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamp</th>
      <th>url</th>
      <th>text</th>
      <th>user</th>
      <th>html</th>
      <th>retweets</th>
      <th>replies</th>
      <th>fullname</th>
      <th>id</th>
      <th>likes</th>
      <th>user_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2006-11-08T11:46:29</td>
      <td>/larskflem/status/59306</td>
      <td>coding python. happy time</td>
      <td>larskflem</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>Lars K. Flem</td>
      <td>59306</td>
      <td>0</td>
      <td>11721.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2006-11-06T21:20:39</td>
      <td>/sergio_101/status/57683</td>
      <td>Trying to figure out what phone to get next.. ...</td>
      <td>sergio_101</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>sergio t. ruiz</td>
      <td>57683</td>
      <td>0</td>
      <td>2676.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2006-10-23T00:21:20</td>
      <td>/thomasknoll/status/46836</td>
      <td>Learning python while kim watches city of god</td>
      <td>thomasknoll</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>0</td>
      <td>0</td>
      <td>Thomas Knoll</td>
      <td>46836</td>
      <td>0</td>
      <td>2874.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2006-08-02T02:07:24</td>
      <td>/marceloeduardo/status/15613</td>
      <td>Finishing some turbogears experience, writing ...</td>
      <td>marceloeduardo</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>1</td>
      <td>0</td>
      <td>Marcelo Eduardo</td>
      <td>15613</td>
      <td>1</td>
      <td>3652.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2006-07-16T18:03:45</td>
      <td>/nitin/status/10584</td>
      <td>Heading to peets in emryvil to hack python tnx...</td>
      <td>nitin</td>
      <td>&lt;p class="TweetTextSize js-tweet-text tweet-te...</td>
      <td>1</td>
      <td>1</td>
      <td>Nitin Borwankar</td>
      <td>10584</td>
      <td>1</td>
      <td>988.0</td>
    </tr>
  </tbody>
</table>
</div>


