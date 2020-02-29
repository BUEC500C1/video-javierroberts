from PIL import Image
import os
import imaging


def test_createImage():
    imaging.createImage("The public health director of Santa Clara County, California, confirmed that the county's new coronavirus case does",
                        None, "https://pbs.twimg.com/media/ERoUIJYWsAA66Eh?format=jpg&name=medium", "nytimes", "28/02/20", 1, "test_images2")

    im1 = Image.open('test_images2/image_0.png')
    im2 = Image.open('test_images2/image_1.png')

    assert list(im1.getdata()) == list(im2.getdata())


def test_makeImages():
    if os.stat("keys").st_size > 0:
        imaging.makeImages("espn", "test_images", 3)
        assert len(os.listdir('test_images')) == 3
    else:
        assert True
