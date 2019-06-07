#!/usr/bin/python3

"""A module for append_after."""


def append_after(filename="", search_string="", new_string="")
    """Inserts a line of text to a file, after each line containing a specific
    string."""
    with open(filename, encoding='utf-8') as f:
        for i in f:
            if search_string == i:
                f.append(new_string)
