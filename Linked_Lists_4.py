#   Palindrome Linked List - Leetcode 234 - Python
#   https://www.youtube.com/watch?v=yOzXms1J6Nk

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}, next {self.next.data if self.next else None}"


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

    def get_length_iterative(self):
        #   O(n)
        current_node = self.head
        n = 0
        while current_node:
            n += 1
            current_node = current_node.next
        return n

    def get_length_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.get_length_recursive(node.next)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=', ')
            current_node = current_node.next
        print()


def is_palindrome(list):
    pass


my_list = LinkedList()

values = [1, 2, 2, 1]
for value in values:
    my_list.append(value)

my_list.print_list()
print(f"isPalindrome {is_palindrome(my_list)}")
print(f"len {my_list.get_length_recursive(my_list.head)}")
