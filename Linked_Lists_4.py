#   Palindrome Linked List - Leetcode 234 - Python
#   Write a function that receives a linked list and returns true if the list is a palindrome

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
        #   O(n)
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


def peek(linked_list, b):
    #   O(n)
    runner = linked_list.head
    while runner is not None:
        if runner.next is b:
            return runner
        runner = runner.next


def is_palindrome(linked_list):
    #   O(n / 2) * O(n) = O(n^2)
    if linked_list.get_length_recursive(linked_list.head) % 2 != 0:     # O(n)
        return False
    is_pali = True
    a = linked_list.head
    b = peek(linked_list, None)     # O(n)
    while a.next is not b:          # O(n/2)
        if a.data != b.data:
            is_pali = False
            break
        a = a.next
        b = peek(linked_list, b)    # O(n)

    return is_pali


my_list = LinkedList()

values = [1, 2, 2, 1]
for value in values:
    my_list.append(value)

my_list.print_list()

print(f"get_length_recursive {my_list.get_length_recursive(my_list.head)}")
print(f"isPalindrome {is_palindrome(my_list)}")
