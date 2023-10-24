#!/usr/bin/python3
"""
1-fifo_cache.py
Implements the class 'FIFOCache' which inherits from class 'BaseCaching'
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache
    """
    def put(self, key, item):
        """
        put(key, item)

        Args:
          - key (any) -> key to store @item at within the cache.
          - item (any) -> item stored at @key within the cache.

        Returns:
          - None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = list(self.cache_data.keys())[0]
                self.cache_data.pop(popped)
                print('DISCARD: {}'.format(popped))

    def get(self, key):
        """
        get(key)

        Args:
          - key (any) -> Key to store @item within the cache.

        Returns:
          - self.cache_data[key] -> item stored at @key within cache or None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
