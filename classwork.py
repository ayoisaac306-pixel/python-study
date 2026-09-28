import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
author TEXT,
year INTEGER,
genre TEXT
)
''')
conn.commit()
conn.close()

# Create models

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title} | {self.author} | {self.year} | {self.genre}"


#CRUD functions

def add_books(book):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
INSERT INTO books (title, author, year, genre)
VALUES (?, ?, ?, ?)
''', (book.title, book.author, book.year, book.genre))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM books')
    rows = cursor.fetchall()

    conn.close()
    return rows
    
    

def get_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM books WHERE id = ?', (book_id,))
    book = cursor.fetchone()

    conn.close()
    return book

def update_book_genre(book_id, new_genre):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('''
UPDATE books    
SET genre = ?
WHERE id = ?
''', (new_genre, book_id)
)          
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()

#App console
while True:
    print("--- LIBRARY MANAGEMENT SYSTEM ---")

    print("1. Add Book")
    print("2. View Books")
    print("3. Find Book")
    print("4. Update Book Genre")
    print("5. Delete Book")
    print("6. Exit")

    choice = (input("Select an option: "))

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Author name: ")
        year = int(input("Date published: "))
        genre = input("Book genre: ")

        book = Book(title, author, year,genre)
        add_books(book)
        print("Book added successfully")

    elif choice == "2":
        books = view_books()
        for b in books:
            print(b)

    elif choice == "3":
        book_id = int(input("input book id: "))
        book = get_book(book_id)
        if book is None:
            print("Book not found")
        else:
            print("Book info:", book)

    elif choice == "4":
        book_id = int(input("input book id: "))
        book = get_book(book_id)
        if book is None:
                print("Book not found")
        else:
            new_genre = input("Enter new genre: ")
            update_book_genre(book_id, new_genre)
            print("Book updated successfully")

    elif choice == "5":
        book_id = int(input("input book id: "))
        book = get_book(book_id)
        if book is None:
                print("Book not found")
        else:
            print("Book info:", book)
            confirm = input("Are you sure you want to delete?(yes/no): ")
        
            if confirm.lower() == "yes":
                delete_book(book_id)
                print("Book deleted")
            else:
             print("Delete cancelled") 

    elif choice == "6":
        print("Goodbye")
        break

    else:
        print("Enter a valid option")        




