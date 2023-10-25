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
        self.recency_count = {}
        self.recency = 0

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
                    min_freq = min(
                        self.frequency_count.items(),
                        key=lambda x: x[1]
                      )[1]
                    min_freq_keys = {k: v
                                     for k, v in self.frequency_count.items()
                                     if v == min_freq
                                     }
                    if len(min_freq_keys) > 1:
                        lru_keys = {k: v
                                    for k, v in self.recency_count.items()
                                    if k in min_freq_keys
                                    }
                        key_to_pop = min(lru_keys.items(),
                                         key=lambda x: x[1])[0]
                    else:
                        key_to_pop = list(min_freq_keys.keys())[0]
                    self.cache_data.pop(key_to_pop)
                    self.frequency_count.pop(key_to_pop)
                    self.recency_count.pop(key_to_pop)
                    print('DISCARD: {}'.format(key_to_pop))
                self.frequency_count[key] = 0
            self.recency += 1
            self.recency_count[key] = self.recency
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
        self.recency += 1
        self.recency_count[key] = self.recency
        return self.cache_data[key]
