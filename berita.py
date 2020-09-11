#!/usr/bin/env python3
#
#
# You're coding and you're too lazy to leave the terminal
# to know latest news
#
# renisawidya@protonmail.com
# 2020

import urllib.request
import xml.etree.ElementTree as ET
from Myparser import *
from sys import argv, exit

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

news_sites = {
        'ANTARA' : {
            'url': 'https://www.antaranews.com/rss/top-news',
            'parser' : Antara,
            },
        'TEMPO' : {
            'url' : 'https://rss.tempo.co/nasional',
            'parser' : Tempo,
            },
        'CNN' : {
            'url' : 'https://www.cnnindonesia.com/nasional/rss',
            'parser' : Cnn,
            },
        }

colors = {
        'BLACK' : '\033[0;30m',
        'LIGHT_WHITE' : '\033[1;37m',
        'GREEN' : '\033[0;32m',
        'BLUE' : '\033[0;34m',
        'YELLOW' : '\033[1;33m',
        'BOLD' : '\033[1m',
        'UNDERLINE' : '\033[4m',
        }

saved_index = dict()

def get_raw_page(url):
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    response_data = response.read()
    return response_data.decode('utf8')

def read_index(url):
    index_data = get_raw_page(url)
    root = ET.fromstring(index_data)
    news_header = root.find('./channel/title')
    news_desc = root.find('./channel/description')
    print(f'{colors["GREEN"]}{colors["BOLD"]}{news_header.text}')
    print(f'{colors["LIGHT_WHITE"]}{colors["UNDERLINE"]}{news_desc.text}')
    for idx, item in enumerate(root.findall('./channel/item'), start=1):
        if idx > 10:
            break
        title = item.find('./title').text
        link = item.find('./link').text
        saved_index[idx] = {'title': title, 'link' : link}
        print(f'{colors["GREEN"]}[{idx}] {colors["YELLOW"]}{title}')

def read_more(news_site, idx):
    if not idx in saved_index:
        exit(1)
    chosen_news = saved_index[idx]
    print(f'\n\n{colors["YELLOW"]}{chosen_news["title"]}\n')
    print('=================================\n')
    page = get_raw_page(chosen_news['link'])
    page_parser = news_sites[news_site]['parser']()
    page_parser.feed(page)


def print_usage():
    print(f'Usage: {argv[0]} news_site')
    print(f'Available news sites: {list(news_sites)}')
    exit(1)

def main():
    if len(argv) != 2:
        print_usage()
    news_site = argv[1].upper()
    if news_site in news_sites:
        read_index(news_sites[news_site]['url'])
        index = input(f'{colors["BLUE"]}Read More [insert index number or q to quit]? ')
        try:
            index = int(index)
            read_more(news_site, index)
        except:
            exit(0)
    else:
        print_usage()

if __name__ == '__main__':
    main()
