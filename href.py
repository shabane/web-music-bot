#!/usr/bin/python3

# Libraries
import re
import sys
import json
import requests
from bs4 import BeautifulSoup as bs

# Functions
## Finding the all tag a and link's
def GetAllTags(url: str, pattern: str):
    global headers

    musics = set()
    site = requests.get(url, headers=headers)

    if site.status_code != 200:
        return str("err:", site.status_code, file=sys.stderr)
    else:
        site = bs(site.content, "html.parser")
        site = site.find_all("a")
        for i in site:
            try:
                if re.search(f"{pattern}", i["href"], re.IGNORECASE):
                    musics.add(re.search(f"{pattern}", i["href"], re.IGNORECASE).string)
            except:
                pass
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
