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
    user_input = input("Enter\n"
                       "'a' to add a movie,\n"
                       "'l' to see your movie,\n"
                       "'f' to find a movie and\n"
                       "'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print('Unknown command, please try again!')

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movie, 'f' to find a movie and 'q' to quit: ")


def add_movie():
    movie_name = input('What is the movie name?: ')
    movie_director = input('Who is the movie director?: ')
    movie_year = input('Which year was it released? (YYYY): ')

    movies.append({
        'name': movie_name,
        'director': movie_director,
        'year': movie_year
    })


def show_movie(movies_list):
    for movie in movies_list:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by = input('What property of the movie are you looking for?'
                    'Name?\n'
                    'Director?\n'
                    'Year?: ')
    looking_for = input('What are you searching for?: ')

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movie(found_movies)


def find_by_attribute(items, expected, finder):
    found = []
    for i in movies:
        if finder(i) == expected:
            found.append(i)

        return found


menu()

