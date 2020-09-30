import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
nytimes = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def show_cache_pages(direct, act):
    with open(os.path.join(direct, act + '.txt'), 'r',
              encoding='utf-8') as _f:
        for _l in _f.readlines():
            print(_l)
        # html_doc = _f.read()
        # bs = BeautifulSoup(html_doc, 'lxml')
        # for child in bs.recursiveChildGenerator():
        #     if child.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a',
        #                       'ul', 'ol', 'li']:
        #         if child.name == 'a':
        #             print(Fore.BLUE + child.text)
        #             print(Style.RESET_ALL)
        #         else:
        #             print(child.text)



args = sys.argv
directory = args[1]

if not os.path.exists(directory):
    directory = directory
    os.mkdir(directory)

init()
cached_pages = []
back_pages = deque()
loaded_page = None
while True:
    action = input()
    if action == 'exit':
        break
    elif action == 'back':
        if len(back_pages) > 0:
            loaded_page = None
            page = back_pages.pop()
            show_cache_pages(directory, page)
    elif action in cached_pages:
        show_cache_pages(directory, action)
        if loaded_page:
            back_pages.append(loaded_page)
        loaded_page = action
    elif '.' not in action:
        print('Error: Incorrect url')
        if loaded_page:
            back_pages.append(loaded_page)
        loaded_page = None
    else:
        if not action.startswith('https://'):
            action = 'https://' + action

        page_cache = action.replace('https://', '')
        page_cache = page_cache[:page_cache.rfind('.')]
        res = requests.get(action)
        if res:
            if loaded_page:
                back_pages.append(loaded_page)
            loaded_page = page_cache
            bs = BeautifulSoup(res.text, 'html')
            text_cache = ''
            for child in bs.recursiveChildGenerator():
                if child.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a',
                                  'ul', 'ol', 'li']:
                    if child.name == 'a':
                        print(Fore.BLUE + child.text)
                        print(Style.RESET_ALL)
                    else:
                        print(child.text)
                    text_cache = text_cache + child.text + '\n'

            with open(os.path.join(directory, page_cache + '.txt'), 'w',
                      encoding=res.encoding) as f:
                f.writelines(text_cache)
            cached_pages.append(page_cache)
        else:
            print('Error: Incorrect url')
            if loaded_page:
                back_pages.append(loaded_page)
            loaded_page = None
