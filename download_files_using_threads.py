# Downloads the given urls and writes content to files in local filesystem 

import requests
from threading import Thread

class DownloadThread(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url
        print("Downloading : ", self.url)

    def run(self):
        resp = requests.get(self.url)
        if resp.status_code == 200:
            # write to file
            pos = self.url.rfind("/")
            filename = self.url[pos + 1:]
            file = open(filename, "wb")
            file.write(resp.content)
            file.close()
            print(f"Downloaded {self.url} to {filename}")
         else:
            print(f"Sorry! Could not download {self.ulr}")


urls = [
    "https://freemusicdownloads.world/wp-content/uploads/2017/05/Justin-Bieber-Love-Yourself-PURPOSE-The-Movement.mp3",
    "http://freemusicdownloads.world/wp-content/uploads/2017/05/Beyonc%C3%A9-Hold-Up.mp3",
    "http://freemusicdownloads.world/wp-content/uploads/2017/05/Coldplay-Paradise-Official-Video.mp3"]

for url in urls:
    t = DownloadThread(url)
    t.start()
