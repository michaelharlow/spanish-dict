import requests
from bs4 import BeautifulSoup

from dictionary import Translation, TranslationPage
from conjugation import Conjugation, ConjugationPage

import json

recent_requests = {}


def _request_translation_page(word):
    url = f"https://www.spanishdict.com/translate/{word}"
    response = requests.get(url)

    recent_requests[word] = response.text

    return response.text


def _request_conjugation_page(word):
    url = f"https://www.spanishdict.com/conjugate/{word}"
    response = requests.get(url)

    recent_requests[word] = response.text

    return response.text


def _parse_translation_page(response, word):
    all_translations = []

    soup = BeautifulSoup(response, "html.parser")

    words = soup.find_all(string=True)

    for w in words:
        if w.parent.name == "script" and "SD_COMPONENT_DATA" in w:
            obj = (
                json.loads(w.split("SD_COMPONENT_DATA = ")[1].split(";")[0])
                .get("sdDictionaryResultsProps")
                .get("entry")
                .get("neodict")[0]
                .get("posGroups")
            )

    for sense in obj:
        for item in sense.get("senses"):
            all_translations.append(
                Translation(
                    translation=item.get("translations")[0].get("translation"),
                    context=item.get("contextEn"),
                    example=item.get("translations")[0].get("examples"),
                    gender=item.get("translations")[0].get("gender"),
                    partOfSpeech=item.get("partOfSpeech").get("nameEn"),
                    region=item.get("region"),
                )
            )

    return TranslationPage(word, all_translations)


def _parse_conjugation_page(response, word):
    soup = BeautifulSoup(response, "html.parser")

    words = soup.find_all(string=True)

    for w in words:
        if w.parent.name == "script" and "SD_COMPONENT_DATA" in w:
            obj = (
                json.loads(w.split("SD_COMPONENT_DATA = ")[1].split(";")[0]).get("verb").get("paradigms")
            )

    result = []

    # for item in obj:
    #     result.append({item: {pronoun: conjugation for (pronoun, conjugation) in obj[item]}})

    for i, item in enumerate(obj):
        result.append({item: {}})
        for data in obj[item]:
            result[i][item] = {**result[i][item], data['pronoun']: data['word']}


    return ConjugationPage(word, result)


def get_translation_data(word):
    if word in recent_requests:
        return _parse_translation_page(recent_requests[word], word)

    response = _request_translation_page(word)
    return _parse_translation_page(response, word)

def get_conjugation_data(word):
    return _parse_conjugation_page(_request_conjugation_page(word), word)
