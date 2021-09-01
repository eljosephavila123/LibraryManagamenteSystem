from colors import bcolors
from Book import Book
from LibraryManagamenteSystem import LibraryManagamenteSystem
from Student import Student
from datetime import datetime
from datetime import timedelta


def menuAdmistrador(lms):
    """[Displays the menu for the administrator]

    Args:
        lms ([LibraryManagamenteSystem]): [LibraryManagamenteSystem]
    """
    print(f"{bcolors.BOLD}{bcolors.WARNING}Administador Menu{bcolors.ENDC}")
    admin_flag = True
    while admin_flag:
        print("1. Add Book")
        print("2. Find Book")
        print("3. View available books")
        print("4. Lend Books")
        print("5. Exit")
        option = input("Choose option: ")
        if option == "1":
            code = input("Code: ")
            if lms.findBook(code) == None:
                title = input("Title: ")
                author = input("Author: ")
                quantity = int(input("Quantity: "))
                lms.addBook(Book(code, title, author, quantity))
            else:
                lms.addBookExisting(code)
        if option == "2":
            code = input("Code: ")
            book = lms.findBook(code)
            print(book)
        if option == "3":
            lms.displayAvabileBooks()
        if option == "4":
            lms.displayNotAvabileBooks()
        if option == "5":
            admin_flag = False


def bookLend(book, borrowed_book):
    """[Verify if the student has already borrowed the book or if the loan period has expired]"""
    for bookL in borrowed_book:
        if bookL["book"] == book or bookL["datatime"] == str(datetime.now())[0:10]:
            return False
    return True


def menuStudent(lms, student):
    """[Displays the menu for the student]

    Args:
        lms ([LibraryManagamenteSystem]): [LibraryManagamenteSystem]
        student ([Student): [Student]
    """
    print(f"{bcolors.BOLD}{bcolors.WARNING}Student Menu{bcolors.ENDC}")
    student_flag = True
    while student_flag:
        print("1. View available books")
        print("2. Lend Book")
        print("3. Exit")
        option = input("Choose option: ")
        if option == "1":
            lms.displayAvabileBooks()
        if option == "2":
            last30days = datetime.now() + timedelta(days=30)
            code = input("Code: ")
            book = lms.lendBookStudent(lms.findBook(code))
            nextto = bookLend(book, student.borrowed_books)
            if nextto:
                print("a. Lend book")
                print("b. Cancel book loan")
                optionLend = input("Choose option: ")

                if optionLend == "a":
                    student.lendBookLibray(book, str(last30days)[0:10])
                if optionLend == "b":
                    lms.addBookExisting(code)
            else:
                print("Book already borrowed")
        if option == "3":
            student_flag = False


def principalMain():
    """[Displays the main menu]"""
    print(
        f"{bcolors.BOLD}{bcolors.WARNING}Welcome to the library management system{bcolors.ENDC}"
    )
    print("1. Login")
    print("2. Exit")


def login():
    """[Application Login]"""
    login_flag = True
    lms = LibraryManagamenteSystem()
    student = Student("student", "student")
    while login_flag:
        principalMain()
        option = input("Choose option: ")
        if option == "1":
            user_id = input("User ID: ")
            password = input("Password: ")
            if user_id == "admin" and password == "admin":
                menuAdmistrador(lms)
            elif user_id == "student" and password == "student":
                menuStudent(lms, student)
            else:
                print("Invalid user")
        if option == "2":
            login_flag = False


if __name__ == "__main__":
    login()
