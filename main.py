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


# This list will contain every category of books

category_list = []


# We requests main page with categorys to scrape

URL = requests.get("https://books.toscrape.com/catalogue/page-1.html")

# We creat a Bs4 object to parse data 

soup = BeautifulSoup(URL.text, 'html.parser')

main_page = soup.find("ul", {"class": "nav nav-list"})


# We creat a loop to get each category of books
# Then we fill category_list whit it.
# "href" give us the end of category url
# so we concatenate this first_url_part with "a" to get full category url

for element in main_page.find_all("a"):
    first_url_part = "https://books.toscrape.com/catalogue/"
    list_of_category_books_url = category_list.append(first_url_part + element.get("href"))
    
# First element of category list is an index and not a category
# so we remove it.
category_list.pop(0)


############################################
############################################

#### TRY ON ONE BOOK

############################################

# Same process as the main page we request url and creat a Bs4 object to scrape data


book_try_url = ["https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", 
                "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
                "https://books.toscrape.com/catalogue/soumission_998/index.html"
                ]

for books in book_try_url:
    book_try_request = requests.get(books)

    soup_book_try = BeautifulSoup(book_try_request.text, "html.parser")


    get_product_page_url = books

    c.print("-------" * 10, style= "bold blue",justify= 'center')
    c.print("-------" * 10, style= "bold blue",justify= 'center')
    c.print("NEW BOOK", style= "bold green", justify= 'center')
    c.print("-------" * 10, style= "bold blue",justify= 'center')
    c.print("-------" * 10, style= "bold blue",justify= 'center')
    
    print(get_product_page_url)
    c.print("-------" * 10, style= "bold red")

    get_book_name = soup_book_try.find("div", class_="col-sm-6 product_main").find("h1").text

    print(get_book_name)
    c.print("-------" * 10, style= "bold red")

    get_upc = soup_book_try.find("td").text

    print(get_upc)
    c.print("-------" * 10, style= "bold red")

    get_price_including_tax = soup_book_try.select("td")[2].text[1:]

    print(get_price_including_tax)
    c.print("-------" * 10, style= "bold red")

    get_price_excluding_tax  = soup_book_try.select("td")[3].text[1:]

    print(get_price_excluding_tax)
    c.print("-------" * 10, style= "bold red")

    get_number_available_full_str =  soup_book_try.select("td")[5].text

    # here data is a string, with number available inside.
    # We create a comprehension list, avoiding a for loop, to get a list with only the
    # digits . Then we join those elements, to get back in a string, numbers available 

    get_number_available_in_list = [element 
                                for element in get_number_available_full_str 
                                if int(element.isdigit())
                                ]

    get_number_available = "".join(get_number_available_in_list)

    print(get_number_available)
    c.print("-------" * 10, style= "bold red")

    get_product_description = soup_book_try.select("p")[3].text

    print(get_product_description)
    c.print("-------" * 10, style= "bold red")

    get_category = soup_book_try.find("ul", class_="breadcrumb").select('a')[2].text

    print(get_category)
    c.print("-------" * 10, style= "bold red")

    get_view_rating = soup_book_try.select("td")[6].text

    print(get_view_rating)
    c.print("-------" * 10, style= "bold red")

    # Here data is only the end of img url, 
    # once the data scraped we replace ../../ whit the begining url
    # to get full img url

    get_image_url_first_step = soup_book_try.find("img").get("src")

    get_image_url = get_image_url_first_step.replace("../../","https://books.toscrape.com/")


    print(get_image_url)
    print("")
    print("")
    
    





