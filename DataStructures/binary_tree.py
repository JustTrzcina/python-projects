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
    
    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self,current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def find(self,value:int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f'Node with value {value} not found.')

    def find_parent(self,value:int)->Node:
        if self.head and self.head.value == value:
            return self.head
        
        current_node = self.head
        while current_node:
            if current_node.left and current_node.left.value == value or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value>current_node.value:
                current_node = current_node.right
            elif current_node<current_node.value:
                current_node = current_node.left
    
    def find_rightmost(self,node:Node)->Node:
        current_node = node
        while current_node.left:
            current_node = current_node.right
        return current_node
    
    def delete(self,value:int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            pass
        if to_delete.left or to_delete.right:
            pass
        else:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left=None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None





new_tree = BinaryTree(Node(33))
new_tree.add(Node(3))
new_tree.add(Node(78))
    
new_tree.inorder()
print(new_tree.find(3))