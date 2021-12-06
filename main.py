import threading
import requests
import random
import string

def run():
    while True:
        try:
            s = requests.Session()
            code = ''.join(random.choices(string.ascii_uppercase, k = 4))
            url = f"https://ecast.jackboxgames.com/api/v2/rooms/{code}"
            r = s.get(url)
            if r.json()['ok'] == True:
                print(f"Found new code | {code} | Game: {r.json()['body']['appTag']}")
                break
        except:
            pass

for i in range(150):
    t = threading.Thread(target=run)
    t.start()