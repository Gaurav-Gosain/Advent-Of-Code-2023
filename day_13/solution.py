# Day 13, ...mirror | rorrim... 🎅

def get_score(pattern, diff_count=0):
    m = len(pattern)
    n = len(pattern[0])

    for c in range(n - 1):
        i = 0
        diff = 0
        while c - i >= 0 and c + 1 + i < n:
            for r in range(m):
                if pattern[r][c - i] != pattern[r][c + 1 + i]:
                    diff += 1
                    if diff > diff_count:
                        break
            if diff > diff_count:
                break
            i += 1
        if diff == diff_count:
            return c + 1

    for r in range(m - 1):
        i = 0
        diff = 0
        while r - i >= 0 and r + 1 + i < m:
            for c in range(n):
                if pattern[r - i][c] != pattern[r + 1 + i][c]:
                    diff += 1
                    if diff > diff_count:
                        break
            if diff > diff_count:
                break
            i += 1
        if diff == diff_count:
            return 100 * (r + 1)


p1 = 0
p2 = 0
result = [(get_score((p:=list(map(list,pattern.strip().split("\n"))))), get_score(p, 1)) for pattern in open(0).read().split("\n\n")]

p1 = sum([r[0] for r in result])
p2 = sum([r[1] for r in result])

print("Part 1:", p1)
print("Part 2:", p2)
