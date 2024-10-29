#!/usr/bin/env python3
""" FIFO caching """


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
                del self.keys[0]
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
