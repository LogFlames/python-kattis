class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.prev = None

s = input()
current = Node()
current.data = 0
current.next = None
current.prev = None

for c in s:
    if c == 'B':
        if current.next is not None:
            current.next.prev = current.prev
        current.prev.next = current.next
        current = current.prev
    elif c == 'L':
        current = current.prev
    elif c == 'R':
        current = current.next
    else:
        n = Node()
        n.data = c
        if current.next is not None:
            n.next = current.next
            current.next.prev = n
        else:
            n.next = None

        current.next = n
        n.prev = current
        current = n

while current.prev is not None:
    current = current.prev

s = ""
while current.next is not None:
    current = current.next
    s += current.data

print(s)
