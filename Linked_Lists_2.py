# given a linked list a1 -> a2 -> ... -> an -> b1 -> b2 -> ... -> bn
# rearrange it into a1 -> b1 -> a2 -> b2 -> ... -> an -> bn

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def interleave(self):
        if self.head is None or self.head.next is None:
            return
        fast = self.head
        slow = self.head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        first_half = self.head
        slow.next = None

        while second_half:
            first_half_next = first_half.next
            second_half_next = second_half.next
            first_half.next = second_half
            second_half.next = first_half_next
            first_half = first_half_next
            second_half = second_half_next


my_list = LinkedList()

values = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
for value in values:
    my_list.append(value)

print("Original List")
my_list.print_list()
my_list.interleave()
print("Interleaved List")
my_list.print_list()
