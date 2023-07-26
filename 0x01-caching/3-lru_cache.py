#!/usr/bin/env python3
"""
class LRUCache, cahching system which thrashes out item from the
cache_data dict depend on least item recently used algorithm
"""
from base_caching import BaseCaching
import datetime


class LRUCache(BaseCaching):
    """
    implementing class LRUCache
    """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.queue_time = {}

    def put(self, key, item):
        """ assigns item value to cache_data dict"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.queue_time[key] = datetime.datetime.now()

        if len(self.cache_data) > self.MAX_ITEMS:
            lru = datetime.datetime.now()
            leastkey = None
            for key, value in self.queue_time.items():
                if value < lru:
                    lru = value
                    leastkey = key
            del self.queue_time[leastkey]
            del self.cache_data[leastkey]
            print(f'DISCARD: {leastkey}')

    def get(self, key):
        """ return retrived data from cache_data dict """
        if key in self.cache_data:
            self.queue_time[key] = datetime.datetime.now()
        return self.cache_data.get(key)
