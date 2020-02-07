import argparse
import tweepy
import os
from dotenv import load_dotenv, set_key

parser = argparse.ArgumentParser()
parser.add_argument("-ck", "--consumer-key", help="set your consumer key here")
parser.add_argument("-cs", "--consumer-secret",
                    help="set your consumer secret here")

args = vars(parser.parse_args())

consumer_key = args["consumer_key"]
consumer_secret = args["consumer_secret"]

if consumer_key is not None and consumer_key is not None:

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    print("Please visit to authenticate: " + auth.get_authorization_url())

    oauth_token = auth.request_token["oauth_token"]
    oauth_token_secret = auth.request_token["oauth_token_secret"]

    auth.request_token['oauth_token'] = oauth_token
    auth.request_token['oauth_token_secret'] = oauth_token_secret

    verifier = input('Paste verifier code here: ')

    try:
        oa = auth.get_access_token(verifier)
        set_key(key_to_set="CONSUMER_KEY",
                value_to_set=consumer_key, dotenv_path=".env")
        set_key(key_to_set="CONSUMER_SECRET",
                value_to_set=consumer_secret, dotenv_path=".env")
        set_key(key_to_set="ACCESS_TOKEN",
                value_to_set=oa[0], dotenv_path=".env")
        set_key(key_to_set="ACCESS_SECRET",
                value_to_set=oa[1], dotenv_path=".env")
        print("bot connected with account")

    except tweepy.TweepError as e:
        print(e)

else:
    print('check existing file')

    load_dotenv()

    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")

    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        print("Please visit to authenticate: " + auth.get_authorization_url())
        oauth_token = auth.request_token["oauth_token"]
        oauth_token_secret = auth.request_token["oauth_token_secret"]

        auth.request_token['oauth_token'] = oauth_token
        auth.request_token['oauth_token_secret'] = oauth_token_secret

        verifier = input('Paste verifier code here: ')

        oa = auth.get_access_token(verifier)
        set_key(key_to_set="ACCESS_TOKEN",
                value_to_set=oa[0], dotenv_path=".env")
        set_key(key_to_set="ACCESS_SECRET",
                value_to_set=oa[1], dotenv_path=".env")
        print("bot connected with account")

    except tweepy.TweepError as e:
        print(e)
