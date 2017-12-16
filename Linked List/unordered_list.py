from node import Node

# Implementation of Unordered Linked List
class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self): # For printing list 
        current = self.head
        s=''
        while current != None:
            s+=str(current) + ' '
            current = current.get_next()
        return s

    def is_empty(self):  # To check if the list is empty
        return self.head == None

    def add(self, item): # To add a new node to list
        temp = Node(item)
        # Insert at beginning
        temp.set_next(self.head) 
        self.head = temp

    def size(self): # To get length of list
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item): # To search an item in list
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item): # Removing item from list
        current = self.head
        previous = None
        found = False
        while not found: # Assuming value is present in the list
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None: # If first item is to be removed
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


my_list=UnorderedList()
my_list.add(1)
my_list.add(2)
print(my_list)
print(my_list.size())
print(my_list.search(2))
