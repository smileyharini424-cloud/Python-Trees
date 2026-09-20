class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Create Binary Tree
root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)


print("Inorder:", end=" ")
inorder(root)

print()

print("Preorder:", end=" ")
preorder(root)

print()

print("Postorder:", end=" ")
postorder(root)
