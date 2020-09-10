#!/usr/bin/env python3


# You're coding and you're too lazy to leave the terminal
# to know latest news
#
# renisawidya@protonmail.com
# 2020

import urllib.request
import xml.etree.ElementTree as ET
from sys import argv, exit

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

news_sites = {
        'ANTARA' : 'https://www.antaranews.com/rss/top-news', 
        'DETIK' : 'https://rss.detik.com/index.php/detikcom_nasional',
        'TEMPO' : 'https://rss.tempo.co/nasional',
        'CNN' : 'https://www.cnnindonesia.com/nasional/rss',
        }

colors = {
        'BLACK' : '\033[0;30m',
        'RED' : '\033[0;31m',
        'GREEN' : '\033[0;32m',
        'BLUE' : '\033[0;34m',
        'YELLOW' : '\033[1;33m',
        }

def get_raw_page(url):
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    return response_data.decode('utf8')

def read_index(url):
    response_data = get_raw_page(url)
    root = ET.fromstring(response_data)
    for idx, title in enumerate(root.findall('./channel/item/title'), start=1):
        if idx > 10:
            break
        print(f'{colors["GREEN"]}[{idx}] {colors["YELLOW"]}{title.text}')

def print_usage():
    print(f'Usage: {argv[0]} news_site')
    print(f'Available news sites: {list(news_sites)}')

def main():
    if len(argv) != 2:
        print_usage()
        exit(1)
    news_site = argv[1].upper()
    read_index(news_sites[news_site])

if __name__ == '__main__':
    main()
