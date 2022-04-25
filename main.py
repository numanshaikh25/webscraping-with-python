from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = "https://www.netflix.com/in/browse/genre/839338"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
scraped_movies = soup.find('ul',class_="nm-content-horizontal-row-item-container")
movies = []
for movie in scraped_movies:
    movies.append(movie.get_text().strip())

links = soup.find('ul',class_="nm-content-horizontal-row-item-container").find_all('a',attrs={'href': re.compile("^https://")})
href_links = []
for link in links:
    href_links.append(link.get('href'))
    
    
images = soup.find('ul',class_="nm-content-horizontal-row-item-container").find_all('img')
movie_images = []
for image in images:
    movie_images.append(image['src'])


data = pd.DataFrame()
data['Title Name'] = movies
data['Link'] = href_links
data['Image Link'] = movie_images
data.head()
data.to_csv('Popular on Netflix.csv', index = False)
