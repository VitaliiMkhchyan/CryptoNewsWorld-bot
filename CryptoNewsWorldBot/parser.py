""" Парсер криптоновостей """

import requests
from requests import Response
from bs4 import BeautifulSoup
from loguru import logger

headers: dict = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
params: dict = {'page': '1'}

url: str = "https://cryptonews.net"


def get_news() -> dict:
    response: Response = requests.get('https://cryptonews.net/ru/', params=params, headers=headers)

    logger.debug("Получение данных с cryptonews.net")

    soup: BeautifulSoup = BeautifulSoup(response.text, "html.parser")
    news: list = soup.find_all("div", class_="row news-item start-xs")

    # Титульник
    title: str = news[0].find("a", class_="title").text.strip()

    # Полный URL до страницы с новостью
    full_url: str = url + news[0].find("a", class_="title")["href"]

    # Дата выпуска новости
    date: str = news[0].find("span", class_="datetime flex middle-xs").text.strip()

    # Get запрос до страницы с новостью
    response2: Response = requests.get(full_url, headers=headers)
    soup2: BeautifulSoup = BeautifulSoup(response2.text, "html.parser")

    # Находим блок с контентом
    content: str = soup2.find("div", class_="cn-content").text

    logger.debug("Данные получены!")

    return {"title": title,
            "full_url": full_url,
            "date": date,
            "content": content.strip()}


# Test
if __name__ == '__main__':
    print(get_news())
