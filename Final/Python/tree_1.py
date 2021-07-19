"""
Create a recursive function that inserts a value into the correct node of a tree. 
This should be very similar to the _contains function found in the Software Example,
but when an empty node is found where the number should go you should add the number 
to the tree.
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
        pass

tree = SearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)  
tree.insert(4)
tree.insert(8)
tree.insert(2)
tree.insert(6)
for x in tree:
    print(x)  # 2, 3, 4, 5, 6, 7, 8

#Original code based on work from Brother Macbeth.
#He did not invent the insert concept.
#Probably.