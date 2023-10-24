#!/usr/bin/python3
"""
4-mru_cache.py
Implements the class 'MRUCache' which inherits from class 'BaseCaching'
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    class MRUCache
    """
    def __init__(self):
        """
        __init__()
        """
        super().__init__()
        self.recency_count = {}
        self.recency = 0

    def put(self, key, item):
        """
        put(key, item)

        Args:
          - key (any) -> key in cache to store @item.
          - item (any) -> item to store at @key in cache.

        Returns:
          - None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.recency += 1
            self.recency_count[key] = self.recency
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys_recency = list(dict(
                      sorted(self.recency_count.items(), key=lambda x: x[1])
                    ).keys())
                most_recent_key = keys_recency[len(keys_recency) - 2]
                self.cache_data.pop(most_recent_key)
                self.recency_count.pop(most_recent_key)
                print('DISCARD: {}'.format(most_recent_key))

    def get(self, key):
        """
        get(key)

        Args:
          - key (any) -> key in cache where we seek to retrieve @item.

        Returns:
          - self.cache_data[key] -> item stored at @key in cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.recency += 1
        self.recency_count[key] = self.recency
        return self.cache_data[key]
