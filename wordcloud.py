import turtle
import requests

def get_movie_data(movie_name):
    api_key = "8bf41bd8dd79b79f2cce125f6eb2bda0"  # Replace with your TMDB API key
    base_url = "https://api.themoviedb.org/3/search/movie"

    params = {"api_key": api_key, "query": movie_name}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["results"]:
        movie_id = data["results"][0]["id"]
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
        credits_params = {"api_key": api_key}
        credits_response = requests.get(credits_url, params=credits_params)
        credits_data = credits_response.json()

        return data["results"][0], credits_data["cast"][:10]  # Get top 10 actors
    else:
        return None, None

def draw_movie_cloud(movie, actors):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Movie Cloud")

    turtle.speed(2)
    turtle.hideturtle()
    turtle.pencolor("Black")

    # Draw movie title
    turtle.penup()
    turtle.goto(0, 200)
    turtle.write(movie["title"], align="center", font=("Arial", 30, "bold"))


    # Draw actors
    turtle.goto(-180, 40)
    turtle.color("purple")
    for actor in actors:
        turtle.write(actor["name"], align="left", font=("Arial", int(actor["popularity"] / 3), "normal"))
        turtle.penup()
        turtle.goto(turtle.xcor(), turtle.ycor() - 25)

    turtle.done()

def main():
    movie_name = input("Enter the name of the movie: ")
    movie, actors = get_movie_data(movie_name)

    if movie and actors:
        actors.sort(key=lambda x: x["popularity"], reverse=True)
        draw_movie_cloud(movie, actors)
    else:
        print("Movie not found.")

if __name__ == "__main__":
    main()
