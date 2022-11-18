import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich import print
from rich.progress import track

from write_data import write_csv_headers, write_data_in_csv

# with rich library, we creat Console() object as c,  
# to color some output for users

c = Console()


# Creat a list of every data we need to scrap
# We use this list to get headers of csv file

DATA_TO_SCRAPT = ["PRODUCT_PAGE_URL", 
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


# with csv library we creat a books_listing file 
# we will fill the first row as header with data_to_scrap list

write_csv_headers(DATA_TO_SCRAPT)

# This list will contain every category of books

category_list = []

category_list_next_pages = []


# This list will contain every urls books 

url_books_page = []

"""
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


######################################
######################################

# Here we check every category pages 
# and we try to find if there  next-pages
# We get the number of pages and 
# we concatenate url. 
# We need to creat a new list otherwise 
# we creat an infinit loop


for each_category in track(category_list, description="Scrapping all URL CATEGORY PAGES") :
    
    try:      
        requests_all_pages = requests.get(each_category)
        soup_all_pages = BeautifulSoup(requests_all_pages.text, 'html.parser')
        find_number_of_pages = soup_all_pages.find("li", class_="current").text.strip()
        
        for number_of_pages in range(int(find_number_of_pages[-1])):
            number_of_pages +=1
            category_list_next_pages.append(each_category.replace("index.html","page-"+str(number_of_pages)+".html"))          
    except:
        pass
      

final_category_list = category_list + category_list_next_pages

"""

######################################
######################################


#TRY TO GET BOOKS URL FROM 
# CATEGORY PAGES


######################################
######################################


url_test = ["https://books.toscrape.com/catalogue/category/books/travel_2/index.html", 
            "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
            ]


for each_url in url_test:
    request_url_for_books = requests.get(each_url)

    soup_books_url = BeautifulSoup(request_url_for_books.text, "html.parser")


    for each_url in soup_books_url.find_all("h3"):
        end_of_url = each_url.find("a").get("href")
        url_books_page.append(end_of_url.replace("../../../","https://books.toscrape.com/catalogue/" ))

print(url_books_page)
print(len(url_books_page))








"""

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

    # Here we start data from second character [1:] because first one 
    # is special 
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
    
    # We create a list with all data for each books
    data_list_scrapped = [get_product_page_url,get_book_name,get_upc,
                            get_price_including_tax,get_price_excluding_tax,
                            get_number_available,get_product_description,
                            get_category,get_image_url]
    
    # We use a function to write in csv file each elements of our list
    write_data_in_csv(data_list_scrapped)

""" 





