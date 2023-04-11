#   Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#   Do not modify the linked list.
#   https://leetcode.com/problems/linked-list-cycle-ii/

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

    def peek(self, peek_value):
        current_node = self.head
        while current_node:
            if current_node.data == peek_value:
                return current_node
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        n = 0
        while current_node and n < 20:
            print(current_node.data, end=', ')
            current_node = current_node.next
            n += 1
        print()


def get_cycle_v1(head):
    visited_nodes = []
    node = head
    while node.next:
        if node.next in visited_nodes:
            return node.next
        visited_nodes.append(node)
        node = node.next
    return None


def get_cycle_v2(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head

    # increment both pointers at the same pace until they meet again
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


my_list = LinkedList()

values = [3, 2, 0, -4]
for value in values:
    my_list.append(value)

my_list.peek(-4).next = my_list.peek(2)
print("loop", my_list.peek(-4))

my_list.print_list()
print(f"get_cycle_v1 {get_cycle_v1(my_list.head)}")
print(f"get_cycle_v2 {get_cycle_v2(my_list.head)}")

