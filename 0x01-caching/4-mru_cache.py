#!/usr/bin/env python3
""" MRU caching """


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put an item to the cache """

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                val = self.keys.pop()
                del self.cache_data[val]
                print("DISCARD: {}".format(val))
            if key in self.keys:
                self.keys.remove(key)
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
