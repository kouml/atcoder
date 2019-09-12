n = input()
a = []
n = int(n)

for i in range(n):
    a.append(int(input()))

prev_v = a[0]
count = 1
t_v = a[0]

for x in a[1:]:
    if prev_v < x:
        pass
    else:
        if t_v < x:
            t_v = x
        else:
            count += 1
    prev_v = x

print(count)





    t = [a[0]]
    for i in a:
        if i < t[-1]:
            t.append(i)

print(len(t))




