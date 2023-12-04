# Day 4, Hmm 🎅

d = open(0).read().strip().split("\n")

part_1 = 0
won_cards = {i + 1: 1 for i in range(len(d))}

for idx, g in enumerate(d):
    _, g = g.split(": ")
    a, b = map(str.split, g.split(" | "))
    c = sum(1 for e in a if e in b)
    
    if c:
        part_1 += 2**(c-1)

        for i in range(idx + 2, idx + c + 2):
            won_cards[i] += won_cards[idx + 1]

part_2 = sum(won_cards.values())

print(part_1)
print(part_2)
