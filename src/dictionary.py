class Translation(dict):
    def __init__(self, translation, context, example, gender, partOfSpeech, region):
        dict.__setitem__(
            self,
            translation,
            {
                "context": context,
                "example": example,
                "gender": gender,
                "partOfSpeech": partOfSpeech,
                "region": region,
            },
        )

    def translation(self):
        return list(self.keys())[0]

    def context(self):
        return self["context"]

    def example(self):
        return self["example"]

    def __str__(self) -> str:
        return self.translation()


class TranslationPage(dict):
    def __init__(self, word, data):
        dict.__init__(self, word=word, data=data)

    def __str__(self) -> str:
        return str(self["data"][0])

    def __iter__(self):
        for item in self["data"]:
            yield item