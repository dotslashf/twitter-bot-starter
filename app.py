from bot import Bot
import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


def main(ck, cs, at, ats):
    bot = Bot(ck, cs, at, ats)

    while True:
        # do your method here by calling the bot object


if __name__ == "__main__":
    main(consumer_key, consumer_secret, access_token, access_token_secret)
