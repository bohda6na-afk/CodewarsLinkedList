class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    # your code goes here.
    def recursive(curr, prev):
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        return recursive(next_node, curr)
    return recursive(head, None)