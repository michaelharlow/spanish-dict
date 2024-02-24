import requests
from bs4 import BeautifulSoup
import re

recent_requests = {}


class TranslationPage(dict):
    def __init__(self, word, translations, contexts, examples):
        dict.__init__(self, word=word, translations=translations,
                      contexts=contexts, examples=examples)

    def get_translations(self):
        return self['translations']


def _request_translation_page(word):
    url = f'https://www.spanishdict.com/translate/{word}'
    response = requests.get(url)

    recent_requests[word] = response.text

    return response.text


def _parse_translation_page(response, word):
    soup = BeautifulSoup(response, 'html.parser')

    translations = soup.find_all('a', class_='HOypmmqy')
    translations = [word.text for word in translations]

    contexts = soup.find_all('span', class_='a9peX5qq')
    contexts = [context.text for context in contexts]

    examples_top = soup.find_all('span', class_='bXF90XJM')
    examples_top = [example.text for example in examples_top]
    examples_bottom = soup.find_all('span', class_='LneYEI1C')
    examples_bottom = [example.text for example in examples_bottom]
    examples = {top: bottom for (top, bottom) in zip(
        examples_top, examples_bottom)}

    return TranslationPage(word, translations, contexts, examples)


def get_translation_data(word):
    if word in recent_requests:
        return _parse_translation_page(recent_requests[word], word)

    response = _request_translation_page(word)
    return _parse_translation_page(response, word)
