#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup as bs
import re
import json
import sys


with open("headers", "r") as fli:
    fli = json.load(fli)
    if type(fli) != dict:
        print("err: the header file should be a json file", file=sys.stderr)
    elif type(fli) == dict:
        headers = fli
    else:
        headers = {}



# finding the all tag a and link's
def GetAllTags(url: str, pattern: str):
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
                return False
        return musics



