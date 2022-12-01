import csv
import urllib.request
from pathlib import Path
import shutil
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

IMG_FOLDER = OUTPUT_FOLDER / "IMG"

CSV_FOLDER = OUTPUT_FOLDER / "CSV"

def delete_file_if_already_exist(dir_to_check,dir_to_delete):
    """To avoid problem with folder and files alrdeady existing
    this function delete output folder if he exist.

    Args:
        dir_to_check (path): directory to check
        dir_to_delete (path): directory to delete if exist
    """
    for element in dir_to_check.iterdir():
        if element == dir_to_delete:
            shutil.rmtree(element)
        pass



def write_books_csv_file(list_of_dictionary):
    """This function use all books dictionary to
    data in csv

    Args:
        dictionnary (dict): all books in dictionnary
    """
    with open(
        CSV_FOLDER / "books-listing.csv", "w", newline="", encoding="utf-8"
    ) as books_listing:
        writer = csv.DictWriter(books_listing, fieldnames=DATA_TO_SCRAPE)
        writer.writeheader()
        writer.writerows(list_of_dictionary)


def dl_img_in_sub_dir(list_of_dictionary):
    """This function download all books images.
    all images are put in subdirectory names by category

    Args:
        dictionary (dict): all books in dictionnary
    """
    for element in track(list_of_dictionary, description="LOAD data"):
        folder_path = IMG_FOLDER / element["CATEGORY"]
        folder_path.mkdir(exist_ok=True)
        urllib.request.urlretrieve(
            element["IMAGE_URL"],
            f'{folder_path}/{element["CATEGORY"]} - {element["UNIVERSAL_PRODUCT_CODE"]}.jpg',
        )



        
     
                