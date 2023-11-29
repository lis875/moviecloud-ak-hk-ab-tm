api_key = "24090bf84e01e51e608087ab308902c7"

import requests
import json
import pprint

##### Useful URLS
# Base URL for accessing the TMBD API
movies_base = "https://api.themoviedb.org/3/"

# Additional URLS for searching
movie_search = movies_base + "search/movie"

##### Code for accessing TMBD
query1 = "Avatar"

parameter = {"api_key": api_key, "query": query1}


result_movie = requests.get(movie_search, parameter)

# Convert the results from JSON to a dictionary
movie_result = json.loads(result_movie.text)

movie_id = movie_result["results"][0].get("id")
print("movie id :",movie_id)

movie_credits = movies_base + "movie/" + str(movie_id) + "/credits"
result_credits = requests.get(movie_credits, parameter)
results2 = json.loads(result_credits.text)

# pprint.pprint(results2)
actors = []

for g in results2['cast'][:15]:
    actors.append(g['name'])

print(actors)
