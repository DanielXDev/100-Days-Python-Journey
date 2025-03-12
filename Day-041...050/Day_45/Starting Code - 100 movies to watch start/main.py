import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL1= "https://web.archive.org/web/20200611015421/https://www.empireonline.com/movies/features/best-tv-shows-ever-2/"

# Write your code below this line 👇
response = requests.get(URL)
website = response.text


soup = BeautifulSoup(website, "html.parser")
top_movies = soup.find_all("h3", class_="title")
# print(top_movies)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    file.write("Top 100 Movies 2018")
    for movie in top_movies[::-1]:
        file.write(f'\n{str(movie.getText())}')


