# Day 10, I don't like this one... 🎅

from collections import defaultdict

s = list(filter(None, open(0).read().splitlines()))

# (x,y) =>[(x,y),...]
con = defaultdict(list)

st = 0, 0
for i in range(len(s)):
    for j in range(len(s[i])):
        c = s[i][j]
        if c in "|LJ":
            con[i, j].append((i - 1, j))
        if c in "-J7":
            con[i, j].append((i, j - 1))
        if c in "|7F":
            con[i, j].append((i + 1, j))
        if c in "-LF":
            con[i, j].append((i, j + 1))
        if c == "S":
            st = i, j

ss = set()
for n, m in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
    if st in con[st[0] + n, st[1] + m]:
        con[st].append((st[0] + n, st[1] + m))
        ss.add((n, m))

lc = st
ls = -1, -1
pt = []
while not pt or lc != st:
    # print(lc)
    nx = con[lc][1] if con[lc][0] == ls else con[lc][0]
    ls = lc
    lc = nx
    pt.append(lc)

# lop wtf
M = {
    "|": "010010010",
    "-": "000111000",
    "L": "010011000",
    "J": "010110000",
    "7": "000110010",
    "F": "000011010",
    ".": "000000000",
}

M["S"] = M["L"]


def ad(c):
    v = [int(x) for x in M[c]]
    mp[-3].extend(v[:3])
    mp[-2].extend(v[3:6])
    mp[-1].extend(v[6:])


mp = []
for i in range(len(s)):
    mp.append([])
    mp.append([])
    mp.append([])
    for j in range(len(s[i])):
        ad(s[i][j] if (i, j) in pt else ".")

print(len(mp), len(mp[0]))

vis = set()
vis = [[0 for _ in range(len(mp[0]))] for _ in range(len(mp))]
q = [(1, 1)]
are = set()
while q:
    c = q.pop()
    # if c in vis:continue
    # vis.add(c)
    if vis[c[0]][c[1]]:
        continue
    vis[c[0]][c[1]] = 1
    if (c[0] // 3, c[1] // 3) not in pt:
        are.add((c[0] // 3, c[1] // 3))
    for n, m in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
        i, j = c[0] + n, c[1] + m
        # if (i,j) in vis:continue
        if i < 0 or j < 0:
            continue
        if i >= len(mp) or j >= len(mp[0]):
            continue
        if vis[i][j]:
            continue
        if mp[i][j]:
            continue
        q.append((i, j))

print(len(s) * len(s[0]) - len(pt) - len(are))
