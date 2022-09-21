import os

import pandas as pd
import scrapy
from scrapy.http import Response


URL_TO_PARSE = os.environ.get(
    "URL_TO_PARSE", "https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html"
)


class DetailOfMovieSpider(scrapy.Spider):
    name = "detail_of_movie"
    allowed_domains = ["rezka.ag"]
    start_urls = [URL_TO_PARSE]

    def parse(self, response: Response, **kwargs):
        yield {
            "name": response.css("h1::text").get(),
            "original_name": response.css(".b-post__origtitle::text").get(),
            "IMDb_rating": response.css(
                "div > table > tr:nth-child(1) > td:nth-child(2) > span.b-post__info_rates.imdb > span::text"
            ).get(),
            "country": response.css(
                "div > table > tr:nth-child(5) > td:nth-child(2) > a::text"
            ).get(),
            "duration": response.css(
                "div > table > tr:nth-child(10) > td:nth-child(2)::text"
            ).get(),
            "description": response.css(".b-post__description_text::text").get(),
        }


def read_csv_pandas(csv_name):
    data = pd.read_csv(csv_name)
    print(data.head())
