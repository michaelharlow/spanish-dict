import requests
from bs4 import BeautifulSoup

import json

import spanishdict

# url = 'https://quotes.toscrape.com/'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# quotes = soup.find_all('span', class_='text')
# authors = soup.find_all('small', class_='author')
# tags = soup.find_all('div', class_='tags')

# for i in range(len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text)
#     quote_tags = tags[i].find_all('a', class_='tag')
#     for tag in quote_tags:
#         print(tag.text)
#     print()


def fun(word):
    url = f'https://www.spanishdict.com/translate/{word}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    words = soup.find_all(string=True)

    for w in words:
        if w.parent.name not in ['a', 'span'] or w.parent.get('lang') is None:
            continue
        print(w)


if __name__ == '__main__':
    print(spanishdict.translate('hola'))
    for item in spanishdict.translate('adios'):
        print(item)
