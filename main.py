from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
with open("The 100 Greatest Movies _ Movies _ Empire.html") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
films = [film.getText() for film in soup.select(selector='h3.title')]
with open("movies.txt", mode="w") as file:
    for _ in range(len(films)):
        file.write(f"{films.pop()}\n")

