# TuberMash
Like FaceMash, but with YouTubers!

I LOVE (The Social Network)[https://www.imdb.com/title/tt1285016/], so I decided to create FaceMash, but with YouTubers. TuberMash does not require any connection to YouTube API, since you run the Python script to get the channels and their PFPs.


## How to use it

I have not supplied `channels.json`, so you will have to create that file yourself, then run either `channels-getter-trending.py` or `channels-getter-shorts.py`. (I HIGHLY reccomend the Shorts version, since you can get as MANY channels as you want, since the Shorts feed is basically indefinite.)

All you have to do is run `python3 channels-getter-shorts.py`, and it will output all the channels into `channels.json`, and you're all ready to start mashing YouTubers!

(This DOES have to be run on a webserver, as the cross-origin content policy will block the Google images when running the HTML file locally.)


I would LOVE to see if anybody alters or makes the project better! All I ask if you do is that you credit me (YourFurryDeveloper on GitHub) for the original code. :3
