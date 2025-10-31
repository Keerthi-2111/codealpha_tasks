import requests
from bs4 import BeautifulSoup
import pandas as pd


titles = []
prices = []
ratings = []


for page in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        # Title
        title = book.h3.a['title']
        titles.append(title)
        
        
        price = book.find('p', class_='price_color').text
        prices.append(price)
        
        
        rating = book.p['class'][1]  # example: "One", "Two", "Three"
        ratings.append(rating)


df = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings
})

# Save as CSV file
df.to_csv('books_dataset.csv', index=False, encoding='utf-8')

print("✅ Dataset created successfully: books_dataset.csv")
print(df.head())

