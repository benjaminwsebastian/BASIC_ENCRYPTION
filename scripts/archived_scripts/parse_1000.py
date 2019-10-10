#!/bin/python3
'''
No longer using because the 1000 most popular words are not comprehensive enough
This was the URL used: https://1000mostcommonwords.com/1000-most-common-english-words/
'''
import sys, requests
from bs4 import BeautifulSoup

if len(sys.argv) != 2:
    print('Bad input')
    sys.exit()

URL = sys.argv[1]

# get html file
content = requests.get(URL)

# initial soup parser with hmtl file
soup = BeautifulSoup(content.text, 'html.parser')

# get words from html file
words = [word.text for word in soup.find_all('td')]

# remove blank entries
words = list(filter(None, words))

# remove preamble
to_delete = len(words)-2000
del words[:to_delete]

# remove numbers
for i, word in enumerate(words):
    try:
        int(word)
        del words[i]
    except:
        pass

print(words)
