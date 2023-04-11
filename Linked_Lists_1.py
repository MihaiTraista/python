# the runner technique for linked lists from the book Cracking the Coding Interview

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
            print(current_node.data, end=', ')
            current_node = current_node.next
        print()

    def get_length(self):
        #   O(n)
        current_node = self.head
        n = 0
        while current_node:
            n += 1
            current_node = current_node.next
        return n

    def get_middle_node_my_implementation(self):
        #   O(n + n/2) = O(n)
        middle_index = int(self.get_length() / 2)
        current_node = self.head
        stopper = 0
        while current_node and stopper < middle_index - 1:
            current_node = current_node.next
            stopper += 1
        return current_node.data

    def get_middle_node_runner_technique(self):
        #   O(n)
        fast_runner = self.head
        slow_runner = self.head
        while fast_runner and fast_runner.next:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
        return slow_runner.data


my_list = LinkedList()
my_list.append(9)
my_list.append(7)
my_list.append(5)
my_list.append(3)

my_list.print_list()
print(f"length {my_list.get_length()}")
print(f"get_middle_node_my_implementation {my_list.get_middle_node_my_implementation()}")
print(f"get_middle_node_runner_technique {my_list.get_middle_node_runner_technique()}")
