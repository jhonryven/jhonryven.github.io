import json
import os

DATA_FILE = "library_data.json"


# ----------------------- Data Handling -----------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(books):
    with open(DATA_FILE, "w") as f:
        json.dump(books, f, indent=4)


# ----------------------- Core Functions -----------------------
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()

    book = {
        "title": title,
        "author": author,
        "available": True
    }
    books.append(book)
    save_data(books)
    print("Book added successfully.")


def view_books(books):
    if not books:
        print("No books in the library yet.")
        return

    print("\n--- Library Books ---")
    for idx, book in enumerate(books, 1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{idx}. {book['title']} by {book['author']} - {status}")
    print()


def search_books(books):
    keyword = input("Enter title or author keyword: ").lower()
    results = [b for b in books if keyword in b["title"].lower() or keyword in b["author"].lower()]

    if not results:
        print("No matching books found.")
        return

    print("\n--- Search Results ---")
    for book in results:
        status = "Available" if book["available"] else "Borrowed"
        print(f"{book['title']} by {book['author']} - {status}")
    print()


def borrow_book(books):
    view_books(books)
    choice = int(input("Enter book number to borrow: ")) - 1

    if 0 <= choice < len(books):
        if books[choice]["available"]:
            books[choice]["available"] = False
            save_data(books)
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
    else:
        print("Invalid selection.")


def return_book(books):
    view_books(books)
    choice = int(input("Enter book number to return: ")) - 1

    if 0 <= choice < len(books):
        if not books[choice]["available"]:
            books[choice]["available"] = True
            save_data(books)
            print("Book returned successfully.")
        else:
            print("This book is not borrowed.")
    else:
        print("Invalid selection.")


# ----------------------- Main Menu -----------------------
def main():
    books = load_data()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book(books)
        elif choice == "2":
            view_books(books)
        elif choice == "3":
            search_books(books)
        elif choice == "4":
            borrow_book(books)
        elif choice == "5":
            return_book(books)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
