import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'https://manascinema.com/schedule/'

HEADERS = {'Accept': 'text/html,application/xhtml+xml,applitcation/xml;q=0.9,image/avif'}

def html_content_content(url, params=None):
    try:
        response = requests.get(url=url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        raise e

def get_data(html):
    soup = bs(html, 'html.parser')
    manas_films = []
    items = soup.find_all('div', class_='creation-schedule-item')
    for item in items:
        title = item.find('div', class_='creation-title')
        info = item.find('div', class_='creation-genre')
        title = title.text
        genre = item.text.split(',')[0]
        country = item.text.split(',')[1]
        duration = item.text.split(',')[2]
        manas_films.append({
            'title': title,
            'genre': genre,
            'country': country,
            'duration': duration})
    return manas_films

def parser():
    for i in range(25, 28):
        html = html_content_content(URL, params=f'{i}.10.2024')
        films = get_data(html.content)
        return films


