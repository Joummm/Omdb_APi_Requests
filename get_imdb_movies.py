import requests
import json

# Function to obtain movie information using the OMDb API
def get_movie_information(title):
    api_key = "Put-here-your-key-from-omdb"
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    movie_data = response.json()
    return movie_data

# Function to create a JSON file containing information about a list of movies
def create_json_movies(movie_list):
    movie_data_list = []

    # Iterate through the list of movies
    for index, movie in enumerate(movie_list, start=1):
        # Obtain information about the movie from the OMDb API
        movie_info = get_movie_information(movie)

        # Check if the API response is successful
        if movie_info["Response"] == "True":
            # Extract relevant information and create a dictionary for the movie
            movie_data_dict = {
                "id": index,
                "name": movie_info["Title"],
                "year": movie_info["Year"],
                "poster": movie_info["Poster"]
                # you can put here more requests
            }

            # Add the movie information to the list
            movie_data_list.append(movie_data_dict)

    # Write the list of movie information to a JSON file
    with open("movies.json", "w") as json_file:
        json.dump(movie_data_list, json_file, indent=2)

if __name__ == "__main__":
    # Read the list of movies from a text file
    with open("movie_list.txt", "r") as list_file:
        movie_list = [line.strip() for line in list_file]

    # Call the function to create a JSON file with movie information
    create_json_movies(movie_list)
