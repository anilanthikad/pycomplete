from utils import database

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


def prompt_add_book():  #  ask for book name and author
    name = input('Enter the name of the book: ')
    author = input('Enter the name of the author: ')

    database.add_book(name, author)


def list_books():  #  show all the books in our list
    books = database.get_all_books()
    for book in books:
        print(book)

def prompt_read_book():  #  ask for book name and change it to "read"
    pass

def prompt_delete_book():  #  ask the book and delete the book from list
    pass



