import requests
from bs4 import BeautifulSoup
import re

import json

recent_requests = {}


class Translation(dict):
    def __init__(self, translation, context, example, gender, partOfSpeech, audioUrl, region):
        dict.__setitem__(self, translation, {
                         'context': context,
                         'example': example,
                         'gender': gender,
                         'partOfSpeech': partOfSpeech,
                         'audioUrl': audioUrl,
                         'region': region
                         })

    def translation(self):
        return self['translation']

    def context(self):
        return self['context']

    def example(self):
        return self['example']

    def __str__(self) -> str:
        return self.translation()


class TranslationPage(dict):
    def __init__(self, word, translations, contexts, examples):
        dict.__init__(self, word=word, pageData=[Translation(translation, context, example) for (
            translation, context, example) in zip(translations, contexts, examples)])

    def __str__(self) -> str:
        return str(self['pageData'][0])

    def __iter__(self):
        for item in self['pageData']:
            yield item


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
    lang_top = examples_top[0].get('lang')
    examples_top = [example.text for example in examples_top]

    examples_bottom = soup.find_all('span', class_='LneYEI1C')
    lang_bottom = examples_bottom[0].get('lang')
    examples_bottom = [example.text for example in examples_bottom]

    examples = [{lang_top: top, lang_bottom: bottom} for (top, bottom)
                in zip(examples_top, examples_bottom)]

    return TranslationPage(word, translations, contexts, examples)


def get_translation_data(word):
    if word in recent_requests:
        return _parse_translation_page(recent_requests[word], word)

    response = _request_translation_page(word)
    return _parse_translation_page(response, word)
