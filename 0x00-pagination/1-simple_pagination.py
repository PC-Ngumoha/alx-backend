#!/usr/bin/env python3
"""
1-simple_pagination.py

Contains code that implements a simple pagination system based on
the limit/offset style/approach to pagination.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    index_range(page, page_size)

    Args:
      - page (int) -> The page number we want to read from.
      - page_size (int) -> How many elements of information can be on a page.

    Returns:
      - tuple<int, int> -> tuple of start_index (int) and end_index (int)
    """
    start_index = page * page_size - page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page(page, page_size)

        Args:
          - page (int) -> We want to return the page at this number.
          - page_size (int) -> Number of elements each page contains.

        Return:
          - Page[List[elements]] -> The correct page with the correct number
            of elements
        """
        self.dataset()  # Fetch dataset from CSV file
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index < 0 or end_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index: end_index]
