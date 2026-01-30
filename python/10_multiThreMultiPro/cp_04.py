import threading
import requests
import time

def download_img(url):
    print(f"starting the downloading from {url}")
    resp = requests.get(url)
    print(f"Finshed downloading from the {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
thread = []

for url in urls:
    t = threading.Thread(target=download_img, args=(url, ))
    t.start()
    thread.append(t)

for t in thread:
    t.join()
end = time.time()

print(f"all downloads done in {end-start:.2f} seconds")