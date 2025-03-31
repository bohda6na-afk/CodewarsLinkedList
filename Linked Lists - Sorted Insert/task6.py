""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    # Your code goes here.
    # Make sure to return the head of the list.
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node
    probe = head
    while probe.next is not None and probe.next.data < data:
        probe = probe.next
    new_node.next = probe.next
    probe.next = new_node
    return head