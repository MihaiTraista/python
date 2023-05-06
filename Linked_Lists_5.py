#   codewars katas

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def print_list(head):
    if head is None:
        return
    node = head
    while node is not None:
        print(node.data, "-> ", end='')
        node = node.next
    print("")


def push(head, data):
    if head is None:
        return Node(data)
    else:
        new_head = Node(data)
        new_head.next = head
        return new_head


def build_one_two_three():
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head


def length(node):
    n = 0
    current_node = node
    while current_node is not None:
        n += 1
        current_node = current_node.next
    return n


def count(node, data):
    n = 0
    current_node = node
    while current_node is not None:
        n += current_node.data == data
        current_node = current_node.next
    return n


def move_node(source, dest):
    second_node = source.next
    new_dest = source
    new_source = second_node
    new_dest.next = dest
    return Context(new_source, new_dest)


def merge_sort(list):
    sorted_list = list



    return sorted_list

source = None
source = push(source, 5)
source = push(source, 7)
source = push(source, 3)

print_list(source)

dest = build_one_two_three()
print_list(dest)


print_list(move_node(source, dest).source)
print_list(move_node(source, dest).dest)
