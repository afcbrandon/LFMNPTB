#!/usr/bin/env python3
import tweepy
import pylast

## replace with your twitter credientials
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")


## replace with your credientials
lastfm_network = pylast.LastFMNetwork(
    api_key = "XXX" ,
    api_secret = "XXX",
)

## lastfm username
username = "XXX"
## status for not playing music
notplaying = "curretly not bumping jams"
## your twitter bio
bio = " "
## the text you displayed before your currently playing song
pretext = "Now playing: "

##########################
api = tweepy.API(auth)
now_playing = lastfm_network.get_user(username).get_now_playing()
nowplaying =  pretext  + str(now_playing)
updateactive = bio + nowplaying
updateinactive = bio + notplaying

if now_playing is None:
    print(now_playing)
    api.update_profile(description = updateinactive)
else:
    print(notplaying)
    api.update_profile(description = updateactive)
