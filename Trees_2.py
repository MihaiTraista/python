#   Your task is to return the list with elements from tree sorted by levels, which means the root element goes first,
#   then root children (from left to right) are second and third, and so on.

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def get_array(root):
    arr = []
    node = root

    while node is not None:
        pass

root = Node(2)
level_1a = Node(8)
level_1b = Node(9)
level_2a = Node(1)
level_2b = Node(3)
level_2c = Node(4)
level_2d = Node(5)

root.left = level_1a
root.right = level_1b
level_1a.left = level_2a
level_1a.right = level_2b
level_1b.left = level_2c
level_1b.right = level_2d

print(get_array(root))
