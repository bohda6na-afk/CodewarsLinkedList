class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    first = head
    second = head.next
    a = first
    b = second
    while b and b.next:
        a.next = b.next
        a = a.next
        b.next = a.next
        b = b.next
    a.next = None
    return Context(first, second)
