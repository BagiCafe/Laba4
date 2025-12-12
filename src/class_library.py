from src.collections_user import BookCollection, IndexDict


class Library:
    """
    Класс библиотеки, который управляет коллекциями книг и их индексами

    Args:
        name: Название библиотеки
        books: Коллекция всех книг
        index: Индекс для быстрого поиска книг
    """
    def __init__(self, name: str = "Главная библиотека"):
        self.name = name
        self.books = BookCollection()
        self.index = IndexDict()

    def __repr__(self) -> str:
        return f"Library('{self.name}', books={len(self.books)})"

    def append_book(self, book) -> None:
        """"Добавляет книгу в библиотеку"""
        self.books.append(book)
        self.index.append_book(book)

    def remove_book(self, book) -> None:
        """Удаляет книгу из библиотеки"""
        if book in self.books:
            self.books.remove(book)
            self.index.remove_book(book)

    def search_isbn(self, isbn: str):
        """Находит книгу по ISBN"""
        return self.index.search_isbn(isbn)

    def search_author(self, author: str) -> list:
        """Находит все книги выбранного автора"""
        return self.index.search_author(author)

    def search_year(self, year: int) -> list:
        """Находит все книги выбранного года издания"""
        return self.index.search_year(year)