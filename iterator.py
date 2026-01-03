class BookCollection:
    def __init__(self, books):
        self.books = books
    
    def __iter__(self):
        return BookIterator(self.books)

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0
    
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

if __name__ == "__main__":
    library = BookCollection(["Война и мир", "Преступление и наказание"])
    for book in library:
        print(f"Читаю: {book}")
