#!/bin/python3
import sys, requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print('Bad input')
    sys.exit()

URL = sys.argv[1]

# get html file
content = requests.get(URL)

# initial soup parser with hmtl file
soup = BeautifulSoup(content.text, 'lxml')

# get words from html file
words = [word.next_sibling for word in soup.find_all('br')]

# remove '\n\t' from the beginning of the words
words = [word.rsplit('\n\t')[-1] for word in words]

print(words)
