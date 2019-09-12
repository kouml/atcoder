n = int(input())
v = list(map(int, input().split(" ")))

v = sorted(v)

while len(v) != 1:
    s = v.pop(0)
    t = v.pop(0)
    v.append((s+t)/2)
    v = sorted(v)

print(v[0])