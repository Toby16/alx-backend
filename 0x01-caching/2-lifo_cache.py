#!/usr/bin/env python3
"""
LIFO caching
"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching
# from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    a class that inherits from 'BaseCaching' class
    and is a caching system -
    LAST IN. FIRST OUT Caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        A method to assign to the dictionary 'self.cache_data'
        the item value for the key 'key' following the LIFO caching system

        Args:
            key - The key for an item
            item - The item belonging to a key
        """
        if (key is None) or (item is None):
            pass
        else:
            # self.cache_data[key] = item

            if key not in self.cache_data:
                if ((len(self.cache_data) + 1) > self.MAX_ITEMS):
                    # key, value = self.cache_data.popitem()

                    # Get the last value
                    dict_key, dict_value = (self.cache_data).popitem()
                    print("DISCARD: {}".format(dict_key))

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        A method to return the value
        in 'self.cache_data' linked to a key

        Args:
            key - The key for an item in 'self.cache_data'
        """
        try:
            if key is None:
                return None
            else:
                return self.cache_data[key]
        except Exception as e:
            return None


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
