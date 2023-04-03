class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_sum(node):
    if node is None:
        return 0
    else:
        return node.value + find_sum(node.left) + find_sum(node.right)


root = Node(2)
level_1_r = Node(4)
level_1_l = Node(3)
level_2_r = Node(6)
level_2_l = Node(5)

root.right = level_1_r
root.left = level_1_l
level_1_l.right = level_2_r
level_1_l.left = level_2_l

print("the sum is ", find_sum(root))
