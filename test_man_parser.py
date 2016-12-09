import gzip
import os
import unittest
import re

from man_parser import ManParser


class ManTester(unittest.TestCase):
    def test_emphasis(self):
        input_file = 'ls.1.gz'
        output_file = 'page.html'
        source = ''
        try:
            os.remove(output_file)
        except FileNotFoundError:
            pass
        with open(output_file, 'a') as page:
            with gzip.open(input_file) as file:
                parser = ManParser(file, page)
                parser.parse_man()
        with open("page.html") as file:
            source = file.read()
        bold_teg = re.compile("<b>(.*?)</b>")
        bold_text = re.compile("-{1,2}\w*")
        for teg in re.findall(bold_teg, source):
            self.assertTrue((re.match(bold_text, teg) is not None) or
                            (teg.replace(' ', '') == parser.title.lower()))

