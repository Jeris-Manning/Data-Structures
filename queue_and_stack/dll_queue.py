import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, node=None):
        self.size = 0
        self.storage = DoublyLinkedList(self)
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        self.value = value




    def dequeue(self):
        if self.size < 1:
            return None
        else:
            self.size -= 1
            self.storage.remove_from_head()
            return

    def len(self):
        return self.size
