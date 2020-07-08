import requests
from bs4 import BeautifulSoup

URL = 'https://dicionariocriativo.com.br/'


def scraper_word(word):
    page = requests.get(URL + word)

    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.find(id='sinant')

    elements = content.find_all('a', class_='c_primary_hover')
    synonyms = set()
    antonyms = set()

    for elem in elements:
        if "c_primary" in elem["class"]:
            antonyms.add(elem.text)
        else:
            if word != elem.text:
                synonyms.add(elem.text)

    return synonyms, antonyms
