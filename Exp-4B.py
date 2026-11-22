class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create():
    x = int(input("Enter book ID (-1 for no book): "))

    if x == -1:
        return None

    root = Node(x)

    print(f"Enter left of book {x}")
    root.left = create()

    print(f"Enter right of book {x}")
    root.right = create()

    return root


def preorder(temp):
    if temp is not None:
        print(temp.data, end=" ")
        preorder(temp.left)
        preorder(temp.right)


def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)


def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")


root = create()

print("\nPreorder Traversal:")
preorder(root)

print("\n\nInorder Traversal:")
inorder(root)

print("\n\nPostorder Traversal:")
postorder(root)