# Day 5, Oof that was challenging... 🎅

from copy import deepcopy

seeds, *data = open(0).read().strip().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

cp_seeds = deepcopy(seeds)

maps = [[list(map(int, i.split())) for i in d.split("\n")[1:]] for d in data]

for m in maps:
    for i, v in enumerate(seeds):
        for d, s, r in m:
            if s <= v < s + r:
                seeds[i] = d + v - s
                break

print("Part 1", min(seeds))

seeds = deepcopy(cp_seeds)
ranges = list(zip(seeds[0::2], seeds[1::2]))

for m in maps:
    for i, (vs, vr) in enumerate(ranges):
        for d, s, r in m:
            se = s + r - 1
            if s <= vs <= se:
                ve = vs + vr - 1
                ms = d + vs - s
                if ve <= se:
                    ranges[i] = (ms, vr)
                else:
                    ranges[i] = (ms, se - vs + 1)
                    ranges.append((se + 1, vr - se + vs - 1))
                break

print("Part 2", min(ranges)[0])
