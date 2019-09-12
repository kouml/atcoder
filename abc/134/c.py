n = input()
a = []
n = int(n)

for i in range(n):
    a.append(int(input()))

if n == 1:
    print(a[0])
else:
    s = sorted(a, reverse=True)[0]
    t = sorted(a, reverse=True)[1]

    for i in a:
        if i == s:
            print(t)
        else:
            print(s)
