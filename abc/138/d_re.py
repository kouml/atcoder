n, q = list(map(int, input().split(" ")))
a = []
b = []
tree = []

class Node:
    def __init__(self, id):
        self.id = id
        self.counter = 0
        self.linked = []

    def add_node(self, node):
        self.linked.append(node)

    def add_count(self, count):
        self.counter += count

# make node
for i in range(n):
    tree.append(Node(i))

# add node
for i in range(n-1):
    j, k = list(map(int, input().split(" ")))
    tree[j-1].add_node(tree[k-1])

# add count
for i in range(q):
    j, k = list(map(int, input().split(" ")))
    tree[j-1].add_count(k)

# traverse
for i in tree:
    for j in i.linked:
        j.counter += i.counter

m = []
for i in tree:
    m.append(i.counter)

print(" ".join(map(str, m)))
