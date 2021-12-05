import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
data_dict = []

for i in root[0].findall('item'):
    a = {}
    for j in i:
        a[j.tag] = j.text
    data_dict.append(a)

with open('news.json', 'wb') as json_file:
    file = json.dumps(data_dict, indent=3, ensure_ascii=False).encode('utf8')
    json_file.write(file)