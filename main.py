from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import html
import datetime


def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(options=options)


def get_product_data(driver, url):
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    products, prices, currencies, ratings = [], [], [], []

    for a in soup.findAll('a', href=True, attrs={'class': 'ratio-box product-link'}):
        name = a.find('h4', attrs={'class': 'name'})
        price = a.find('div', attrs={'class': 'price'})
        currency, amount = html.unescape(price.text).split()
        rating = a.find('span', attrs={'class': 'product-rating-count'})

        prices.append(amount.strip())
        currencies.append(currency.strip())
        products.append(name.text.strip())
        ratings.append(rating.text.strip().strip('()'))

    return products, prices, currencies, ratings


def main():
    url = "https://uae.sharafdg.com/c/computing/laptops/macbooks/"

    with initialize_driver() as driver:
        products, prices, currencies, ratings = get_product_data(driver, url)

        df = pd.DataFrame({
            'Product Name': products,
            'Price': prices,
            'Currency': currencies,
            'Rating': ratings
        })

        current_date = datetime.date.today()
        df['year'] = current_date.year
        df['month'] = current_date.month

        df.to_csv('products.csv', index=False, encoding='utf-8')
        df.to_parquet('data.parquet', engine='pyarrow',
                      partition_cols=['year', 'month'])


if __name__ == "__main__":
    main()
