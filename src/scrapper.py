import requests
from bs4 import BeautifulSoup
import re


def get_translations(word):
    url = f'https://www.spanishdict.com/translate/{word}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    words = soup.find_all('div', id=re.compile('quickdef'))

    return [w.contents[0].text for w in words]
