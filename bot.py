import tweepy

class Bot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = self.authentication()
        self.api = tweepy.API(self.auth)
        
    def authentication(self):
        self.auth = tweepy.OAuthHandler(
            self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(
            self.access_token, self.access_token_secret)
        return self.auth

    # write your method here