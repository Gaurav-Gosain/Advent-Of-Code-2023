# Day 5, Oof that was challenging... 🎅

from copy import deepcopy

seeds, *data = open(0).read().strip().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

cp_seeds = deepcopy(seeds)

maps = [[list(map(int, i.split())) for i in d.split("\n")[1:]] for d in data]

for m in maps:
    for i, value in enumerate(seeds):
        for destination_start, source_start, map_range in m:
            if source_start <= value < source_start + map_range:
                seeds[i] = destination_start + value - source_start
                break

print("Part 1", min(seeds))

seeds = deepcopy(cp_seeds)
ranges = list(zip(seeds[0::2], seeds[1::2]))

for m in maps:
    for i, (value_start, value_range) in enumerate(ranges):
        for destination_start, source_start, map_range in m:
            source_end = source_start + map_range - 1
            if source_start <= value_start <= source_end:
                value_end = value_start + value_range - 1
                mapped_start = destination_start + value_start - source_start
                if value_end <= source_end:
                    ranges[i] = (mapped_start, value_range)
                else:
                    ranges[i] = (mapped_start, source_end - value_start + 1)
                    ranges.append((source_end + 1, value_range - source_end + value_start - 1))
                break

print("Part 2", min(ranges)[0])
