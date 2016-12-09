import re


italic_pattern = re.compile("\\\\fI\\\\(.*?)\\\\fR")


def italic_replace(group):
    return "<i>{}</i>".format(group.group+(1))


def italic_regexp_func(string):
    return re.sub(italic_pattern, italic_replace, string)


REGEXP_REPLACE_FUNCS = [italic_regexp_func]




