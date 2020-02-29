import tweepy
import json
import configparser

path = "keys"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(path)
    auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
                               config.get('auth', 'consumer_secret').strip())
    auth.set_access_token(config.get('auth', 'access_token').strip(),
                          config.get('auth', 'access_secret').strip())

    api = tweepy.API(auth)

    feed = []

    public_tweets = api.user_timeline(id="nytimes", count=1)

    status = public_tweets[0]
    json_str = json.dumps(status._json)

    with open('nytimes.json', 'w') as outfile:
        json.dump(json_str, outfile)
