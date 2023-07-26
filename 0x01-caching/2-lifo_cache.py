#!/usr/bin/python3
"""
class LIFOCache cach3ing system which thrashes out least
item in first to be out of the cache_data dict
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    implementing class LIFOCache
    """
    def __init__(self):
        """
        initializing
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        assigns item value in the cache_data dict
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.stack:
                self.stack.remove(key)
            self.stack.append(key)

        if len(self.stack) > self.MAX_ITEMS:
            new_keys = self.stack.pop(-2)
            del self.cache_data[new_keys]
            print(f'DISCARD: {new_keys}')

    def get(self, key):
        """
        returns value in the cache_data dict
        """
        return self.cache_data.get(key)
