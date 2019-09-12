a = input()
n, d = a.split(" ")
n = int(n)
d = int(d)

if n%(d*2+1) == 0:
    print((n//(d*2+1)))
else:
    print((n//(d*2+1))+1)
