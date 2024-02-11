class Queue:
    '''
        Implements queue datastructure
    '''
    def __init__(self):
        self.items=[]

    def push(self,val):
        self.items = self.items.append(val)

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head

class Stack:
    '''
        Implements stack datastructure
    '''
    def __init__(self):
        self.items=[]

    def push(self,e):
        self.items = [e] + self.items

    def pop(self):
        return self.items.pop()
