#!/usr/bin/env python3
"""
class MRUCache, caching system thrashes out the most recently used
cache from the cache_data dict or set.
"""
from base_caching import BaseCaching
import datetime


class MRUCache(BaseCaching):
    """
    implementing Most Recently Used Cache class
    """
    def __init__(self):
        """ initializing """
        super().__init__()
        self.mru_time = {}

    def put(self, key, item):
        """ assigning item value in a cache_data dict """
        if key is not None and item is not None:
            self.cache_data[key] = item
            mru = self.mru_time[key] = datetime.datetime.now()
            recentkey = key

        if len(self.cache_data) > self.MAX_ITEMS:
            minimum_time = datetime.datetime(year=1, month=1, day=1)
            dif = mru - minimum_time
            next_recent = None
            for key, value in self.mru_time.items():
                if key == recentkey:
                    continue
                if (mru - value) < dif:
                    dif = mru - value
                    next_recent = key
            del self.mru_time[next_recent]
            del self.cache_data[next_recent]
            print(f'DISCARD: {next_recent}')

    def get(self, key):
        """ returns retrived date from cache_data dict """
        if key in self.cache_data:
            self.mru_time[key] = datetime.datetime.now()
        return self.cache_data.get(key)
