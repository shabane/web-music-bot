#!/usr/bin/python3

# Libraries
import re
import sys
import json
import requests
from bs4 import BeautifulSoup as bs

# Functions
## Finding the all tag a and link's
def GetAllTags(url: str):
    global headers

    musics = set()
    site = requests.get(url, headers=headers)

    if site.status_code != 200:
        return str("err:", site.status_code, file=sys.stderr)
    else:
        site = bs(site.content, "html.parser")
        for i in ('a', 'audio'):
            for j in site.find_all(i):
                if(src := j.get('href')):
                    if('mp3' in src):
                        musics.add(src)
                        print(src)
                else:
                    if(src := j.get('src')):
                        if('mp3' in src):
                            musics.add(src)
                            print(src)
                            
        if(musics):
            return musics
        else:
            return False
                        

# Start point
with open("headers.json", "r") as fli:
    fli = json.load(fli)
    if type(fli) != dict:
        print("Error: the header.json file not follow JSON format!", file=sys.stderr)
    elif type(fli) == dict:
        headers = fli
    else:
        headers = {}
