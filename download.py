import requests
import time
from tqdm import tqdm
base_url = 'https://unsplash.com/napi/photos?page={}'
session = requests.session()
index = 1
for i in range(10):
    page = i + 1
    url = base_url.format(page)
    req = session.get(url)
    json = req.json()
    for image in json:
        alt = image.get('alt_description', ' ')
        raw_url = image['urls']['raw']
        
    time.sleep(1)
    print(url)
