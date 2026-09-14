from datetime import date

books = []  # will hold all books; each book = [id, title, author, status, borrower, due_date]

def add_book(books, book_id, title, author):
    new_book = [book_id, title, author, "Available", "", ""]
    books.append(new_book)
    return books

def is_duplicate_id(books, book_id):
    for book in books:
        if book[0] == book_id:
            return True
    return False

def get_book_status(books, book_id):
    for book in books:
        if book[0] == book_id:
            return book[3]
    return None

def view_books(books):
    if len(books) == 0:
        print("No books in the system yet.")
    else:
        print("\n===== BOOK LIST =====")
        for book in books:
            print("ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            print("Borrower:", book[4])
            print("Due Date:", book[5])
            print("-----------------------")

def borrow_book(books, book_id, borrower_name, due_date):
    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Borrowed"
                book[4] = borrower_name
                book[5] = due_date
                return True
            else:
                return False
    return False

def return_book(books, book_id):
    for book in books:
        if book[0] == book_id:
            if book[3] == "Borrowed":
                book[3] = "Available"
                book[4] = ""
                book[5] = ""
                return True
            else:
                return False
    return False

def mark_missing(books, book_id):
    for book in books:
        if book[0] == book_id:
            if book[3] == "Missing":
                return False
            else:
                book[3] = "Missing"
                return True
    return False

def mark_found(books, book_id):
    for book in books:
        if book[0] == book_id:
            if book[3] == "Missing":
                book[3] = "Available"
                return True
            else:
                return False
    return False

def check_overdue(books):
    today = str(date.today())
    found = False
    for book in books:
        if book[3] == "Borrowed" and book[5] < today:
            print("OVERDUE - ID:", book[0], "- Title:", book[1], "- Due:", book[5], "- Borrower:", book[4])
            found = True
        elif book[3] == "Missing":
            print("MISSING - ID:", book[0], "- Title:", book[1])
            found = True
    if not found:
        print("No overdue or missing books.")

while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("[1] Add Book")
    print("[2] View Books")
    print("[3] Borrow Book")
    print("[4] Return Book")
    print("[5] Check Overdue/Missing Books")
    print("[6] Mark Book Missing")
    print("[7] Mark Book Found")
    print("[8] Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID (or type 'cancel' to go back): ").strip()

        while book_id == "" or (book_id.lower() != "cancel" and is_duplicate_id(books, book_id)):
            if book_id == "":
                print("Book ID cannot be blank.")
            else:
                print("That Book ID already exists. Please use a different one.")
            book_id = input("Enter Book ID (or type 'cancel' to go back): ").strip()

        if book_id.lower() == "cancel":
            print("Add Book cancelled.")
        else:
            title = input("Enter Title: ").strip()
            while title == "":
                print("Title cannot be blank.")
                title = input("Enter Title: ").strip()

            author = input("Enter Author: ").strip()
            while author == "":
                print("Author cannot be blank.")
                author = input("Enter Author: ").strip()

            books = add_book(books, book_id, title, author)
            print("Book added successfully!")
    elif choice == "2":
        view_books(books)
    elif choice == "3":
        book_id = input("Enter Book ID to borrow (or type 'cancel' to go back): ").strip()

        if book_id.lower() == "cancel":
            print("Borrow Book cancelled.")
        else:
            borrower_name = input("Enter your name (or type 'cancel' to go back): ").strip()
            while borrower_name == "":
                print("Name cannot be blank.")
                borrower_name = input("Enter your name (or type 'cancel' to go back): ").strip()

            if borrower_name.lower() == "cancel":
                print("Borrow Book cancelled.")
            else:
                due_date = input("Enter due date (YYYY-MM-DD): ")

                if len(due_date) == 10 and due_date[4] == "-" and due_date[7] == "-":
                    success = borrow_book(books, book_id, borrower_name, due_date)
                    if success:
                        print("Book borrowed successfully!")
                    else:
                        print("Book not available or not found.")
                else:
                    print("Invalid date format. Please use YYYY-MM-DD, example: 2026-01-01")
    elif choice == "4":
        book_id = input("Enter Book ID to return: ")
        success = return_book(books, book_id)
        if success:
            print("Book returned successfully!")
        else:
            status = get_book_status(books, book_id)
            if status == "Missing":
                print("This book is marked Missing, not Borrowed. Use option 7 (Mark Book Found) instead.")
            elif status == "Available":
                print("This book is already Available — it wasn't borrowed.")
            elif status is None:
                print("Book not found.")
            else:
                print("Book not found or not currently borrowed.")
    elif choice == "5":
        check_overdue(books)
    elif choice == "6":
        book_id = input("Enter Book ID to mark as missing (or type 'cancel' to go back): ").strip()
        if book_id.lower() == "cancel":
            print("Mark Missing cancelled.")
        else:
            success = mark_missing(books, book_id)
            if success:
                print("Book marked as missing.")
            else:
                print("Book not found or already marked missing.")
    elif choice == "7":
        book_id = input("Enter Book ID to mark as found (or type 'cancel' to go back): ").strip()
        if book_id.lower() == "cancel":
            print("Mark Found cancelled.")
        else:
            success = mark_found(books, book_id)
            if success:
                print("Book marked as found and is now available.")
            else:
                print("Book not found or not currently marked missing.")
    elif choice == "8":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 8.")