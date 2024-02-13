
from typing import List

class MaxBinaryHeap():
    """
    A class representing a max binary heap data structure

    Attributes:
        values (List[int]): A list to store the values of the heap
    """
    def __init__(self) -> None:
        self.values = [57, 23, 89, 42, 68, 35, 77, 10, 50]

    def insert(self,element):
        """ 
        Inserts a new element into the heap.

        Args:
            element : The element to be inserted into the heap.
        """
        self.values.append(element)
        self.bubble_up(element)

    def bubble_up(self,element):
        """ 
        Moves the newly inserted element up the heap to maintain the heap property.

        Args:
            element: The element to be moved up the heap.
        """
        idx = len(self.values)-1
        while idx > 0:
            parent_index = (idx-1)//2
            parent = self.values[parent_index]
            if element <= parent:
                break
            self.values[parent_index] = element
            self.values[idx] = parent
            idx = parent_index

    def extract_max(self):
        """ 
        Extracts the maximum value from the heap.

        Returns:
            The maximum value from the heap.
        """
        max_val = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()

        return max_val

    def sink_down(self):
        """ 
        Moves the top element down the heap to maintain the heap 
        property after extraction.
        """
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = 2*idx+1
            right_child_idx = 2*idx+2
            swap = None

            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child > element:
                    swap = left_child_idx

            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((swap is None and right_child > element)
                    or (swap is not None and right_child>left_child)):
                    swap = right_child_idx

            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

heap = MaxBinaryHeap()
heap.insert(94)
print(heap.values)
heap.extract_max()
print(heap.values)

class Node():
    def __init__(self,value,priority) -> None:
        self.value = value
        self.priority = priority

    def __repr__(self) -> str:
        return f'<Node priority:{self.priority}, {self.value}>'

class PriorityQueue():
    """
    A class representing a min priority queue data structure

    Attributes:
        values (List[int]): A list to store the values of the heap
    """
    def __init__(self) -> None:
        self.values:List[Node] = []

    def enqueue(self,element,priority):
        """ 
        Inserts a new element into the heap.

        Args:
            element : The element to be inserted into the heap.
        """
        new_node = Node(element,priority)
        self.values.append(new_node)
        self.bubble_up(new_node)

    def bubble_up(self,element:Node):
        """ 
        Moves the newly inserted element up the heap to maintain the heap property.

        Args:
            element: The element to be moved up the heap.
        """
        idx = len(self.values)-1
        while idx > 0:
            parent_index = (idx-1)//2
            parent = self.values[parent_index]
            if element.priority >= parent.priority:
                break
            self.values[parent_index] = element
            self.values[idx] = parent
            idx = parent_index

    def dequeue(self):
        """ 
        Extracts the minimum value from the heap.

        Returns:
            The minimum value from the heap.
        """
        min_val = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()

        return min_val

    def sink_down(self):
        """ 
        Moves the top element down the heap to maintain the heap 
        property after extraction.
        """
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_idx = 2*idx+1
            right_child_idx = 2*idx+2
            swap = None

            if left_child_idx < length:
                left_child = self.values[left_child_idx]
                if left_child.priority < element.priority:
                    swap = left_child_idx

            if right_child_idx < length:
                right_child = self.values[right_child_idx]
                if ((swap is None and right_child.priority < element.priority)
                    or (swap is not None and right_child.priority < left_child.priority)):
                    swap = right_child_idx

            if swap is None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap

coffe_shop = PriorityQueue()
coffe_shop.enqueue('espresso',3)
coffe_shop.enqueue('latte',2)
coffe_shop.enqueue('latte',2)
coffe_shop.enqueue('tea',1)
print(coffe_shop.values)
print(coffe_shop.dequeue())
