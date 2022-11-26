import csv
from reformat_v2 import DATA_TO_SCRAPE
import urllib.request
from pathlib import Path



current_path = Path.cwd()

OUTPUT_FOLDER = current_path / "OUTPUT"

IMG_FOLDER =  OUTPUT_FOLDER / "IMG"

CSV_FOLDER =  OUTPUT_FOLDER / "CSV"


def creat_dir_and_sub_dir(path_1,path_2,path_3):
    path_1.mkdir(exist_ok= True)
    path_2.mkdir(exist_ok= True)
    path_3.mkdir(exist_ok= True)

    
    
creat_dir_and_sub_dir(OUTPUT_FOLDER, IMG_FOLDER,CSV_FOLDER)


dico = [{
        'PRODUCT_PAGE_URL': 
'https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html',
        'UNIVERSAL_PRODUCT_CODE': 'ce60436f52c5ee68',
        'TITLE': 'Full Moon over Noahâs Ark: An Odyssey to Mount Ararat and Beyond',
        'PRICE_INCLUDING_TAXE': '£49.43',
        'PRICE_EXCLUDING_TAXE': '£49.43',
        'NUMBER_AVAILABLE': '15',
        'PRODUCT DESCRIPTION' :'Acclaimed travel writer Rick Antonson....',
        'CATEGORY': 'Paranormal',
        'REVIEW_RATING': '12',
        'IMAGE_URL': 'https://books.toscrape.com/media/cache/fe/8a/fe8af6ceec7718986380c0fde9b3b34f.jpg'
    },
    {
        'PRODUCT_PAGE_URL': 
'https://books.toscrape.com/catalogue/see-america-a-celebration-of-our-national-parks-treasured-sites_732/index.html',
        'UNIVERSAL_PRODUCT_CODE': 'f9705c362f070608',
        'TITLE': 'See America: A Celebration of Our National Parks & Treasured Sites',
        'PRICE_INCLUDING_TAXE': '£48.87',
        'PRICE_EXCLUDING_TAXE': '£48.87',
        'NUMBER_AVAILABLE': '14',
        'PRODUCT DESCRIPTION':"To coincide with the 2016 centennial......",
        'CATEGORY': 'Travel',
        'REVIEW_RATING': '15',
        'IMAGE_URL': 'https://books.toscrape.com/media/cache/c7/1a/c71a85dbf8c2dbc75cb271026618477c.jpg'
    }]




def write_books_csv_file(dictionnary):
    with open(CSV_FOLDER / "books-listing.csv","w",newline="",encoding="utf-8") as books_listing:
        writer = csv.DictWriter(books_listing, fieldnames=DATA_TO_SCRAPE)
        writer.writeheader()
        writer.writerows(dictionnary)
    

write_books_csv_file(dico)


def dl_img_in_sub_dir(dictionnary):
    for element in dictionnary:
        folder_path = IMG_FOLDER / element["CATEGORY"]
        folder_path.mkdir(exist_ok=True) 
        urllib.request.urlretrieve(
            element["IMAGE_URL"],
            f'{folder_path}/{element["CATEGORY"]} - {element["UNIVERSAL_PRODUCT_CODE"]}.jpg')

dl_img_in_sub_dir(dico)
                                                

