value = 0
length = 0
i = 1
mat = {}

while i <= 1000000:
    value = i
    c = 0
    while value != 1:
        if value not in mat.keys():
            if value % 2 == 0:
                value = value / 2
            else:
                value = value * 3 + 1
        else:
            c += mat[value]
            break
        c += 1
    mat[i] = c
    i += 2

values = max(mat, key=mat.get)
print(values)
print(mat[values]+1)
