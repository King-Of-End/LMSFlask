sp = [[int(y) for y in x.split()] for x in open('26_2580.txt').readlines()]
_, sk = sp[0]
np = []
for start, end in sp[1:]:
    if start == end == 0:
        np.append([start, end])
    if start < sk:
        start = sk
    if end < sk:
        if end == 0:
            end += sk - 1
        else:
            continue
    np.append([start - sk, end - sk])
np.sort()
k = np.count([0, 0])
sp = np[k:]
a = [0] * (max(map(max, sp)) + 1)
a[0] = k
a[-1] = -k
for start, end in sp:
    try:
        a[start] += 1
        a[end] -= 1
    except:
        print(start, end)
        raise
k = 0
lk = 0
n = 0
mk = []
for i in a:
    k += i
    mk = max(mk, k)
print(mk)
