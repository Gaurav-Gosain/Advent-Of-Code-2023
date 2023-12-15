# Day 15, hash 🎅

data = open(0).read().strip().split(",")


def find_hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v = v % 0x100
    return v


print("Part 1:", sum(map(find_hash, data)))

boxes = [[] for _ in range(0x100)]
for item in data:
    if item[-1].isdigit():
        label, power = item.split("=")
        power = int(power)
        box = boxes[find_hash(label)]
        found = False
        for i, lens in enumerate(box):
            if found := lens[0] == label:
                box[i] = (label, power)
                break

        if not found:
            box += [(label, power)]
    else:
        box = boxes[(idx := find_hash((label := item[:-1])))]
        boxes[idx] = [_ for _ in box if _[0] != label]

print(
    "Part 2:",
    sum(
        (i + 1) * (j + 1) * lens[1]
        for i, box in enumerate(boxes)
        for j, lens in enumerate(box)
    ),
)
