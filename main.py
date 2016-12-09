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
    input_file = 'yes.1.gz'
    output_file = 'page.html'
    os.remove(output_file)
    with open(output_file, 'a') as page:
        with gzip.open(input_file) as file:
            parser = ManParser(file, page)
            parser.parse_man()


