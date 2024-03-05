class Conjugation():
    def __init__(self, conjugation, pronoun, tense_mood):
        self.conjugation = conjugation
        self.pronoun = pronoun
        self.tense_mood = tense_mood
        
    def __str__(self):
        return f"{self.pronoun} {self.conjugation}"


class ConjugationPage(dict):
    def __init__(self, word, data):
        dict.__init__(self, word=word, data=data)
        
    def __str__(self):
        return str(self["data"][0])
    
    def __iter__(self):
        for item in self["data"]:
            yield item
