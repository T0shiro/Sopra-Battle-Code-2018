v1 = int(input())
v2 = int(input())
v3 = int(input())

min_v = min(v1, v2, v3)

t = 1.0 / float(min_v)

print(str(t*60) + " min")
