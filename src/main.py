import requests
from bs4 import BeautifulSoup
import re

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


def fun():
    api_end_point = input('Enter the word: ')
    while (api_end_point != ''):
        url = f'https://www.spanishdict.com/translate/{api_end_point}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        words = soup.find_all('div', id=re.compile('quickdef'))
        # words = soup.find_all('div', class_='P3wxfRe7 jXjO2bU0')

        for w in words:
            print(w.contents[0].text)

        api_end_point = input('Enter the word: ')


if __name__ == '__main__':
    # fun()
    word = 'hello'
    spanish = spanishdict.SpanishDict(word)
    print(spanish.get_translation())
