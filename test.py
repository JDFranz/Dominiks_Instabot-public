import instabot
import sys
import os

instabot.return_login()
if __name__== "__main__":
    while(True):
        print("quit")
        os.system("test.py")


    hashtags = []

    hashtags.append(instabot.generate_hashtags('local hashtags', 5))
    hashtags.append(instabot.generate_hashtags('music hashtags', 5))
    hashtags.append(instabot.generate_hashtags('rap&Hiphop hashtags', 5))
    hashtags.append(instabot.generate_hashtags('EDM hashtags', 5))
    hashtags.append(instabot.generate_hashtags('Rockmusic hashtags', 5))

    bot = instabot.Instabot(instabot.return_login()[0], instabot.return_login()[1])
    for hashtaglist in hashtags:
        bot.follow_hashtag(hashtaglist[1], 7)
        bot.lpnc_hastags_feed(hashtaglist, 5)


