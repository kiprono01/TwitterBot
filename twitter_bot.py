import os as _os
import dotenv as _dotenv
import time as _time
import tweepy as _tweepy
from tweepy.auth import OAuthHandler


import services as _services
import unsplash as _unsplash

_dotenv.load_dotenv()

API_KEY = _os.environ["Twitter_API_Key"]
SECRET_KEY = _os.environ["Twitter_API_Secret_Key"]
ACCESS_TOKEN = _os.environ["Twitter_Access_Token"]
ACCESS_TOKEN_SECRET = _os.environ["Twitter_Access_Token_Secret"]


def _get_twitter_api():
    auth = _tweepy.OAuthHandler(API_KEY, SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    twitter_api = _tweepy.API(auth, wait_on_rate_limit=True)

    return twitter_api

def _write_tweet():
    tweet = _services.get_tweet()
    twitter_api = _get_twitter_api()
    twitter_api.update_status(tweet)


_write_tweet()

