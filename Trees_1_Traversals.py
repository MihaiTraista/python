class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    #   depth first search
    #   Root -> Left ->Right
    def pre_order_print(self, start):
        if start:
            print(start.value, end='-')
            self.pre_order_print(start.left)
            self.pre_order_print(start.right)

    #   Left -> Root -> Right
    def in_order_print(self, start):
        if start:
            self.pre_order_print(start.left)
            print(start.value, end='-')
            self.pre_order_print(start.right)

    #   Left -> Right -> Root
    def post_order_print(self, start):
        if start:
            self.pre_order_print(start.left)
            self.pre_order_print(start.right)
            print(start.value, end='-')


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("pre_order_print")
tree.pre_order_print(tree.root)
print()
print("in_order_print")
tree.in_order_print(tree.root)
print()
print("post_order_print")
tree.post_order_print(tree.root)
print()

