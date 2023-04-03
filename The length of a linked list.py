class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def count_nodes(self):
        num = 1
        current_node = self
        while current_node.next is not None:
            num += 1
            current_node = current_node.next

        return num


head = Node(5)
nodeB = Node(7)
nodeC = Node(9)
nodeD = Node(11)

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD

print(head.count_nodes())
