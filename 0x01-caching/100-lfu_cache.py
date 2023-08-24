#!/usr/bin/env python3
"""
LFU Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    a class that inherits from 'BaseCaching' class
    and is a caching system -
    LEAST FREQUENTLY USED
    """
    def __init__(self):
        super().__init__()
        # Dictionary to track the frequency of key accesses
        self.frequency = {}

    def put(self, key, item):
        """
        A method to assign to the dictionary 'self.cache_data'
        the item value for the key 'key' following the LFU caching system

        Args:
            key - The key for an item
            item - The item belonging to a key
        """
        if (key is None) or (item is None):
            pass
        else:
            if key in self.cache_data:
                # Update the value
                # and increase the frequency count for the updated key
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                # If the cache is full, pop the least frequently used item
                if (len(self.cache_data) + 1) > self.MAX_ITEMS:
                    least_freq_used_key = min(self.frequency,
                                              key=lambda k: self.frequency[k])
                    del self.cache_data[least_freq_used_key]
                    del self.frequency[least_freq_used_key]
                    print("DISCARD: {}".format(least_freq_used_key))

                self.cache_data[key] = item
                self.frequency[key] = 1

    def get(self, key):
        """
        A method to return the value
        in 'self.cache_data' linked to a key

        Args:
            key - The key for an item in 'self.cache_data'
        """
        if (key is None) or (key not in self.cache_data):
            return None
        else:
            self.frequency[key] += 1
            return self.cache_data[key]


if __name__ == "__main__":
    my_cache = LFUCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    print(my_cache.get("B"))
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
    my_cache.put("H", "H")
    my_cache.print_cache()
    my_cache.put("I", "I")
    my_cache.print_cache()
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    print(my_cache.get("I"))
    print(my_cache.get("H"))
    my_cache.put("J", "J")
    my_cache.print_cache()
    my_cache.put("K", "K")
    my_cache.print_cache()
    my_cache.put("L", "L")
    my_cache.print_cache()
    my_cache.put("M", "M")
    my_cache.print_cache()
