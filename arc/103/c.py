n = input()
v = input()
v = v.split(" ")
v = [int(i) for i in v]


odd_v = v[::2]
even_v = v[1::2]

counter_odd = {}

for i in odd_v:
    if i not in counter_odd:
        counter_odd[i] = 1
    else:
        counter_odd[i] += 1

counter_even = {}
for i in even_v:
    if i not in counter_even:
        counter_even[i] = 1
    else:
        counter_even[i] += 1


max_odd = -1e+100
max_odd_idx = 0
for k, v in counter_odd.items():
    if max(v, max_odd) == v:
        max_odd = v
        max_odd_idx = k


max_even = -1e+100
max_even_idx = 0
for k, v in counter_even.items():
    if max(v, max_even) == v:
        max_even = v
        max_even_idx = k

should_change_odd = None

if max_odd_idx == max_even_idx:
    if max_odd <= max_even:
        should_change_odd = True
    else:
        should_change_odd = False

nb_change = 0
m = int(n) / 2

if should_change_odd is None:
    nb_change += m - max_odd
    nb_change += m - max_even
elif should_change_odd is True:
    # 2nd largest item
    if len(counter_odd.items()) == 1:
        nb_change += m
    else:
        s = sorted(counter_odd.items(), key=lambda x:x[1])[0][1]
        nb_change += m - s
        nb_change += m - max_even
elif should_change_odd is False:
    # 2nd largest item
    if len(counter_even.items()) == 1:
        nb_change += m
    else:
        s = sorted(counter_even.items(), key=lambda x: x[1])[0][1]
        nb_change += m - s
        nb_change += m - max_odd

print(int(nb_change))
