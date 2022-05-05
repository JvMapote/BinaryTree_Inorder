#In order travesal
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(6)
root.left.right.left = Node(5)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

inorder(root)

