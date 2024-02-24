import scrapper


class SpanishDict:

    def __init__(self, word):
        self.word = word
        self.translations = self.get_word()

    def get_word(self):
        return scrapper.get_translations(self.word)

    def get_translation(self):
        return f"{self.word} in English is {self.translations} in Spanish"
