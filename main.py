import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich import print

# with rich library, we creat Console() object as c,  
# to color some output for users

c = Console()

# Creat a list of every data we need to scrap

data_to_scrap = ["PRODUCT_PAGE_URL", 
                 "UNIVERSAL_PRODUCT_CODE",
                 "TITLE",
                 "PRICE_INCLUDING_TAXE",
                 "PRICE_EXCLUDING_TAXE",
                 "NUMBER_AVAILABLE",
                 "PRODUCT8DESCRIPTION"
                 "CATEGORY",
                 "REVIEW_RATING",
                 "IMAGE_URL"
                 ]


# This list will contain every category of book

category_list = []

URL = requests.get("https://books.toscrape.com/catalogue/page-1.html")

soup = BeautifulSoup(URL.text, 'html.parser')

main_page = soup.find("ul", {"class": "nav nav-list"})



for element in main_page.find_all("a"):
    first_url_part = "https://books.toscrape.com/catalogue/"
    list_of_category_books_url = category_list.append(first_url_part + element.get("href"))
    
print(category_list)