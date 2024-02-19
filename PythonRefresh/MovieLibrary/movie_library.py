MENU_PROMPT = "\n Enter 'a' to add a movie, 'l' to list your movies, 'f' to find a movie by title, or 'q' to quit: "
selection = input(MENU_PROMPT)
movie_list = []

def add_movie():
    movie_name=input("Enter the name of the movie: ")
    director_name=input("Enter the name of the movie director: ")
    movie_release_date=input("Enter the date of release: ")
    movie_list.append({"title":movie_name,"director":director_name,"released":movie_release_date})
    print(f"Movie '{movie_name}' by {director_name} released on {movie_release_date} has been added")
def list_movies():
    for index,movie in enumerate(movie_list,start=1):
        print(f"{index}. '{movie['title']}' by {movie['director']} released on {movie['released']} ")
def find_movie():
    search_querry = input('Enter the name of the movie: ')
    for movie in movie_list:
        if movie["title"] == search_querry:
            print(f"'{movie['title']}' by {movie['director']} released on {movie['released']} ")
            break
    else:
        print("no such movie in the library.")

user_functions = {
    "a":add_movie,
    "l":list_movies,
    "f":find_movie
}

def menu(selection):
    while selection !='q':
        if selection in user_functions:
            selected_function = user_functions[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)

menu(selection)
