#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves the index range from a given page and page size
    """
    i = 0
    tuple_value = ()

    value_1 = 0
    value_2 = page_size

    while i < page:
        tuple_value = (value_1, value_2)
        value_1 += page_size
        value_2 += page_size

        i += 1

    return tuple_value


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
