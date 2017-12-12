# Author:
# Dilpreet Singh Chawla
# Indian Institute of Information Technology

# Implementation of Stack ADT

# When end of list will hold top element 
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):           # Time Complexity - O(1) 
        self.items.append(item)

    def pop(self):                     # Time Complexity - O(1)
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


# When beginning of list will hold top element

##class Stack:
##    def __init__(self):
##        self.items=[]
##
##    def is_empty(self):
##        return self.items == []
##
##    def push(self, item):             # Time Complexity - O(n)
##        self.items.insert(0, item)
##
##    def pop(self):                       # Time Complexity - O(n)
##        return self.items.pop(0)
##
##    def peek(self):
##        return self.items[0]
##
##    def size(self):
##        return len(self.items)
##    

















     
