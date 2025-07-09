import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

movies = [movie.text for movie in soup.find_all("h3", class_="title")]
with open("movies.txt", "w", encoding="utf-8") as file:
    for i in range(len(movies) - 1, -1, -1):
        file.write(f"{movies[i]}" + "\n")

print("Top 100 Movies Listed in Movies.txt")


