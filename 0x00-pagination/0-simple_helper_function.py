#!/usr/bin/env python3
"""
0-simple_helper_function.py

contains the definition of the function 'index_range' which
takes two arguments: page and page_size and returns a tuple
containing the start and end indexes.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range(page, page_size)

    Args:
      - page (int) -> The page number we want to read from.
      - page_size (int) -> How many elements of information can be on a page.

    Returns:
      - tuple<int, int> -> tuple of start_index (int) and end_index (int)
    """
    if page <= 0 or page_size <= 0:
        return (0, 1)
    start_index = page * page_size - page_size
    end_index = page * page_size
    return (start_index, end_index)
