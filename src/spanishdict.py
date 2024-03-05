import scrapper


def translate(word):
    return scrapper.get_translation_data(word)


def conjugate(word):
    return scrapper.get_conjugation_data(word)
