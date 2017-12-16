from node import Node

# Implementation of Ordered Linked List
class OrderedList:
    def __init__(self):
        self.head = None

    def __str__(self): # For printing list
        current = self.head
        s=''
        while current != None:
            s+=str(current)+' '
            current = current.get_next()
        return s
    
    def is_empty(self):  # To check if the list is empty
        return self.head == None

    def add(self,item):# To add item in ordered list
        current = self.head
        previous = None
        while current != None:
            if current.get_data() > item:
                break
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None: # Adding at beginning
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        
    def size(self): # To get length of list
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self,item): # To search for item in ordered list
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            elif current.get_data() > item:
                break
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

my_list = OrderedList()
my_list.add(1)
my_list.add(4)
my_list.add(3)
print(my_list)
print(my_list.size())
print(my_list.search(5))
print(my_list.search(4))
