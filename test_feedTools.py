import feedTools as ft
import os
import tweepy
import json
import testImage

with open('nytimes.json') as json_file:
    json_data = json.load(json_file)


def test_getFeed():
    if os.stat("keys").st_size == 0:
        status_json = json.loads(json_data)
        assert status_json['text'] == "The public health director of Santa Clara County, California, confirmed that the county's new coronavirus case does… https://t.co/hl8ClztVbL"
    else:
        data = ft.getFeed("BleacherReport", 1)
        assert len(data[0]['text']) > 0


def test_annotateImage(capsys):
    if os.stat("keys").st_size == 0:
        assert testImage.description == "Blue, Cool, T-shirt, Outerwear, Facial hair, Beard, Rapper, Sleeve, Top"
    else:
        description = ft.annotateImage(testImage.url)
        assert description == "Blue, Cool, T-shirt, Outerwear, Facial hair, Beard, Rapper, Sleeve, Top"


if __name__ == "__main__":
    test_getFeed()
