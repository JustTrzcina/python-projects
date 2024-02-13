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

class Stack:
    '''
        Implements stack datastructure in which LIFO handling of
        items is used

        Attributes:
            first: Reference to the first node in the stack
            last: Reference to the last node in the stack
            size: Representation of the size of the stack
    '''
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self,value):
        """Puts a value on top of the stack

        Args:
            value (any): Value to be pushed onto the stack

        Returns:
            int: New size of the stack
        """
        new_node = Node(value)
        if self.size ==0:
            self.first = new_node
            self.last = new_node
        else:
            temp = self.first
            self.first = new_node
            self.first.next = temp
        self.size+=1
        return self.size

    def pop(self):
        """Removes the last item from the stack

        Returns:
            any or None: Value held in the removed item, or None if the stack is empty.
        """
        if self.size == 0:
            return None
        temp = self.first
        if self.size == 1:
            self.last = None
        self.first = self.first.next
        self.size-=1
        return temp.val


class Queue:
    '''
        Implements queue datastructure in which FIFO handling of
        items is used.

        Attributes:
            first: Reference to the first node in the stack
            last: Reference to the last node in the stack
            size: Representation of the size of the stack
    '''
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self,value):
        """Adds a value at the end of the queue

        Args:
            value (any): Value to be added to the queue

        Returns:
            int: New size of the queue
        """        
        new_node = Node(value)
        if self.size == 0:
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size +=1
        return self.size

    def dequeue(self):
        """Removes the first item from the queue

        Returns:
            any: Value of the removed item
        """        
        if self.size == 0:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.size-=1
        return temp.val
