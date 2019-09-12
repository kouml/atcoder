inp = input().split(' ')
n, a, b, c = [int(i) for i in inp]

l = []
for i in range(n):
    l.append(int(input()))

# 全てのlに対して、
abcd = [0, 0, 0, 0]




x = []
u = []
sum_m = []

for i in range(N):
    j, k = input().split(' ')
    if k == 'JPY':
        sum_m.append(int(j))
        x.append(int(j))
    elif k == 'BTC':
        sum_m.append(float(j) * 380000.0)
        x.append(float(j))
    u.append(k)

print(sum(sum_m))
