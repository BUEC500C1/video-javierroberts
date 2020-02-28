import imaging
import tweepy
import feedTools as ft
import subprocess


def makeVideo(path):

    # Remove any existing video
    subprocess.call("find . -type f -iname \*.mp4 -delete",
                    cwd=path, stdout=subprocess.DEVNULL, shell=True)

    # Converting frames to video
    subprocess.call("ffmpeg -framerate 0.33 -pattern_type glob -i '*.png' -c:v libx264 -r 30 -pix_fmt yuv420p video.mp4",
                    cwd=path, stdout=subprocess.DEVNULL, shell=True)

    # Deleting frames
    subprocess.call("find . -type f -iname \*.png -delete",
                    cwd=path, stdout=subprocess.DEVNULL, shell=True)
