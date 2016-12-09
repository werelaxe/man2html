import gzip
import os
import sys
from man_parser import ManParser
import parsing_arguments


if __name__ == '__main__':
    """
    parser = parsing_arguments.get_parser()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = vars(parser.parse_args(sys.argv[1:]))
    print(args)
    input_file = args["input"]
    output_file = args["output"]
    """
    input_file = 'ls.1.gz'
    output_file = 'page.html'
    try:
        os.remove(output_file)
    except FileNotFoundError:
        pass
    with open(output_file, 'a') as page:
        with gzip.open(input_file) as file:
            parser = ManParser(file, page)
            parser.parse_man()


