import shutil
from pathlib import Path


path = Path.cwd()

CATEGORY_LIST_FOR_DIR = ["Travel","Mystery","Classics","Philosophy","Romance","Fiction",
                         "Childrens","Religion","Nonfiction","Music","Default","Sports-and-Games",
                         "Add-a-comment","Fantasy","New-Adult","Young-Adult","Science","Poetry",
                         "Paranormal","Art","Psychology","Autobiography","Parenting","Adult-F",
                         "Humor","Horror","Food-and-Drink","Business","Biography","Thriller",
                         "Contemporary","Spirituality","Academic","Historical","Christian",
                         "Suspense","Short-Stories","Novels","Health","Politics","Cultural",
                         "Erotica","Crime","History","Self-Help","Hist-F","S-F","W-F","Ch-F",
                         "Sequential-A"]

   
    # Historial Fiction et Self Health
    # retélécharger avec le bon nom de fichier. -"-"

def creat_dir_from_img_category(list_of_category):
    """Creat each directory from each category of book

    Args:
        list_of_category (list): Use list to 
        get name of each directory
    """
    for path_name in list_of_category:
        folder_name = path_name
        folder_path = path / folder_name
        folder_path.mkdir(exist_ok=True)
    
        
def move_img_into_dir(list_of_category):
    """Move every img to her books category

    Args:
        list_of_category (list): _Use list
        of category to move img in appropriate 
        directory
    """
        
    for path_name in list_of_category:
        for img in path.iterdir():
            if path_name in img.name:
                shutil.move(img, path_name)
    


def move_img_dir_in_main_dir(list_of_dir):
    """Move every folder containing img
       in a general folder IMG
    

    Args:
        list_of_dir (list): use constant 
        CATEGORY_LIST_FOR_DIR
    """
    for category in list_of_dir:
        for imgs_folders in path.iterdir():
            if category in imgs_folders.name:
                main_folder_for_img_folder = Path.cwd() / 'IMG'
                main_folder_for_img_folder.mkdir(exist_ok=True)
                shutil.move(imgs_folders,main_folder_for_img_folder)
                

def move_csv_file_to_listing_dir():
    """Loop in current folder to find
    .csv file and move it, into appropriate 
    folder: LISTING-CSV
    """
   
    
    for csv_file in path.iterdir():
        if csv_file.suffix == ".csv":
            folder_for_csv = path / "LISTING-CSV"
            folder_for_csv.mkdir(exist_ok= True)
            shutil.move(csv_file, folder_for_csv)