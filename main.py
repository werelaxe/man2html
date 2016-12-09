import gzip
import os
import sys
from man_parser import ManParser
import parsing_arguments


if __name__ == '__main__':
    parser = parsing_arguments.get_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = vars(parser.parse_args(sys.argv[1:]))
    print(args)
    os.remove("page.html")
    with open("page.html", 'a') as page:
        with gzip.open('yes.1.gz') as file:
            parser = ManParser(file, page)
            parser.parse_man()


