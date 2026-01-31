class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def get_info(self):
        """Получение информации о книге"""
        return f"'{self.title}' - {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        """Добавление книги в библиотеку"""
        new_book = Book(title, author)
        self.books.append(new_book)
        return f"Книга '{title}' добавлена в библиотеку"
liba=Library("gay")
boook=Book
print(liba.add_book("world & piece","Lev Tolstoy"))


