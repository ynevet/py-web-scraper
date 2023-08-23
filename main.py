from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import html
import datetime

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

products = []
prices = []
currencies = []
ratings = []

driver.get("https://uae.sharafdg.com/c/computing/laptops/macbooks/")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
for a in soup.findAll('a', href=True, attrs={'class': 'ratio-box product-link'}):
    name = a.find('h4', attrs={'class': 'name'})
    price = a.find('div', attrs={'class': 'price'})
    currency, amount = html.unescape(price.text).split()
    rating = a.find('span', attrs={'class': 'product-rating-count'})
    prices.append(amount.strip())
    currencies.append(currency.strip())
    products.append(name.text.strip())
    ratings.append(rating.text.strip().strip('()'))


df = pd.DataFrame(
    {'Product Name': products, 'Price': prices, 'Currency': currency, 'Rating': ratings})

current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month

df['year'] = current_year
df['month'] = current_month

df.to_csv('products.csv', index=False, encoding='utf-8')
df.to_parquet('data.parquet', engine='pyarrow',
              partition_cols=['year', 'month'])