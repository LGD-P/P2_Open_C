# Projet de Scrapring : <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width=60 align=center>  


# Books Online: <img src="ico/Books-Online.png" width=60 align=center>

*C'est  un projet python qui vise à faire une étude de marché sur un site de livre en ligne pour récupérer l'intégalité des données suivantes dans un fichier .csv:* 

- product_page_url
- universal_ product_code (upc)
- title
- price_including_tax
- price_excluding_tax
- number_available
- product_description
- category
- review_rating
- image_url

*Enfin toutes les images relatives aux livres seront également récupérées.*


## Liste des commandes à exécuter pour lancer le programme:

_Pré-requis: se placer depuis le terminal dans le dossier où l'on exécute le script:_

Avant toute chose on clone le répository git:

> git clone [https://github.com/LGD-P/P2_Open_C.git](https://github.com/LGD-P/P2_Open_C.git)


Une fois le projet cloné on crée et on active l'environnement virtuel:

> python3 -m venv env \
source env/bin/activate


Puis on lance l'installation des modules nécessaires au fonctionnement du script:

> pip install -m requirements.txt


Il n'y a plus qu'à exécuter le script:

> python3 main.py


*Les fichiers seront téléchargés dans un dossier OUTPUT; il contient :* 

* Un sous-dossier CSV avec le fichier books-listing.csv
* Et un sous-dossier IMG, avec les images classées dans des dossiers par catégories, et identifiées par leur numéro UPC.
