import gzip
import os

from man_parser import ManParser

if __name__ == '__main__':
    os.remove("page.html")
    with open("page.html", 'a') as page:
        with gzip.open('yes.1.gz') as file:
            parser = ManParser(file, page)
            parser.parse_man()


