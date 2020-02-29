from PIL import Image
import os
import imaging


def test_createImage(capsys):
    imaging.createImage("The public health director of Santa Clara County, California, confirmed that the county's new coronavirus case does",
                        None, "https://pbs.twimg.com/media/ERoUIJYWsAA66Eh?format=jpg&name=medium", "nytimes", "28/02/20", 1, "")

    im1 = Image.open('image_0.png')
    im2 = Image.open('image_1.png')

    assert list(im1.getdata()) == list(im2.getdata())


def test_makeImages(capsys):
    if os.stat("keys").st_size > 0:
        imaging.makeImages("espn", "test_images", 3)
        assert len(os.listdir('test_images')) == 3
    else:
        assert True
