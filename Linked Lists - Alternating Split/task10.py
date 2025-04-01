class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if head is None or head.next is None:
        raise ValueError

    first_head = head
    second_head = head.next

    first_probe = first_head
    second_probe = second_head
    while first_probe is not None and second_probe is not None:
        first_probe.next = second_probe.next
        first_probe = first_probe.next
        
        if first_probe is not None:
            second_probe.next = first_probe.next
            second_probe = second_probe.next
    return Context(first_head, second_head)
