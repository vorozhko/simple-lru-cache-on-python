# Simple LRU cache on Python 3

## Data structure

The data structure must fit following operations:

* FIFO queue is responsible to evict least used items. 
* Hash table is responsible to get cached items and update cached items. 

Using Python collections.OrderedDict allow to perform both operations in O(1) time complexity.

## Algorithm

collections.OrderedDict combine both capabilities: 

* Queue: dict items are ordered as FIFO queue, so insert and eviction are done in O(1) 
* Hash table: dict keys provide access to data in O(1) time

See implementation in [lru.py](lru.py)

