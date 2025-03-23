from transformers import pipeline

class TextAnalyzer:
    def word_count(self, text):
        return len(text.split())

    def char_count(self, text):
        return len(text)

    def unique_words(self, text):
        return len(set(text.split()))

class AdvancedTextAnalyzer(TextAnalyzer):
    def sentiment_analysis(self, text):
        sentiment_pipeline = pipeline("sentiment-analysis")
        res = sentiment_pipeline([text])
        print(res)
        print(len(res))
        return res[0]['label']

        # positive_words = ["wspaniały","dobry","świetny"]
        # negative_words = ["okropny","zły","brzydki"]
        # if text in positive_words:
        #     return "Pozytywny"
        # if text in negative_words:
        #     return "Negatywny"
        # return "Neutralny"


str_1 = "It was a really beautiful day!"
str_2 = "It was a really bad day!"

analyzer = AdvancedTextAnalyzer()

print(f"ilość słów {analyzer.word_count(str_1)}")
print(f"ilość znaków {analyzer.char_count(str_1)}")
print(f"unikane słowa {analyzer.unique_words(str_1)}")
print(f"analiza sentymentu {analyzer.sentiment_analysis(str_1)}")

print("------------------------------------------------")

print(f"ilość słów {analyzer.word_count(str_2)}")
print(f"ilość znaków {analyzer.char_count(str_2)}")
print(f"unikane słowa {analyzer.unique_words(str_2)}")
print(f"analiza sentymentu {analyzer.sentiment_analysis(str_2)}")








