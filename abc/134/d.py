n = int(input())
a = list(map(int, input().split(" ")))

num = len(a)
b = [0] * num

for i in reversed(range(1, num+1)):
    index = list(range(i, num+1, i))
    # print(index)
    count = 0
    for s in index:
        count += b[s-1]
    # print(count)

    if a[i-1] != count % 2:
        b[i-1] = 1

if max(b) == 0:
    print(0)
else:
    s = []
    for i, x in enumerate(b):
        if x == 1:
            s.append(i+1)
    print(len(s))
    print(" ".join(map(str, s)))
