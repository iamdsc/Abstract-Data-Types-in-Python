# Author:
# Dilpreet Singh Chawla
# Indian Institute of Information Technology Kalyani

# Implementation of queue ADT
# When the rear is at position 0 of the list and front is at end

class Queue:
    def __init__ (self):
        self.items = []

    def is_empty (self):
        return self.items == []

    def enq (self, item):
        self.items.insert(0,item)

    def dq (self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
