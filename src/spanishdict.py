import scrapper


def get_word(word):
    return scrapper.get_translations(word)


def get_page(word):
    return scrapper.get_translation_data(word)
