#!/usr/bin/env python3
""" LRU caching """
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    val, _ = self.cache_data.popitem(True)
                    print("DISCARD: {}".format(val))
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
