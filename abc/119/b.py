N = int(input())

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
