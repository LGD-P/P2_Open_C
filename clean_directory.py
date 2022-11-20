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
        list_of_category (lsit): _Use list
        of category to move img in appropriate 
        directory
    """
        
    for path_name in list_of_category:
        for img in path.iterdir():
            if path_name in img.name:
                shutil.move(img, path_name)
    
