import feedTools as ft
import os
import tweepy
import json
import testImage

with open('nytimes.json') as json_file:
    status_json = json.load(json_file)


def test_getFeed(capsys):
    if os.stat("keys").st_size == 0:
        assert status_json['text'] == "The public health director of Santa Clara County, California, confirmed that the county's new coronavirus case does"
    else:
        data = ft.getFeed("BleacherReport", 1)
        assert len(data[0]['text']) > 0


def test_annotateImage(capsys):
    if os.stat("keys").st_size == 0:
        assert testImage.description == "Blue, Cool, T-shirt, Outerwear, Facial hair, Beard, Rapper, Sleeve, Top"
    else:
        description = ft.annotateImage(testImage.url)
        assert description == "Blue, Cool, T-shirt, Outerwear, Facial hair, Beard, Rapper, Sleeve, Top"
