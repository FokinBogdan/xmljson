import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_first_element_tree():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_news_and_pub_date(first_element):
    news_and_pub_date = []
    for i in first_element.findall('item'):
        news_and_pub_date.append({'pubDate': i.find('pubDate').text, 'title': i.find('title').text})
    return news_and_pub_date


def save_json(first_element):
    with open("news.json", 'wb') as file:
        json_file = json.dumps(get_news_and_pub_date(first_element), ensure_ascii=False, indent=3).encode('utf8')
        file.write(json_file)

first_element_tree = get_first_element_tree()
save_json(first_element_tree)