# video-javierroberts

# API Desicription:

This API allows users to retrieve a .mp4 video that contains a slideshow where every frame is a tweet that was posted by a specific twitter user within the last day. The frame also contains an AI image description (if there was an image associated with the tweet) that is obtained using Google Vision. Other metadata, such as the users handle and profile picture, are also included in the frame.

# Setup:

- You need to install the requirements, so run pip3 install -r requirements.txt.
- You also need to populate the keys file with appropriate twitter keys in the following format:

        [auth]
        consumer_key =
        consumer_secret =
        access_token =
        access_secret =

- Additioanlly, you need to get gcloud api credentials and save them as my-google-api-credentials.json in the root folder.

# How to start server:

Simply execute python3 api.py to start server

Terminal output should look like this:

![server](sample_images/server-running.png)

# How to request a video for a certain twitter user:

Make a get request to "http://127.0.0.1:5000/getvideo/<HANDLE>" where HANDLE is the handle of the user you are looking for. Make sure handle exists, API is not currently equipped to handle incorrect usernames.

For example, this is what is returned from a get request to http://127.0.0.1:5000/getvideo/espn:

![loading](sample_images/loading_video.png)
![running1](sample_images/video-running.png)
![running2](sample_images/video-running2.png)
![running3](sample_images/video-running3.png)

# Testing:

I used pytest for testing. Tests should pass even without gcloud and tweepy credentials as there are hardcoded stub functions included.

# Answers to assigment questions:

1. Given that the Macbook I am using has an I7 quadcore processor, I believe it should be able to process 4 simultaneous API calls.
2. The API can run more than one API call at the same time.
3. The processing was split into 8 threads, 4 producing images and 4 producing videos.
