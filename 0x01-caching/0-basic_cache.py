#!/usr/bin/env python3
"""
Basic dictionary
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if (key is None) or (item is None):
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        try:
            if key is None:
                return None
            else:
                return self.cache_data[key]
        except Exception as e:
            return None


if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
