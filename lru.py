"""Simple LRUCache implementation."""

import collections
import os
import random
from math import factorial

CACHE_SIZE = 100
if os.getenv('CACHE_SIZE'):
    CACHE_SIZE = int(os.getenv('CACHE_SIZE'))

SAMPLE_SIZE = 100
if os.getenv('SAMPLE_SIZE'):
    SAMPLE_SIZE = int(os.getenv('SAMPLE_SIZE'))

LRUCache = collections.OrderedDict()


def expensive_call(number):
    """Calculate factorial. Example of expensive call."""
    return factorial(number)


if __name__ == '__main__':

    test_cases = random.choices(
        [x for x in range(SAMPLE_SIZE*3)],
        [x for x in range(SAMPLE_SIZE*3)],
        k=SAMPLE_SIZE
    )

    for test in test_cases:
        if test in LRUCache:
            print("hit:", test, LRUCache[test])
            # Update position of the hit item to first. Optional.
            LRUCache.move_to_end(test, last=True)
        else:
            LRUCache[test] = expensive_call(test)
            print("miss:", test, LRUCache[test])
        if len(LRUCache) > CACHE_SIZE:
            evict_key, evict_val = LRUCache.popitem(last=False)
            print("evict:", evict_key, evict_val)
