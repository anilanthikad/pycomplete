from utils import database_csv

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

# user_input = input('')


def menu():
    database_csv.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Unknown command! Please try again.')

        user_input = input(USER_CHOICE)


def prompt_add_book():  # ask for book name and author
    name = input('Enter the name of the book: ')
    author = input('Enter the name of the author: ')

    database_csv.add_book(name, author)


def list_books():  # show all the books in our list
    books = database_csv.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():  # ask for book name and change it to "read"
    name = input('Enter the name of the book you finished reading: ')

    database_csv.mark_book_as_read(name)


def prompt_delete_book():  # ask the book and delete the book from list
    name = input('Enter the name of the book you wish to delete: ')

    database_csv.delete_book(name)


menu()

