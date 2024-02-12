'''This module implements singly linked list as a part of data structures course exercises'''

class Node():
    '''
    Class representing a node in a linked list.

    Attributes:
        val: The value stored in the node.
        next: Reference to the next node in the linked list.
    '''
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class SinglyLinkedList():
    '''
    A class representing a singly linked list.

    Attributes:
        head: The head (first element) of the linked list.
        tail: The tail (last element) of the linked list.
        length: The number of elements in the linked list.

    '''
    def __len__(self):
        return self.length

    def __init__(self) -> None:
        self.head:Node = None
        self.tail:Node = None
        self.length = 0

    def push(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail =self.head
        else:
            self.tail.next= new_node
            self.tail = new_node
        self.length+=1
        return self
    
    def pop(self):
        if not self.head:
            return None
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        if self.length == 0:
            self.head = None
            self.tail = None
        return current
    
    def shift(self):
        if not self.head:
            return None
        current = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current
    
    def unshift(self,value):   
        new_node = Node(value)
        if not self.head:
            self.head=new_node
            self.tail=self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return self

    def get(self,index)->Node:
        if index < 0 or index >= self.length:
            return None
        counter=0
        node = self.head
        while counter != index:
            node = node.next
            counter+=1
        return node
    
    def set_val(self,index,value):
        found_node = self.get(index)
        if found_node:
            found_node.val = value
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            self.push(value)
            return True
        if index == 0:
            self.unshift(value)
            return True
        new_node = Node(value)
        prev = self.get(index-1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length+=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length -1:
            return self.pop()
        previous_node = self.get(index-1)
        removed = previous_node.next
        previous_node.next = removed.next

        return removed
    
    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        next_node = None
        prev_node = None
        while node is not None:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        return self
    


new_list = SinglyLinkedList()
new_list.push(3)
new_list.push(15)
new_list.push(83)
new_list.push(123)
new_list.push(56)