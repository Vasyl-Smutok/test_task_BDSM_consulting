import csv
import os
from dataclasses import dataclass, astuple
import requests
from bs4 import BeautifulSoup
import pandas as pd

MOVIE_OUTPUT_CSV_PATH = "detail_of_movie.csv"
MOVIE_FIELDS = [
    "name",
    "original_name",
    "IMDb_rating",
    "country",
    "duration",
    "description",
]

URL_TO_PARSE = os.environ.get(
    "URL_TO_PARSE", "https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html"
)

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 "
    "Safari/537.36 "
}


@dataclass
class Movie:
    name: str
    original_name: str
    IMDb_rating: str
    country: str
    duration: str
    description: str


def parse_single_page() -> BeautifulSoup:
    page = requests.get(URL_TO_PARSE, headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def parse_detail_of_movie(soup: BeautifulSoup) -> Movie:
    name = soup.select_one("h1").text
    original_name = soup.select_one(".b-post__origtitle").text
    IMDb_rating = soup.select_one(
        "div > table > tr:nth-child(1) > td:nth-child(2) > span.b-post__info_rates.imdb > span"
    ).text
    country = soup.select_one(
        "div > table > tr:nth-child(5) > td:nth-child(2) > a"
    ).text
    duration = soup.select_one("div > table > tr:nth-child(10) > td:nth-child(2)").text
    description = soup.select_one(".b-post__description_text").text

    return Movie(
        name=name,
        original_name=original_name,
        IMDb_rating=IMDb_rating,
        country=country,
        duration=duration,
        description=description,
    )


def write_courses_to_csv(movie: Movie) -> None:
    with open(MOVIE_OUTPUT_CSV_PATH, "w") as file:
        writer = csv.writer(file)
        writer.writerow(MOVIE_FIELDS)
        writer.writerow(astuple(movie))


if __name__ == "__main__":
    soup = parse_single_page()
    detail_of_movie = parse_detail_of_movie(soup)
    write_courses_to_csv(detail_of_movie)

    data = pd.read_csv(MOVIE_OUTPUT_CSV_PATH)
    print(data.head())
