class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'<Node {self.value}>'
    
class BinaryTree:
    def __init__(self,head:Node) -> None:
        self.head = head

    def add(self,new_node:Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('Node with specified value already exists')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
    

new_tree = BinaryTree(Node(33))
new_tree.add(Node(3))
new_tree.add(Node(78))
    