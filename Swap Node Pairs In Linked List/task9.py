from preloaded import Node
def swap_pairs(head):
    if head is None or head.next is None:
        return head
    probe = head.next.next
    new_head = head.next
    head.next.next = head
    head.next = swap_pairs(probe)
    return new_head
