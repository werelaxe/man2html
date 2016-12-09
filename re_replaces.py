import re


italic_pattern = re.compile("\\\\fI\\\\(.*?)\\\\fR")
bold_pattern = re.compile("\\\\fB\\\\(.*?)\\\\fR")
link_pattern = re.compile("<(http://.*?)>")


def italic_replace(group):
    return "<i>{}</i>".format(group.group(1))


def bold_replace(group):
    return "<b>{}</b>".format(group.group(1))


def link_replace(group):
    return "&lt;<a href=\"{0}\">{0}</a>&gt;".format(group.group(1))


def italic_regexp_func(string):
    return re.sub(italic_pattern, italic_replace, string)


def bold_regexp_func(string):
    return re.sub(bold_pattern, bold_replace, string)


def link_regexp_func(string):
    return re.sub(link_pattern, link_replace, string)


REGEXP_REPLACE_FUNCS = [italic_regexp_func, bold_regexp_func, link_regexp_func]




