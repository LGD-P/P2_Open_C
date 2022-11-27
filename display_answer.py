from rich.console import Console
from rich.table import Table


c = Console()

table = Table(
    title="[u bold red]\n\n** FELICITATION TOUS LES FICHIERS ONT ETE TELECHARGES "
    "**\n[/u bold red] \n"
    "[u bold yellow]Un fichier OUTPUT contient le résultat dans des sous dossiers CSV "
    "et IMG:[/u bold yellow]\n\n"
)

table.add_column(
    "FICHIER .CSV",
    justify="center",
    style="dark_blue",
    no_wrap=False,
    header_style="orange3",
)

table.add_column(
    "IMAGES", style="dark_blue", justify="center", no_wrap=False, header_style="orange3"
)

table.add_row(
    "[left]- Dans le sous dossier  [bold blue u i]CSV:[/bold blue u i].\n\n"
    "- L'intégralité des données du site:\n"
    "[bold green u i]https://books.toscrape.com/index.html[/bold green u i]\n\n"
    "- Ont été stockées dans un fichier [bold red u i]books-listing.csvdans"
    "[/bold red u i] un fichier csv.[/left]",
    "- Les images des livres ont toutes été téléchargées dans un sous  dossier "
    " [bold blue u i]IMG:[/bold blue u i] \n\n"
    "- Chaque image est classée dans la catégorie du livre qui lui correspond\n\n"
    "- Elles sont identifiables grace à leur [bold red u i]N°UPC[/bold red u i]",
)


def return_pretty_message(table):
    """From created Table
    return a pretty answer at the end
    of the script

       Args:
        table (class 'rich.table.Table'

    Returns:
       2 columns to describe the content
        of the files created according to
        their category .csv or .jpg
    """
    return c.print(table)
