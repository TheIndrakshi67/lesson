books = ["Python Basics", "Data Science", "Machine Learning"]

books.append("Deep Learning")

books.remove("Data Science")

books.sort()

books.reverse()

first_book = books[0]
print("First book:", first_book)

some_books = books[0:2]
print("Sliced books:", some_books)

librarian = {
    "name": "Alice",
    "id": 101,
    "shift": "Morning"
}

librarian["email"] = "alice@library.com"

print("Librarian Name:", librarian["name"])

book_ids = [1001, 1002, 1003]
book_titles = ["Mathematics", "Science", "History"]

book_directory = dict(zip(book_ids, book_titles))
print("Book Directory:", book_directory)
