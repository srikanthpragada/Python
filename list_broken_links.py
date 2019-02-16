# Displays links in the page that are not valid (broken)

import requests
from bs4 import BeautifulSoup

website = "http://www.srikanthtechnologies.com"   # Website we want to use 
resp = requests.get(website)
bs = BeautifulSoup(resp.text, "html.parser")

anchors = bs.find_all("a")
for a in anchors:
    if 'href' in a.attrs:
        url = a['href']
        if url == "#":  # ignore these URLs 
            continue

        # find out whether url starts with http
        if not url.startswith("http"):
            url = website + "/" + url

        # Check whether URL is valid
        resp = requests.get(url)
        if resp.status_code == 404:
            print(f"{url} is invalid!")
        else:
            print(f"{url} is valid!")
