'''This module implements doubly linked list as a part of data structures course exercises'''

class Node():
    '''
    Class representing a node in a linked list.

    Attributes:
        val: The value stored in the node.
        next: Reference to the next node in the linked list.
    '''
    def __init__(self,val) -> None:
        self.val = val
        self.next:Node = None
        self.previous:Node = None

class DoublyLinkedList():
    '''
    A class representing a doubly linked list.

    Attributes:
        head (Node): The head (first element) of the linked list.
        tail (Node): The tail (last element) of the linked list.
        length (int): The number of elements in the linked list.

    '''
    def __init__(self) -> None:
        self.head:Node = None
        self.tail:Node = None
        self.length:int = 0

    def push(self,value):
        """
        Adds a new node with the given value to the end of the linked list.

        Args:
            value: The value to be added to the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
    def pop(self):
        """
        Removes and returns the last node of the linked list.

        Returns:
            The last node of the linked list.
        """
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.tail=None
            self.head=None
        else:
            self.tail = popped_node.previous
            self.tail.next = None
            popped_node.previous = None
        self.length -=1
        return popped_node

    def shift(self)->Node:
        """
        Removes and returns the first node of the linked list.

        Returns:
            The first node of the linked list.
        """
        if self.length == 0:
            return None
        shifted_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous=None
            shifted_node.next=None
        self.length-=1
        return shifted_node

    def unshift(self,value):
        """
        Adds a new node with the given value to the beginning of the linked list.

        Args:
            value: The value to be added to the linked list.
        """
        new_node = Node(value)
        if self.length==0:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return self

    def get(self,index:int)->Node:
        """
        Returns the node at the specified index.

        Args:
            index: The index of the node to be retrieved.

        Returns:
            The node at the specified index.
        """
        if index <= 0 or index > self.length:
            return None
        if index <= self.length//2:
            counter = 0
            current = self.head
            while counter != index:
                current = current.next
                counter+=1
        else:
            counter = self.length-1
            current = self.tail
            while counter!=index:
                current = current.previous
                counter-=1
        return current

    def set_val(self,index:int,value)->bool:
        """
        Sets the value of the node at the specified index.

        Args:
            index: The index of the node to set the value for.
            value: The new value to be set.
        
        Returns:
            bool: True if the operation was successful, False otherwise.
        """
        node = self.get(index)
        if node is not None:
            node.val = value
            return True
        return False

    def insert(self,index:int,value):
        """
        Inserts a new node with the given value at the specified index.

        Args:
            index: The index at which to insert the new node.
            value: The value to be added to the linked list.
        
        Returns:
            bool: True if the operation was successful, False otherwise.
        """

        if index < 0 or index > self.length:
            return False
        if index == 0 :
            self.unshift(value)
            return True
        if index == self.length:
            self.push(value)
            return True

        prev_node = self.get(index-1)
        new_node = Node(value)
        after_node = prev_node.next

        prev_node.next = new_node
        new_node.previous = prev_node

        new_node.next = after_node
        after_node.previous = new_node
        self.length+=1
        return True

    def remove(self,index:int):
        """
        Removes and returns the node at the specified index.

        Args:
            index: The index of the node to be removed.
        
        Returns:
            The node at the specified index.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0 :
            return self.shift()
        if index == self.length-1:
            return self.pop()
        removed_node = self.get(index)

        previous_node = removed_node.previous
        next_node = removed_node.next

        previous_node.next = removed_node.next
        next_node.previous = removed_node.previous

        removed_node.previous = None
        removed_node.next = None
        self.length-=1
        return removed_node
        

doubly_list = DoublyLinkedList()

doubly_list.push(3)
print(doubly_list.head.val,doubly_list.tail.val, doubly_list.length,)
doubly_list.push(7)
print(doubly_list.head.next.val,doubly_list.tail.previous.val, doubly_list.length)
doubly_list.push(9)
print(doubly_list.head.next.next.val,doubly_list.tail.previous.val, doubly_list.length)
print(doubly_list.pop().val)
print(doubly_list.shift().val)
print(doubly_list.head.val,doubly_list.tail.val, doubly_list.length,)
print(doubly_list.unshift(5).head.val)
print(doubly_list.head.val,doubly_list.tail.val, doubly_list.length,)