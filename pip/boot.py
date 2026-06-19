import wiitools as w
import json

data = None
get = []
urls = ["https://raw.github.com/lberwa/wii-pip"]

def update():
    for url in urls:
        get.append(w.curl_get(url + "/data.json"))
    
    