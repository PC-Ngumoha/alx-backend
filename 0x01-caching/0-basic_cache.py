#!/usr/bin/python3
"""
0-basic_cache.py
Implements a class 'BasicCache' which inherits from the class 'BaseCaching'
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache
    """
    def put(self, key, item):
        """
        put(key, item)

        Args:
          - key (any) -> key to locate @item stored in cache
          - item (any) -> item we want to store at @key in cache.

        Returns:
          - None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        get(key)

        Args:
          - key (any) -> key to locate item stored in cache.

        Returns:
          - self.cache_data[key] -> value located at @key in cache or None.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
