s = input()
y, m, d = s.split('/')


def heisei(y, m, d):
    if int(y) < 2019:
        return 'Heisei'
    elif int(y) > 2019:
        return 'TBD'
    elif int(y) == 2019:
        if int(m) > 4:
            return 'TBD'
        elif int(m) < 4:
            return 'Heisei'
        elif int(m) == 4:
            if int(d) == 30:
                return 'Heisei'
            elif int(d) > 30:
                return 'TBD'
            else:
                return 'Heisei'


print(heisei(y, m, d))

