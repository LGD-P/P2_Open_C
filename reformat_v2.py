import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track

import urllib.request
from urllib.parse import urljoin


from write_data import write_csv_headers, write_data_in_csv
from clean_directory import (
    creat_dir_from_img_category,
    move_img_into_dir,
    move_img_dir_in_main_dir,
    move_csv_file_to_listing_dir,
    CATEGORY_LIST_FOR_DIR,
)
from answer_set import table, return_pretty_message


c = Console()


DATA_TO_SCRAPT = [
    "PRODUCT_PAGE_URL",
    "UNIVERSAL_PRODUCT_CODE",
    "TITLE",
    "PRICE_INCLUDING_TAXE",
    "PRICE_EXCLUDING_TAXE",
    "NUMBER_AVAILABLE",
    "PRODUCT8DESCRIPTION" "CATEGORY",
    "REVIEW_RATING",
    "IMAGE_URL",
]


category_list = []

category_list_next_pages = []

final_category_list = []

url_books_page = []

data_list_scrapped = []

URL = requests.get("https://books.toscrape.com/catalogue/page-1.html")



def get_category_list_url(constant_url):
        """Using main URL of web site
        this function get all first url page of 
        each book category

        Args:
            constant_url (requests.models.Response'): URL as 
            requests.get(url)
        """

        soup = BeautifulSoup(constant_url.text, "html.parser")

        main_page = soup.find("ul", {"class": "nav nav-list"})


        for element in main_page.find_all("a"):
                first_url_part = "https://books.toscrape.com/catalogue/"
                category_list.append(first_url_part + element.get("href"))

        category_list.pop(0)


######################################
######################################

# Here we check every category pages
# and we try to find if there  next-pages
# We get the number of pages and
# we concatenate url.
# We need to creat a new list otherwise
# we creat an infinit loop



def get_url_cat_if_more_one_page(firsts_pages_urls):
        """This fuction use the first category url part
        to get pages when there is more than one page

        Args:
            firsts_pages_urls (list): list of category

        Returns:
            first_list + next_pages_list
        """
        for next_page in track(firsts_pages_urls,
                              description="Scrapping all URL by CATEGORY"):
            
            

            requests_all_pages = requests.get(next_page)
            soup_all_pages = BeautifulSoup(requests_all_pages.text,"html.parser")
            find_number_of_pages = soup_all_pages.find("li",class_="next")
            
            if find_number_of_pages:
                category_list.append(urljoin(next_page, find_number_of_pages.select('a')[0].get('href')))
                
            else:
                pass

get_category_list_url(URL)

get_url_cat_if_more_one_page(category_list)

print(len(category_list))




    
