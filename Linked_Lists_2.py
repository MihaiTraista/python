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

    def rearrange(self):
        fast = self.head
        slow = self.head
        while fast.next.next:
            fast = fast.next.next
            slow = slow.next
            # print(f"fast {fast.data}, fast.next {fast.next.data}, slow {slow.data}")

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
            # print(f"first_half_next {first_half_next.data}, second_half_next {second_half_next.data}")


my_list = LinkedList()

my_list.append('a1')
my_list.append('a2')
my_list.append('a3')
my_list.append('a4')
my_list.append('b1')
my_list.append('b2')
my_list.append('b3')
my_list.append('b4')

my_list.print_list()
my_list.rearrange()
my_list.print_list()
