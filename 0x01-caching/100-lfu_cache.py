#!/usr/bin/env python3
""" LFU caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """

    def __init__(self):
        """ constructor """
        super().__init__()
        self.keys = []
        self.freq = {}

    def put(self, key, item):
        """ put an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.keys.remove(key)
                self.freq[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_keys = [k for k in self.keys if self.freq[k]
                                == min(self.freq.values())]
                    lru_key = lfu_keys[0]
                    for k in lfu_keys:
                        if k in self.keys:
                            lru_key = k
                            break
                    del self.cache_data[lru_key]
                    del self.freq[lru_key]
                    self.keys.remove(lru_key)
                    print("DISCARD: {}".format(lru_key))

                self.cache_data[key] = item
                self.freq[key] = 1
                self.keys.append(key)

    def get(self, key):
        """ get data from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        return self.cache_data[key]
