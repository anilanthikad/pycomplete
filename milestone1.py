"""
- Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie and 'q' to quit:
    - Add movies
    - See movies
    - Find movies
    - Stop running movies

Tasks:
[]: Where to store movies.
[]: What format of a movie?
[]: Show the user the main interface and get their input.
[]: Allow user to add movies
[]: Show all their movies
[]: Find a movie
[]: Stop running the program when they type "q"
"""

movies = []

"""
movie = {
    'name': (str),
    'director': (str).
    'year': (int)
}
"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command, please try again!')

        user_input = input("Enter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie and 'q' to quit: ")


def add_movie():
    movie_name = input('What is the movie name?: ')
    movie_director = input('Who is the movie director?: ')
    movie_year = int(input('Which year was it released? (YYYY): '))

    movies.append({
        'name': movie_name,
        'director': movie_director,
        'year': movie_year
    })


menu()

print(movies)
