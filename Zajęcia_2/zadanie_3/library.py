from typing import Dict


class Library:
    def __init__(self, books: Dict[str, str]) -> None:
        self.books = books

    def find_book(self, isbn: str) -> str | None:
        try:
            return self.books[isbn]
        except KeyError:
            return None


library = Library({"1234": "Pan Tadeusz", "123": "Lalka"})
print(library.find_book("1234"))
