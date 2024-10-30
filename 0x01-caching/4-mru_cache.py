#!/usr/bin/env python3
""" MRU caching """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    val, _ = self.cache_data.popitem(last=True)
                    print("DISCARD: {}".format(val))
            else:
                self.cache_data.move_to_end(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
