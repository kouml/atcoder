from collections import defaultdict
from collections import Counter

n = input()
v = input()
v = [int(i) for i in v.split(" ")]
odd_v = v[::2]
even_v = v[1::2]
m = int(n) / 2

count_odd_v = dict(Counter(odd_v))
count_even_v = dict(Counter(even_v))

o_idx1, o_cnt1 = sorted(count_odd_v.items(), key=lambda x: x[1])[0]
e_idx1, e_cnt1 = sorted(count_even_v.items(), key=lambda x: x[1])[0]

nb_change = 0
if len(count_even_v) == 1 and len(count_odd_v) == 1:
    if o_idx1 == e_idx1:
        nb_change += m
    else:
        nb_change += 0
elif len(count_even_v) == 1:
    nb_change += m - o_cnt1
elif len(count_odd_v) == 1:
    nb_change += m - e_cnt1
else:
    o_idx2, o_cnt2 = sorted(count_odd_v.items(), key=lambda x: x[1])[1]
    e_idx2, e_cnt2 = sorted(count_even_v.items(), key=lambda x: x[1])[1]

    # どちらの数列も同じ数字で、数が違った場合
    if o_idx1 == e_idx1:
        if o_cnt1 < e_cnt1:
            nb_change += m - e_cnt1 # even count
            nb_change += m - o_cnt2 # odd count
        elif e_cnt1 < o_cnt1:
            nb_change += m - e_cnt2  # even count
            nb_change += m - o_cnt1  # odd count
        elif o_cnt1 == e_cnt1:
            if o_cnt2 < e_cnt2:
                nb_change += m - e_cnt2 # even count
                nb_change += m - o_cnt1 # even count
            elif o_cnt2 <= e_cnt2:
                nb_change += m - o_cnt2  # even count
                nb_change += m - e_cnt1  # even count
    elif o_idx1 != e_idx1:
        nb_chagne += m - e_cnt1
        nb_chagne += m - o_cnt1

print(int(nb_change))
