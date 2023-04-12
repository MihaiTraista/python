class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    #   Left -> Root -> Right
    def pre_order_print(self, start):
        if start:
            print(start.value)
            self.pre_order_print(start.left)
            self.pre_order_print(start.right)


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# depth first search
tree.pre_order_print(tree.root)
