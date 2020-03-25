import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit # Max number of nodes in cache
        self.dll = DoublyLinkedList()
        self.node_count = self.dll.length # Use the length of the dll as node counter
        self.storage_dict = {} # Dictionary for hash table style lookups

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict: # If the key is in the dictionary, move corresponding node to tail return value
           node = self.storage_dict[key]
           self.dll.move_to_end(node)
           return node.value[1]
        else:
            return None # Returns None if no corresponding key in the dictionary

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):

        if key in self.storage_dict: # If the key is already in the dictionary, update with new value and move to tail
            node = self.storage_dict[key]
            node.value = (key, value)
            self.dll.move_to_end(node)
            return

        if self.node_count == self.limit: # If cache is full, remove least used entry from dictionary and dll head
            del self.storage_dict[self.dll.head.value[0]]
            self.dll.remove_from_head()
            self.node_count -= 1

        self.dll.add_to_tail((key, value)) # Add new node to dll tail and dictionary
        self.storage_dict[key] = self.dll.tail
        self.node_count += 1