n, q = list(map(int, input().split(" ")))
a = []
b = []
for i in range(n-1):
    j, k = list(map(int, input().split(" ")))
    a.append(j)
    b.append(k)

p = []
x = []
for i in range(q):
    j, k = list(map(int, input().split(" ")))
    p.append(j)
    x.append(k)


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
tree = []
for i in range(n):
    tree.append(Node(i))

for j, k in zip(a, b):
    tree[j-1].add_node(tree[k-1])

for j, k in zip(p, x):
    tree[j-1].add_count(k)

# traverse
for i in tree:
    for j in i.linked:
        j.counter += i.counter

m = []
for i in tree:
    m.append(i.counter)

print(" ".join(map(str, m)))
