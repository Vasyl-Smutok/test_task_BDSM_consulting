import os
import pandas as pd

csv_name = "detail_of_movie.csv"

command = f"scrapy crawl detail_of_movie -O {csv_name}"
os.system(command)


def read_csv_pandas(csv_name):
    data = pd.read_csv(csv_name)
    print(data.head())


if __name__ == '__main__':
    read_csv_pandas(csv_name)

