# Linked List

A **Linked List** is a dynamic data structure that consists of a series of nodes that are not stored in continguous locations; instead, each node is connected via a pointer.

A **Singly Linked List** is a linked list with nodes that consists of two elements: data and a pointer to next node.

A **Doubly Linked List** is a linked list with nodes that consists of three elements: data and pointers to next and previous node.

Unlike an Array, a linked list does not provide constant time access to a particular "index", if you want to find the Kth element in the list, you need to iterate through till the Kth element.

The benefit of a linked list is that you can add and remove items from the beginning of the list in constant time.

Creating a linked list in python:
```
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self, ):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data

    def get_next(self, ):
        return self.next

    def set_next(self, new_next_node):
        self.next = new_next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.head

    def unshift(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
    def shift(self):
        re_node = self.head
        self.head = re_node.next()
        return re_node
    
    def insert(self, data):
        """simplified to insert at end only"""
        new_node = Node(data)
        self.tail.set_next(new_node)
        self.tail = new_node

    def pop(self):
        pass
    
    def delete(self, data):
        """delete node based on first instance of data"""
        pass

    def delete_by_index(self, k):
        """delete node on kth index"""
        pass

    def get(self, data):
        """get node on first instance of data"""
        pass

    def get_by_index(self, k):
        """get node from kth index"""
        pass
    ...
```

