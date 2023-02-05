import requests
import string
import random
import argparse
import sys
import threading
import make_box
from pyshade import *


def getRandomString(length):
    return "".join(random.choice(string.ascii_lowercase+string.digits) for i in range(length))

def getRandomText(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

def generate():
    nickname = getRandomText(8)
    passw = getRandomString(12)
    email = nickname+"@"+getRandomText(5)+".com"

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": getRandomString(32)}
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nickname,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6",
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)

    if r.status_code==200:
        if r.json()['status']==1:
            return (True, nickname, r.json()["username"], email, passw)

if __name__ == "__main__":
    choice = int(Mode.Vertical(colors.purple_to_blue , make_box.Banner("""
███████ ██████   ██████  ████████ ██ ███████ ██    ██ 
██      ██   ██ ██    ██    ██    ██ ██       ██  ██  
███████ ██████  ██    ██    ██    ██ █████     ████   
     ██ ██      ██    ██    ██    ██ ██         ██    
███████ ██       ██████     ██    ██ ██         ██ 

            Spotify Account Gen""")+"""
[1] Email:Pass
[2] Nick:Username:Email:Pass
> """, 2, False))

    if choice == 1:
        account_num = int(Mode.Horizontal(colors.purple_to_blue, "\nNumber of Account > ", 4))
        print("\n")
        for _ in range(account_num):
            res = generate()

            if res[0]:
                result = f"{res[3]}:{res[4]}"
                with open("Accounts.txt", "a+") as f:
                    f.write(f"{result}\n")
                Mode.Horizontal(colors.purple_to_blue, f"{result}  [{_+1}]", 5)

    elif choice == 2:
        account_num = int(input("Number of Account > "))

        for _ in range(account_num):
            res = generate()

            if res[0]:
                result = f"{res[1]}:{res[2]}:{res[3]}:{res[4]}"
                with open("Accounts_Details.txt", "a+") as f:
                    f.write(f"{result}\n")
                print(f"{result}  [{_+1}]")