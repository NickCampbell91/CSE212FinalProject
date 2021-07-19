"""
Based on your work from the previous problem, create a function to remove a node
from a tree.
"""

class SearchTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = SearchTree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = SearchTree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = SearchTree.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    def remove(self, data):
        if self.root is None:
            self.root = SearchTree.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _remove(self, data, node):
        pass


tree = SearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

tree.remove(1)
for x in tree:
    print(x)  # 3, 4, 5, 6, 7, 10