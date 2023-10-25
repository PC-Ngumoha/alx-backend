#!/usr/bin/python3
"""
100-lfu_cache.py
Implements the class 'LFUCache' which inherits from the class 'BaseCaching'
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache
    """
    def __init__(self):
        """
        __init__() method
        """
        super().__init__()
        self.frequency_count = {}

    def put(self, key, item):
        """
        put(key, item)

        Args:
          - key (any) -> key in cache at which we store @item
          - item (any) -> item we want to store at @key in cache.

        Returns:
          - None
        """
        if key is not None and item is not None:
            if key in self.frequency_count:
                self.frequency_count[key] += 1
            else:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    keys_by_frequency = list(
                        dict(
                            sorted(
                                self.frequency_count.items(),
                                key=lambda x: x[1]
                            )
                          ).keys()
                        )
                    print(keys_by_frequency)
                    lfu_item_key = keys_by_frequency[0]
                    self.cache_data.pop(lfu_item_key)
                    self.frequency_count.pop(lfu_item_key)
                    print('DISCARD: {}'.format(lfu_item_key))
                self.frequency_count[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """
        get(key)

        Args:
          - key (any) -> key in cache at which we store the item.

        Returns:
          - self.cache_data[key] or None
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency_count[key] += 1
        return self.cache_data[key]
