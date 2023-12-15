# Day 15, hash 🎅

data = open(0).read().strip().split(",")


def find_hash(s):
    v = 0
    for c in s:
        v = ((v + ord(c)) * 17) % 0x100
    return v


print("Part 1:", sum(map(find_hash, data)))

boxes = [[] for _ in range(0x100)]
for item in data:
    if item[-1].isdigit():
        label, power = item.split("=")
        power = int(power)
        box = boxes[find_hash(label)]
        found = False
        for i, (l, _) in enumerate(box):
            if found := (l == label):
                box[i] = (label, power)
                break

        if not found:
            box += [(label, power)]
    else:
        idx = find_hash((label := item[:-1]))
        boxes[idx] = [item for item in boxes[idx] if item[0] != label]

print(
    "Part 2:",
    sum(
        (i + 1) * (j + 1) * power
        for i, box in enumerate(boxes)
        for j, (_, power) in enumerate(box)
    ),
)
