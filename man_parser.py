import re
import re_replaces


def parse_gzfile(gz_file):
    return gz_file.read().decode()


def parse_header(string):
    return "<h2>{}</h2>".format(string.replace("\"", ''))


def parse_bold(string):
    return "<b>{}</b><br>".format(string)


def parse_paragraph(string):
    return "<p>"


def parse_keys(string):
    return string


def parse_title(string):
    main_title = "<h2>{}</h2><br>".format(string.split()[0])
    parts = re.findall("\"(.*?)\"", string)
    section = "Section: {}({})<br>".format(parts[-1], parts[0])
    updated = "Updated: {}<br>".format(parts[1])
    return main_title + section + updated


PARSE_DICT = dict()
REPL_DICT = dict()
PARSE_DICT[".SH"] = parse_header
PARSE_DICT[".B"] = parse_bold
PARSE_DICT[".P"] = parse_paragraph
PARSE_DICT[".PP"] = parse_paragraph
PARSE_DICT[".TH"] = parse_title
REPL_DICT[r"\-"] = "-"
REPL_DICT[r"\(aq"] = "\'"
REPL_DICT[r"\(co"] = "©"
REPL_DICT[r"\/"] = "/"


class ManParser:
    def __init__(self, gz_file, out_page_file):
        self.source = parse_gzfile(gz_file)
        self.out_page_file = out_page_file
        self.body = ["<html>", "<head>", "<title>", "title", "</title>", "</head>", "<body>"]
        self.title = 'title'

    @staticmethod
    def replace_parts(new_line):
        for old_part, new_part in REPL_DICT.items():
            new_line = new_line.replace(old_part, new_part)
        return new_line

    @staticmethod
    def replace_regexps(line):
        for func_regexp in re_replaces.REGEXP_REPLACE_FUNCS:
            line = func_regexp(line)
        return line

    def parse_man(self):
        for line in self.source.split('\n'):
            first_space = line.find(" ")
            start = line[:first_space]
            if not line.startswith("."):
                line = self.replace_regexps(line)
                line = self.replace_parts(line)
                self.body.append(line + "<br>")
                continue
            if start in PARSE_DICT.keys():
                if start == '.TH':
                    self.title = line[first_space:].split()[0]
                    self.body[3] = "Man page of {}".format(line[first_space:].split()[0])
                new_line = PARSE_DICT[start](line[first_space:])
                new_line = self.replace_regexps(new_line)
                new_line = self.replace_parts(new_line)
                self.body.append(new_line)
        self.write_page()

    def write_page(self):
        self.body += ["</body>", "</html>"]
        self.out_page_file.write(''.join(self.body))
