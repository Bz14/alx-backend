#!/usr/bin/env python3
""" simple helper function """


def index_range(page: int, page_size: int) -> tuple:
    """ return a tuple of start index and an end index """
    return ((page - 1) * page_size, page * page_size)
