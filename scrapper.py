import requests

from bs4 import BeautifulSoup


def scrapper(url):


    response = requests.get(url)

    soup = BeautifulSoup(response.content, features='lxml')

    link = soup.find('div', {'class': 'mw-parser-output'}).find_all('p')

    test = []


    for i in link:
        test += i.text.split()

    print(test)
    return test
