import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track
from rich import print

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


DATA_TO_SCRAPE = [
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

url_books_page = []

BOOKS_DICT_LIST = []

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
                category_list.append(
                    urljoin(next_page, find_number_of_pages.select('a')[0].get('href'))
                    )
                
            else:
                pass


######################################
######################################


# GET BOOKS URL FROM  CATEGORY PAGES #


######################################
######################################



def get_url_books_pages(all_category_pages_url):
    """This functions get all the 1000 books Url

    Args:
        all_category_pages_url (list): final category url
    """

    for each_url in track(all_category_pages_url, description=
                            "Scrapping all URL by BOOKS"):
            request_url_for_books = requests.get(each_url)

            soup_books_url = BeautifulSoup(request_url_for_books.text, 
                                            "html.parser")

            for each_url in soup_books_url.find_all("h3"):
                    end_of_url = each_url.find("a").get("href")
                    url_books_page.append(
                            
                            end_of_url.replace(
                                    "../../../",
                                    "https://books.toscrape.com/catalogue/")
                            )


def scrape_all_books(CONSTANT,url_of_every_book):
    """This function scrape all books 
    and creat a dictionnary with DATA_TO_SCRAPE
    constant
    

    Args:
        url_of_every_book (list): list of all url books
    """

    for books in track(url_of_every_book, description="Scraping 1000 books in .csv"):
        book_try_request = requests.get(books)

        soup_book_try = BeautifulSoup(book_try_request.text, "html.parser")

        get_product_page_url = books

        get_book_name = (
            soup_book_try.find("div", class_="col-sm-6 product_main").find("h1").text
        )

        get_upc = soup_book_try.find("td").text

        get_price_including_tax = soup_book_try.select("td")[2].text[1:]

        get_price_excluding_tax = soup_book_try.select("td")[3].text[1:]

        get_number_available_full_str = soup_book_try.select("td")[5].text

        # here data is a string, with number available inside.
        # We create a comprehension list, avoiding a for loop, to get a list with only the
        # digits . Then we join those elements, to get back in a string, numbers available

        get_number_available_in_list = [
            element for element in get_number_available_full_str if int(element.isdigit())
        ]

        get_number_available = "".join(get_number_available_in_list)

        get_product_description = soup_book_try.select("p")[3].text

        get_category = soup_book_try.find("ul", class_="breadcrumb").select("a")[2].text

        # In this part we remane some category to be able to clean easaly our 
        # directory later.

        get_view_rating = soup_book_try.select("td")[6].text

        # Here data is only the end of img url,
        # once the data scraped we replace ../../ whit the begining url
        # to get full img url

        get_image_url_first_step = soup_book_try.find("img").get("src")

        get_image_url = get_image_url_first_step.replace(
            "../../", "https://books.toscrape.com/"
        )

        # We create a list with all data for each books
        data_list_scrapped = [
            get_product_page_url,
            get_upc,
            get_book_name,            
            get_price_including_tax,
            get_price_excluding_tax,
            get_number_available,
            get_product_description,
            get_category,
            get_image_url,
        ]


        data_in_dict = dict(zip(CONSTANT,data_list_scrapped))
        
        BOOKS_DICT_LIST.append(data_in_dict)
        
        print(BOOKS_DICT_LIST)


"""
urllib.request.urlretrieve(
    get_image_url, get_category + "-" + get_upc + "-" + ".jpg"
)
# We use a function to write in csv file each elements of our list
write_data_in_csv(data_list_scrapped)
"""

if __name__ == "__main__":
    write_csv_headers(DATA_TO_SCRAPE)
    get_category_list_url(URL)
    get_url_cat_if_more_one_page(category_list)    
    get_url_books_pages(category_list)
    scrape_all_books(DATA_TO_SCRAPE, url_books_page)

    """
    creat_dir_from_img_category(CATEGORY_LIST_FOR_DIR)
    move_img_into_dir(CATEGORY_LIST_FOR_DIR)
    move_img_dir_in_main_dir(CATEGORY_LIST_FOR_DIR)
    move_csv_file_to_listing_dir()
    return_pretty_message(table)
    """
    
    




    
