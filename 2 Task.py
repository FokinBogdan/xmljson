import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_first_element_tree():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_items(first_element):
    items = []
    for i in first_element.findall('item'):
        items.append({'author': i.find('author').text, 'category': i.find('category').text,
                      'description': i.find('description').text, 'enclosure': i.find('enclosure').text,
                      'guid': i.find('guid').text, 'link': i.find('link').text,
                      'pubDate': i.find('pubDate').text, 'title': i.find('title').text})
    return items


def save_json(first_element):
    with open("Content of item tags.txt", 'wb') as file:
        json_file = json.dumps(get_items(first_element), ensure_ascii=False, indent=3).encode('utf8')
        file.write(json_file)

first_element_tree = get_first_element_tree()
save_json(first_element_tree)