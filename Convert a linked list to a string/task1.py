class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    res = []
    while node:
        res.append(str(node.data))
        node = node.next
    res.append("None")
    return " -> ".join(res)

# print(stringify(Node(0, Node(1, Node(2, Node(3))))))