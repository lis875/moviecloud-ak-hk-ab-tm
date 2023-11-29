api_key = "24090bf84e01e51e608087ab308902c7"

import requests
import json
import pprint

movies_base = "https://api.themoviedb.org/3/"
movie_search = movies_base + "search/movie"

query1 = "Avatar"
parameter = {"api_key": api_key, "query": query1}
result_movie = requests.get(movie_search, parameter)
movie_result = json.loads(result_movie.text)

movie_id = movie_result["results"][0].get("id")
movie_credits = movies_base + "movie/" + str(movie_id) + "/credits"

result_credits = requests.get(movie_credits, parameter)
results2 = json.loads(result_credits.text)

actors = []
for g in results2['cast'][:15]:
    actors.append(g['name'])
print(actors)
