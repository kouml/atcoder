ori_s = input()
t = input()

if set(t).issubset(set(ori_s)):
    if t in s:
        print(s.find(t))
    else:
        idx = 0
        n_times = 0
        current_idx = 0
        s = ori_s
        for i in t:
            idx = s[idx:].find(i)
            if idx == -1:
                # 初期化
                s = ori_s
                current_idx = 0
                n_times += 1
                # 再検索
                idx = s.find(i)
                current_idx += idx
            else:
                s = s[idx+1:]
                current_idx += (idx+1)
            # print(i)
            # print(current_idx)
            print(n_times)
        idx = current_idx + n_times * len(ori_s)
        print(idx)
else:
    print(-1)
