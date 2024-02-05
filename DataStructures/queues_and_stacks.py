class Queue:
    def __init__(self):
        self.itmes=[]

    def push(self,e):
        self.items = self.itmes.append(e)

    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head
    
class Stack:
    def __init__(self):
        self.items=[]

    def push(self,e):
        self.items = [e] + self.items

    def pop(self):
        return self.items.pop()