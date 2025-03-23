from typing import List


class SimpleChatbot:
    def __init__(self, questions: List[str]) -> None:
        self.questions = questions
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self) -> None:
        if self.counter < len(self.questions) - 1:
            self.counter += 1
        else:
            raise StopIteration


bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor"])

for question in bot.questions:
    print(question)
    input()
    try:
        next(bot)
    except StopIteration:
        print("Stop iteration")
