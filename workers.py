import queue
import threading
import video as vd
import imaging as im
import time
import subprocess
import os

NUMBER_THREADS = 4


q_images = queue.Queue(maxsize=NUMBER_THREADS)
q_video = queue.Queue()
done_list = [0, 0, 0, 0]


def thread_init():

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my-google-api-credentials.json"

    for i in range(NUMBER_THREADS):
        # Remove any existing images
        path = "media/thread%s" % str(i)
        subprocess.call("find . -type f -iname \*.png -delete",
                        cwd=path, stdout=subprocess.DEVNULL, shell=True)

    for i in range(NUMBER_THREADS):
        thread = threading.Thread(name="Thread_%s" % str(
            i), target=imageProcessor)
        thread.start()

    for i in range(NUMBER_THREADS):
        thread = threading.Thread(name="Thread_%s" % str(
            i), target=videoProcessor)
        thread.start()


def imageProcessor():
    while True:
        task = q_images.get()
        t_id = task[1]
        if task[0] != None:
            im.makeImages(task[0], "media/thread%s" % str(t_id), 500)
            break
    q_images.task_done()
    q_video.put(t_id)
    time.sleep(0.001)
    thread = threading.Thread(name="Thread_%s" % str(
        t_id), target=imageProcessor)
    thread.start()


def videoProcessor():
    while True:
        t_id = q_video.get()
        if t_id != None:
            vd.makeVideo("media/thread%s" % str(t_id))
            break
    q_video.task_done()
    done_list[t_id] = 1
    time.sleep(0.001)
    thread = threading.Thread(name="Thread_%s" % str(
        t_id), target=videoProcessor)
    thread.start()


def producer(handle, t_id):
    q_images.put((handle, t_id))
