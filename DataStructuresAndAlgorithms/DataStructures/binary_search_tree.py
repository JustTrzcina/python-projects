from typing import List

class Node:
    '''
    Class representing a node in binary tree.

    Attributes:
        value: The value stored in the node.
        left: Reference to the left child node of the parent node.
        right: Reference to the right child node of the parent node.
    '''
    def __init__(self,value:int) -> None:
        self.value = value
        self.left:Node = None
        self.right:Node = None

    def __repr__(self) -> str:
        return f'<Node {self.value}>'

class BinarySearchTree():
    """Representation of binary search tree

    Atributes
        root (Node): Parent node of all the nodes
    """
    def __init__(self) -> None:
        self.root:Node = None

    def insert(self,value:int):
        """Performs insertion of given value into the BST

        Args:
            value (int): Value added into the tree

        Returns:
            BST or None: Returns BST or None if inserted value was already
            found in the tree.
        """        
        new_node=Node(value)
        if not self.root:
            self.root = new_node
            return self
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left= new_node
                    return self
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return self
                current = current.right
            else:
                return None

    def find(self,value:int):
        """Performs search function on the BST

        Args:
            value (int): Value to be searched for

        Returns:
            Node or None: Returns Node with the specified value or
            None if no value was found
        """        
        if self.root is None:
            return False
        current = self.root
        found = False
        while current and not found:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                found = True
        if not found:
            return None
        return current

    def bfs(self):
        """Implements breadth first search where each of the BST layers
        are traversed before going to the next layer.

        Returns:
            List[Node]: Returns a list of nodes with bfs order.
        """        
        data:List[Node] = []
        queue:List[Node] = []
        tree_node = self.root
        queue.append(tree_node)
        while len(queue)!=0:
            tree_node = queue.pop(0)
            data.append(tree_node)
            if tree_node.left:
                queue.append(tree_node.left)
            if tree_node.right:
                queue.append(tree_node.right)
        return data

    def dfs_preoder(self):
        """ Performs a depth-first search (DFS) traversal in preorder starting from the root node.
        Preorder traversal visits the current node before its child nodes.

        Returns:
            List[Node]: List of nodes in the dfs preorder
        """        
        data:List[Node] = []
        current = self.root
        def traverse(node:Node):
            data.append(node)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(current)
        return data

    def dfs_postorder(self):
        """Perform depth-first search (DFS) traversal of the binary tree in postorder fashion.

        Returns:
            List[Node]: A list containing the nodes of the tree visited in postorder.
        """
        data:List[Node] = []
        current = self.root
        def traverse(node:Node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            data.append(node)

        traverse(current)
        return data

    def dfs_inorder(self):
        """Perform depth-first search (DFS) traversal of the binary tree in postorder fashion.

        Returns:
            List[Node]: A list containing the nodes of the tree visited in postorder.
        """
        data:List[Node] = []
        current = self.root
        def traverse(node:Node):
            if node.left:
                traverse(node.left)
            data.append(node)
            if node.right:
                traverse(node.right)


        traverse(current)
        return data



bst = BinarySearchTree()
bst.insert(10)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(20)
print(bst.dfs_preoder())
print(bst.dfs_postorder())
print(bst.dfs_inorder())
