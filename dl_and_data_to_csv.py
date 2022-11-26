import csv
import urllib.request
from pathlib import Path
from rich.progress import track


DATA_TO_SCRAPE = [
    "PRODUCT_PAGE_URL",
    "UNIVERSAL_PRODUCT_CODE",
    "TITLE",
    "PRICE_INCLUDING_TAXE",
    "PRICE_EXCLUDING_TAXE",
    "NUMBER_AVAILABLE",
    "PRODUCT DESCRIPTION",
    "CATEGORY",
    "REVIEW_RATING",
    "IMAGE_URL",
]

current_path = Path.cwd()

OUTPUT_FOLDER = current_path / "OUTPUT"

IMG_FOLDER =  OUTPUT_FOLDER / "IMG"

CSV_FOLDER =  OUTPUT_FOLDER / "CSV"


def creat_dir_and_sub_dir(path_1,path_2,path_3):
    path_1.mkdir(exist_ok= True)
    path_2.mkdir(exist_ok= True)
    path_3.mkdir(exist_ok= True)

 

def write_books_csv_file(dictionnary):
    with open(CSV_FOLDER / "books-listing.csv","w",newline="",encoding="utf-8") as books_listing:
        writer = csv.DictWriter(books_listing, fieldnames=DATA_TO_SCRAPE)
        writer.writeheader()
        writer.writerows(dictionnary)
    

def dl_img_in_sub_dir(dictionnary):
    for element in track(dictionnary,description="TRANSFORM data"):
        folder_path = IMG_FOLDER / element["CATEGORY"]
        folder_path.mkdir(exist_ok=True) 
        urllib.request.urlretrieve(
            element["IMAGE_URL"],
            f'{folder_path}/{element["CATEGORY"]} - {element["UNIVERSAL_PRODUCT_CODE"]}.jpg')

