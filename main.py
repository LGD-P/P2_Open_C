import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.progress import track

from urllib.parse import urljoin


from dl_img_and_get_data_to_csv import (
    delete_file_if_already_exist,
    current_path,
    write_books_csv_file,
    dl_img_in_sub_dir,
    OUTPUT_FOLDER,
    IMG_FOLDER,
    CSV_FOLDER,
    DATA_TO_SCRAPE,
)

from display_answer import table, return_pretty_message

c = Console()

# This list will contain all category of books.
category_list = []

# This list will contain all url books
url_books_page = []

# This list will contain all scraped datas for every books ass dictionary.
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

    # category_list[0] is not a category we need to delete it
    category_list.pop(0)


######################################

# Here we check every category pages
# and we try to find if there  next-pages
# We get the next page href and add result to
# category_list


def get_url_cat_if_more_one_page(firsts_pages_urls):
    """This fuction use the  category_list
    to get pages when there is more than one.

    Args:
        firsts_pages_urls (list): category_list

    Returns:
        append next page in category list
    """
    for next_page in track(
        firsts_pages_urls, description="EXTRACT all URL by CATEGORY"
    ):

        requests_all_pages = requests.get(next_page)
        soup_all_pages = BeautifulSoup(requests_all_pages.text, "html.parser")
        find_number_of_pages = soup_all_pages.find("li", class_="next")

        if find_number_of_pages:
            category_list.append(
                urljoin(next_page, find_number_of_pages.select("a")[0].get("href"))
            )

        else:
            pass


######################################
# Now that we have all pages to scrape
# we can get every books url
######################################


def get_url_books_pages(all_category_pages_url):
    """This functions get all the 1000 Url Books
    Args:
        all_category_pages_url (list): all category url
    """

    for each_url in track(
        all_category_pages_url, description="EXTRACT all URL by BOOKS"
    ):
        request_url_for_books = requests.get(each_url)

        soup_books_url = BeautifulSoup(request_url_for_books.text, "html.parser")

        for each_url in soup_books_url.find_all("h3"):
            end_of_url = each_url.find("a").get("href")
            url_books_page.append(
                end_of_url.replace("../../../", "https://books.toscrape.com/catalogue/")
            )


def scrape_all_books(CONSTANT, url_of_every_book):
    """This function scrape all books
    and creat a dictionnary with DATA_TO_SCRAPE
    constant

    Args:
        url_of_every_book (list): list of all url books
    """

    for books in track(url_of_every_book, description="TRANSFORM 1000 books"):
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
            element
            for element in get_number_available_full_str
            if int(element.isdigit())
        ]

        get_number_available = "".join(get_number_available_in_list)

        get_product_description = soup_book_try.select("p")[3].text

        get_category = soup_book_try.find("ul", class_="breadcrumb").select("a")[2].text

        get_view_rating = soup_book_try.select("td")[6].text

        # Here data is only the end of img url,
        # once the data scraped we replace ../../ whit the begining url
        # to get full img url

        get_image_url_first_step = soup_book_try.find("img").get("src")

        get_image_url = get_image_url_first_step.replace(
            "../../", "https://books.toscrape.com/"
        )

        # We create a list with all data for each books
        # This list will be used as values for a dictionary
        data_list_scrapped = [
            get_product_page_url,
            get_upc,
            get_book_name,
            get_price_including_tax,
            get_price_excluding_tax,
            get_number_available,
            get_product_description,
            get_category,
            get_view_rating,
            get_image_url,
        ]

        # creat dictionary with constat data to scrape as keys.
        data_in_dict = dict(zip(CONSTANT, data_list_scrapped))

        # add dictionary as book in books list
        BOOKS_DICT_LIST.append(data_in_dict)


if __name__ == "__main__":
    get_category_list_url(URL)
    get_url_cat_if_more_one_page(category_list)
    get_url_books_pages(category_list)
    delete_file_if_already_exist(current_path,OUTPUT_FOLDER)   
    OUTPUT_FOLDER.mkdir(exist_ok=True)
    IMG_FOLDER.mkdir(exist_ok=True)
    CSV_FOLDER.mkdir(exist_ok=True) 
    scrape_all_books(DATA_TO_SCRAPE, url_books_page)
    write_books_csv_file(BOOKS_DICT_LIST)
    dl_img_in_sub_dir(BOOKS_DICT_LIST)
    return_pretty_message(table)
