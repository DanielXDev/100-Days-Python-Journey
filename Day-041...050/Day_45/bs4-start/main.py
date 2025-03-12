from operator import indexOf

from bs4 import BeautifulSoup
import requests

# ------- Scraping a local web -------- #
# with open("./website.html") as web:
#     data = web.read()
#
# soup = BeautifulSoup(data, "html.parser")
# print(soup.title.string)


# ------- Live Scraping -------#
response = requests.get("https://news.ycombinator.com/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
link_texts = soup.find_all("span", class_="titleline")
# print(link_texts)
scores = [int(score.getText().split()[0]) for score in soup.find_all("span", class_= "score")]
score = 0
# for span in link_texts:
#     print(f'{span.getText()}: {scores[score]}')
#     score += 1

highest_score = max(scores)
score_id = indexOf(scores, highest_score)
print(f'{link_texts[score_id].getText()}: {highest_score} scores')
