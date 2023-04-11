class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Data: {self.data or None}"


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


my_list = LinkedList()
my_list.append(9)
my_list.append(7)
my_list.append(5)
my_list.append(3)

my_list.print_list()
