import requests
import time
from tqdm import tqdm
import codecs
import os
os.makedirs('images', exist_ok=True)
base_url = 'https://unsplash.com/napi/photos?page={}'
session = requests.session()
index = 1
with tqdm(range(10), total=10) as t:
    for i in t:
    	try:
			page = i + 1
			t.set_description_str('crawling page {}'.format(page))
			url = base_url.format(page)
			req = session.get(url)
			json = req.json()
			for image in json:
				alt = image.get('alt_description', ' ')
				raw_url = image['urls']['raw']
				name = '{}_{}.jpg'.format(index, alt)
				t.set_postfix_str('current image {}'.format(name))
				index = index + 1
				content = session.get(raw_url)
				f = codecs.open(os.path.join('images', name), 'wb')
				f.write(content.content)
			time.sleep(1)
		except Exception as e:
			pass
		t.close()
