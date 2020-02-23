from PIL import Image, ImageDraw, ImageFont
import feedTools as ft
import datetime
import textwrap
import urllib.request as urllib
import io


def makeImages(handle, path, max_count):
    tweets = ft.getFeed(handle, max_count)
    failed = 0
    today = datetime.datetime.now()
    today = today.strftime('%d/%m/%d')
    for i, tweet in enumerate(tweets):
        created = tweet['dateCreated']
        created = created.strftime('%d/%m/%d')
        if (created == today):
            try:
                if "image description" in tweet:
                    createImage(tweet['text'],
                                tweet["image description"], tweet['pic'], handle, created, i-failed, path)
                else:
                    createImage(tweet['text'], None,
                                tweet['pic'], handle, created, i-failed, path)
            except:
                failed += 1
                continue


def createImage(tweet, image, img_url, handle, date, counter, path):

    # Adding tweet

    img = Image.new('RGB', (800, 800), color=(73, 109, 137))
    d = ImageDraw.Draw(img)

    font = ImageFont.truetype("Arial.ttf", 30)

    if image:
        text = tweet + "\n" + "Attached image description: " + image
        textWrapped = textwrap.wrap(text, width=30)
        displayText = ""
    else:
        textWrapped = textwrap.wrap(tweet, width=30)
        displayText = ""

    for line in textWrapped:
        displayText = displayText + '\n' + line

    d.text((200, 70), displayText, fill='white', font=font)

    # Adding handle

    font = ImageFont.truetype("Arial.ttf", 35)
    handle = "@" + handle

    handleWrapped = textwrap.wrap(handle, 20)
    handle = ""

    for line in handleWrapped:
        handle = handle + '\n' + line

    d.text((400, 500), handle, fill='white', font=font)

    # Adding date

    d.text((400, 600), date, fill='white', font=font)

    # Adding profile image

    fd = urllib.urlopen(img_url)
    image_file = io.BytesIO(fd.read())
    profile_pic = Image.open(image_file)

    profile_pic = profile_pic.resize((250, 250))

    img.paste(profile_pic, (100, 450))

    img.save(path + '/image_%d.png' % counter)
    counter += 1


if __name__ == "__main__":
    makeImages("realDonaldTrump", 'media', 50)
