from app import books

USER_CHOICES = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to quit

Enter your Choice: '''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)

# print('--- Best ---')
# print_best_books()
# print('--- Cheapest ---')
# print_cheapest_books()

# ===================================================
# !!!!!!!!!!!!!!! Error here...
# AttributeError: 'NoneType' object has no attribute 'attrs'
# ===================================================


books_generator = (x for x in books)


def get_next_book():
    print(next(books_generator))


def menu():
    user_input = input(USER_CHOICES)
    while user_input != 'q':
        if user_input == 'b':
            print_best_books()
        elif user_input == 'c':
            print_cheapest_books()
        elif user_input == 'n':
            get_next_book()
        else:
            print('Please choose a valid Choice.')
        user_input = input(USER_CHOICES)


menu()

