import re
import re_replaces


def parse_gzfile(gz_file):
    return gz_file.read().decode()


def parse_header(string):
    return "<h2>{}</h2><br>".format(string.replace("\"", ''))


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
    print(parts)
    updated = "Updated: {}<br>".format(parts[1])
    return main_title + section + updated


PARSE_DICT = dict()
REPL_DICT = dict()
PARSE_DICT[".SH"] = parse_header
PARSE_DICT[".B"] = parse_bold
PARSE_DICT[".P"] = parse_paragraph
PARSE_DICT[".TH"] = parse_title
# PARSE_DICT["\\fB\\"] =
REPL_DICT[r"\-"] = "-"
REPL_DICT[r"\(aq"] = "\'"
REPL_DICT[r"\(co"] = "©"
# REPL_DICT["\\fI\\"] = "<i>"
# REPL_DICT[r"\fR"] = "</i>"
REPL_DICT[r"\/"] = "/"


class ManParser:
    def __init__(self, gz_file, out_page_file):
        print(REPL_DICT)
        self.source = parse_gzfile(gz_file)
        self.out_page_file = out_page_file
        self.body = []
        self.html_page = ""

    @staticmethod
    def replace_parts(new_line):
        for old_part, new_part in REPL_DICT.items():
            # print(old_part, new_part, new_line, new_line.replace(old_part, new_part))
            return new_line.replace(old_part, new_part)

    @staticmethod
    def replace_regexps(line):
        for func_regexp in re_replaces.REGEXP_REPLACE_FUNCS:
            line = func_regexp(line)

    def parse_man(self):
        for line in self.source.split('\n'):
            first_space = line.find(" ")
            start = line[:first_space]
            if not line.startswith("."):
                new_line = self.replace_parts(line)
                # self.replace_regexps(new_line)
                self.body.append(new_line + "<br>")
            if start in PARSE_DICT.keys():
                new_line = PARSE_DICT[start](line[first_space:])
                new_line = self.replace_parts(new_line)
                # self.replace_regexps(new_line)
                self.body.append(new_line)
        self.write_page()

    def write_page(self):
        self.out_page_file.write(''.join(self.body))
