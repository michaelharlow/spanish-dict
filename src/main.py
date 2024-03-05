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
        if w.parent.name == 'script' and 'SD_COMPONENT_DATA' in w:
            return w


if __name__ == '__main__':
    # print(json.dumps(spanishdict.translate('hola'), indent=2))
    # print(json.dumps(spanishdict.translate('hello'), indent=2))
    for item in spanishdict.translate('milk'):
        print(item)
    # obj = json.loads(fun('milk').split(
    #     'SD_COMPONENT_DATA = ')[1].split(';')[0]).get('sdDictionaryResultsProps').get('entry').get('neodict')[0].get('posGroups')[1].get('senses')

    # print(repr(spanishdict.translate('milk')))
    print(json.dumps(spanishdict.translate("milk"), indent=2))

    # loop through every key and subkey in the dictionary
