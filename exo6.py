def arms(n):
    res = 0
    for c in n:
        res += int(c) ** len(n)
        if res > int(n):
            break
    return res
    # return sum([int(c) ** len(n) for c in n])


l = []
vals = []
for i in range(0, 10000000):
    if 11 <= i <= 99:
        pass
    else:
        nb = str(i)
        if i == arms(nb):
            vals.append(i)
print(vals)
print(len(vals))
