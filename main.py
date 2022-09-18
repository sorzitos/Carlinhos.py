import requests
#import time


channelID = channelid
headers = {"authorization": "token"}
i = 1

file = open("textos.txt", "r")
lines = file.readlines()

while True:
    #time.sleep(1.3)
    for line in lines:
        requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers = headers, json = {"content": line})
