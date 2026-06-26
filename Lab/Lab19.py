# AVL Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

# Get height
def height(node):
    if node is None:
        return 0
    return node.height

# Get balance factor
def balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

# Right Rotation
def rightRotate(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x

# Left Rotation
def leftRotate(x):
    y = x.right
    t = y.left

    y.left = x
    x.right = t

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

# Insert Node
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))

    b = balance(root)

    # Left Left Case
    if b > 1 and key < root.left.data:
        return rightRotate(root)

    # Right Right Case
    if b < -1 and key > root.right.data:
        return leftRotate(root)

    return root

# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Create AVL Tree
root = None
values = [30, 20, 40, 10, 25]

for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)
