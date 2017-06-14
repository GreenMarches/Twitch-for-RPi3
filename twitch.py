from subprocess import call

# Example to put into command line after getting authentication token
# $ livestreamer -np omxplayer --twitch-oauth-token xxxxxxxxxxxxx twitch.tv/channel best

'''
auth_token can be found by:
    1. Enter on the command line:    livestreamer --twitch-oauth-authenticate    
    2. Login to Twitch
    3. Page does not exist error will appear
    4. In the URL, look for:    access_token=xxxxxxxxxxxxxx
        ex) livestreamer.tanuki.se/en/develop/twitch_oauth.html#access_token=xxxxxxxxxxxxxx&scope=user_read+user_subscriptions
    5. Replace the string auth_token above with whatever your xxxxxxxxxxxxxx is

quality can be set to one of the following: 
      best, worst, 1080p60, 160p, 360p, 480p, 720p, 720p60, audio_only

mode can either be analogue or hdmi, by uncommenting one of the above

'''

auth_token = "xxxxxxxxxx"    # Replace xxxxxxxxxx with your auth_token with the steps below
quality = "best"
mode = "omxplayer -o hdmi"    # HDMI
# mode = "omxplayer -o local"    # ANALOGUE
channel = "twitch.tv/" + input("Enter channel name: ")




call(["livestreamer", "-np", mode, "--twitch-oauth-token", auth_token, channel, quality])
