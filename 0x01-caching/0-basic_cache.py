#!/usr/bin/env python3
""" Basic dictionary """


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache class """

    def __init__(self):
        """ constructor """
        super().__init__()

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
