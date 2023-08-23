#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    a class that inherits from 'BaseCaching' class
    and is a caching system -
    FIRST IN. FIRST OUT Caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        A method to assign to the dictionary 'self.cache_data'
        the item value for the key 'key' following the FIFO caching system

        Args:
            key - The key for an item
            item - The item belonging to a key
        """
        if (key is None) or (item is None):
            pass
        else:
            self.cache_data[key] = item

            if (len(self.cache_data) > self.MAX_ITEMS):
                # key, value = self.cache_data.popitem()

                # Get the first value
                first_key = next(iter(self.cache_data))

                # Pop it out of the dictionary
                first_value = (self.cache_data).pop(first_key)

                """
                After discarding the first item in the dict,
                include the next data
                """
                print("DISCARD: {}".format(first_key))

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
    my_cache = FIFOCache()
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
