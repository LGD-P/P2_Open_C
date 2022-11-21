from rich.console import Console
from rich.table import Table


c = Console()

table = Table(
    title="[u bold red]\n\n** FELICITATION TOUS LES FICHIERS ONT ETE TELECHARGES "
    "**\n[/u bold red]"
)

table.add_column("FICHIER .CSV",justify="center",style="dark_blue",no_wrap=False,
                 header_style="orange3",)

table.add_column("IMAGES", style="dark_blue", justify="center", no_wrap=False, 
                 header_style="orange3")

table.add_row(
    "[left]- Dans le repertoire courant, un fichier [bold blue u i]LISTING-CSV"
    "[/bold blue u i] a été crée.\n\n- Il contient l'intégralité des données du site:\n"
    "[bold blue u i]https://books.toscrape.com/index.html[/bold blue u i][/left] dans"
    " un fichier csv","- Les images des livres ont toutes été téléchargées par "
    "categorie, et placées dans des sous dossiers leur correspondant, elles sont "
    "nommées avec chaque N° de produit pour identification.\n\n - Le tout est contenu "
    "dans le dossier [bold blue u i]IMG[/bold blue u i], les fichiers sont identifiable "
    "par comparaison\n"
)


def return_pretty_message(table):
    """From created Table
    return a pretty answer at the end
    of the script

    Args:
        table (class 'rich.table.Table'):
        2 columns to describe the content
        of the files created according to
        their category .csv or .jpg
    """
    return c.print(table)
