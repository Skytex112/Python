class Library:
    def __init__(self, name, address, books):
        self.name = name
        self.address = address
        self.books = books

    def __add__(self, value):
        return Library(self.name, self.address, self.books + value)

    def __sub__(self, value):
        return Library(self.name, self.address, self.books - value)

    def __iadd__(self, value):
        self.books += value
        return self

    def __isub__(self, value):
        self.books -= value
        return self

    def __lt__(self, other):
        return self.books < other.books

    def __gt__(self, other):
        return self.books > other.books

    def __le__(self, other):
        return self.books <= other.books

    def __ge__(self, other):
        return self.books >= other.books

    def __eq__(self, other):
        return self.books == other.books

    def __ne__(self, other):
        return self.books != other.books

    def __str__(self):
        return f"{self.name}, {self.address}, books: {self.books}"