# Twitch-for-RPi3

Watch Twitch on Raspberry Pi 3 using the command line on Raspbian

## Update Pi
Type anything in the code block on the command line
```
sudo apt-get update
sudo apt-get upgrade
```

## Install Livestreamer ( http://docs.livestreamer.io/ )
```
sudo pip install livestreamer
```

## Get authentication token
```
livestreamer --twitch-oauth-authenticate
```

1. A browser will open after typing in the above   
2. Login to Twitch   
3. Page does not exist error will appear  
4. In the URL, look for:    access_token=xxxxxxxxxxxxxx       
  
  
Replace xxxxxxxxxxx with the retrieved token and channel with the desired channel.

Source quality of the video feed will play on omxplayer after entering the below
``` 
livestreamer -np omxplayer --twitch-oauth-token xxxxxxxxxxxxx twitch.tv/channel best
```

## Python
To not type the long string everytime, download twitch.py

1. Move twitch.py to /home/pi

2. Change the string variable auth_token in twitch.py to the token retrieved

3. Optionally, change quality and sound mode

4. Run on the command line, and enter channel name when prompted

```
python3 twitch.py
```
