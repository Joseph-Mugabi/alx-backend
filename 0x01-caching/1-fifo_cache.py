#!/usr/bbin/env python3
"""
class FIFOCache system which thrash out first in first out items
 in the cache_data dict
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    implements fifo cache
    """
    def __init__(self):
        """ initialise """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        assigns items value in the cache_data dict
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.queue:
                self.queue.append(key)

        if len(self.queue) > self.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        return values in the cache_data dict
        """
        return self.cache_data.get(key)
