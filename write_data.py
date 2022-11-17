import csv


def write_csv_headers(list_of_data_header):
    """Creat headers for csv file

    Args:
        data_header (str): list of data to scrappe
        as headers
    """
    with open("books-listing.csv", "w", newline="", encoding="utf-8",) as books_listing:
        writer = csv.writer(books_listing)
        writer = writer.writerow(list_of_data_header)
        





def write_data_in_csv(list_of_data_scrapped):
    """Open csv file and write data
       in append mode.

    Args:
        data_scrapped (str): list of data scrapped ==>
        books_url, upc, price_including_taxe etc..
    """
    with open("books-listing.csv", "a" , newline ="" , encoding="utf-8") as books_listing:
        writer = csv.writer(books_listing)
        writer = writer.writerow(list_of_data_scrapped)
    