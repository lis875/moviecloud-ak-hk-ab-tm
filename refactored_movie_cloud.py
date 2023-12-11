import turtle
import requests

API_KEY = "68fb82694c5bb73d9bf877ee4613f426"
BASE_URL = "https://api.themoviedb.org/3"


def get_movie_data(movie_name):
    params = {"api_key": API_KEY, "query": movie_name}
    response = requests.get(f"{BASE_URL}/search/movie", params=params)
    data = response.json()
    if data.get("results"):
        movie_id = data["results"][0]["id"]
        credits_response = requests.get(f"{BASE_URL}/movie/{movie_id}/credits", params={"api_key": API_KEY})
        credits_data = credits_response.json()
        return data["results"][0], credits_data["cast"][:10] if credits_data.get("cast") else None
    return None, None


def draw_movie_cloud(movie, actors):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Movie Cloud")

    t = turtle.Turtle()
    t.speed(2)
    t.hideturtle()
    t.pencolor("black")

    t.penup()
    t.goto(0, 200)
    t.write(movie["title"], align="center", font=("Arial", 30, "bold"))

    t.goto(-180, 40)
    t.color("purple")
    for actor in actors:
        t.write(actor["name"], align="left", font=("Arial", int(actor["popularity"] / 3), "normal"))
        t.goto(t.xcor(), t.ycor() - 25)

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
