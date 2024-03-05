import requests
from bs4 import BeautifulSoup
import re

import json

recent_requests = {}


class Translation(dict):
    def __init__(self, translation, context, example, gender, partOfSpeech, region):
        dict.__setitem__(self, translation, {
                         'context': context,
                         'example': example,
                         'gender': gender,
                         'partOfSpeech': partOfSpeech,
                         'region': region
                         })

    def translation(self):
        return list(self.keys())[0]

    def context(self):
        return self['context']

    def example(self):
        return self['example']

    def __str__(self) -> str:
        return self.translation()


class TranslationPage(dict):
    def __init__(self, word, data):
        dict.__init__(self, word=word, data=data)

    def __str__(self) -> str:
        return str(self['data'][0])

    def __iter__(self):
        for item in self['data']:
            yield item


def _request_translation_page(word):
    url = f'https://www.spanishdict.com/translate/{word}'
    response = requests.get(url)

    recent_requests[word] = response.text

    return response.text


def _parse_translation_page(response, word):
    all_translations = []

    soup = BeautifulSoup(response, 'html.parser')

    words = soup.find_all(string=True)

    for w in words:
        if w.parent.name == 'script' and 'SD_COMPONENT_DATA' in w:
            obj = json.loads(w.split(
                'SD_COMPONENT_DATA = ')[1].split(';')[0]).get('sdDictionaryResultsProps').get('entry').get('neodict')[0].get('posGroups')

    for sense in obj:
        for item in sense.get('senses'):
            all_translations.append(
                Translation(translation=item.get('translations')[0].get('translation'),
                            context=item.get('contextEn'),
                            example=item.get('translations')[
                    0].get('examples'),
                    gender=item.get('translations')[0].get('gender'),
                    partOfSpeech=item.get(
                                'partOfSpeech').get('nameEn'),
                    region=item.get('region')))

    return TranslationPage(word, all_translations)


def get_translation_data(word):
    if word in recent_requests:
        return _parse_translation_page(recent_requests[word], word)

    response = _request_translation_page(word)
    return _parse_translation_page(response, word)
