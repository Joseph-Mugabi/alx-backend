#!/usr/bin/env python3
"""
implementing basic cache class that inherits from parent BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    representing the class BaseCaching
    """
    def put(self, key, item):
        #  check if key or item are not none,
        #  and proceed to assign the item value to the key in cache_data dict
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        # check if key is None or if the key doesn't exist 
        # in the cache_data dict
        if key is None or key not in self.cache_data:
            return None

        #  return value associated with the key in the cache_data dict
        return self.cache_data[key]
