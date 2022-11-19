import shutil
import os
from pathlib import Path


path = Path.cwd()

first_list_of_category = ["Travel","Mystery","Historical-Fiction","Sequential-Art",
                          "Classics","Philosophy","Romance","Womens-Fiction2","Fiction",
                          "Childrens","Religion","Nonfiction","Music","Default","Science-Fiction",
                          "Sports-and-Games","Add-a-comment","Fantasy","New-Adult","Young-Adult",
                          "Science","Poetry","Paranormal","Art","Psychology","Autobiography","Parenting",
                          "Adult-Fiction","Humor","Horror","Food-and-Drink","Christian-Fiction",
                          "Business","Biography","Thriller","Contemporary","Spirituality","Academic",
                          "Historical","Christian","Suspense","Short-Stories","Novels","Health","Politics",
                          "Cultural","Erotica","Crime","History","Self-Help"]

"""second_list_of_category = ["History","Self-Help"]"""


    # Historial Fiction et Self Health ? 
    # retélécharger avec le bon nom de fichier. -"-"

def creat_dir_from_img_category(list_of_catagery):
    for path_name in list_of_catagery:
        folder_name = path_name
        folder_path = path / folder_name
        folder_path.mkdir(exist_ok=True)
    
        
creat_dir_from_img_category(first_list_of_category)

"""creat_dir_from_img_category(second_list_of_category)"""

def move_image_in_dir(list_of_category):
    for path_name in list_of_category :
        for img in path.iterdir():
            if path_name in img.name:
                shutil.move(img, path_name)
                
move_image_in_dir(first_list_of_category)
            
"""
for path_name in second_list_of_category :
    for img in path.iterdir():
        if path_name in img.name:
            shutil.move(img, path_name)

"""

## Dossier ART et Dossier FICTION posent problème car il s'agit de nom de dossier composé.
## Sequential-Art se retrouve dans ART etc... 