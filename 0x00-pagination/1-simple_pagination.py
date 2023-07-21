#!/usr/bin/env python3
"""
Return a tuple of size two containing a start index and an end index
"""
import csv
import math
from typing import List, Tuple
is_inst = isinstance


def index_range(page: int, page_size: int) -> Tuple:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters.
    """
    start_page = (page - 1) * page_size
    end_page = page * page_size
    return (start_page, end_page)


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
        return the appropriate page of the dataset
        """
        assert is_inst(page, int) and is_inst(page_size, int)
        assert page > 0 and page_size > 0

        start_page, end_page = index_range(page, page_size)
        end_page = min(end_page, len(self.dataset()))

        if start_page > len(self.dataset()):
            return []

        return self.__dataset[start_page:end_page]
