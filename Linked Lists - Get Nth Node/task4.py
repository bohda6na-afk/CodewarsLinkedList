from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError
    count = 0
    probe = node
    while probe is not None:
        if count == index:
            return probe
        probe = probe.next
        count += 1
    raise ValueError
