import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='man to html')

    parser.add_argument('-i', action='store',
                        dest='input', required=True,
                        help='input man file')

    parser.add_argument('-o', action='store',
                        dest='output',
                        help='output man file', default='page.html')
    return parser
