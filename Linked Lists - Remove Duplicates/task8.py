class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    # Your code goes here.
    # Remember to return the head of the list.
    if head is None or head.next is None:
        return head
    probe = head
    while probe.next is not None:
        if probe.data == probe.next.data:
            probe.next = probe.next.next
        else:
            probe = probe.next
    return head
