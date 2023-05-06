class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    if head is None:
        return
    node = head
    while node is not None:
        print(node.data, "-> ", end='')
        node = node.next

def push(head, data):
    if head is None:
        return Node(data)
    else:
        new_head = Node(data)
        new_head.next = head
        return new_head


def build_one_two_three():
    pass


chained = None
chained = push(chained, 3)
chained = push(chained, 5)
chained = push(chained, 7)

print_list(chained)
