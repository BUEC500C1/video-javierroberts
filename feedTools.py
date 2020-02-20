import tweepy
import keys
from google.cloud import vision
import io
from PIL import Image
import urllib.request
import os

os.system(
    "export GOOGLE_APPLICATION_CREDENTIALS=~/Documents/gcloudstuff/apikey.json")


def getFeed(handle, count):
    auth = tweepy.OAuthHandler(keys.key, keys.skey)
    auth.set_access_token(keys.token, keys.stoken)

    api = tweepy.API(auth)

    feed = []

    public_tweets = api.user_timeline(id=handle, count=count)

    for tweet in public_tweets:
        entry = {}
        entry.update({"text": tweet.text})
        if 'media' in tweet.entities:
            for media in tweet.entities["media"]:
                entry.update(
                    {"image description": annotateImage(media["media_url"])})

        feed.append(entry)
    return feed


def annotateImage(URL):
    client = vision.ImageAnnotatorClient()

    with urllib.request.urlopen(URL) as url:
        f = io.BytesIO(url.read())

    content_jpeg = Image.open(f)

    imgByteArr = io.BytesIO()
    content_jpeg.save(imgByteArr, format=content_jpeg.format)
    content = imgByteArr.getvalue()

    image = vision.types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    summary = ""

    for label in labels:
        summary += label.description
        summary += ", "

    summary = summary[: -2]

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return summary


if __name__ == "__main__":
    annotateImage(
        "https://pbs.twimg.com/profile_images/927446347879292930/Fi0D7FGJ_400x400.jpg")
