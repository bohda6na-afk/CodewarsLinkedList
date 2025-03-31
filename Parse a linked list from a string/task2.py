class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s.strip() == "None":
        return None
    parts = s.split(" -> ")
    if parts[-1] == "None":
        parts.pop()
    if not parts:
        return None
    head = Node(int(parts[0]))
    current = head
    for part in parts[1:]:
        node = Node(int(part))
        current.next = node
        current = node
    return head
