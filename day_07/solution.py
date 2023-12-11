# Day 7, Poker Face... 🎅

d = [
    {"rank": i, "type": "", "value": c, "bid": int(b), "groups": [], "updated_value": c}
    for i, (c, b) in enumerate(list(map(str.split, open(0).read().strip().split("\n"))))
]


def pre_process(card):
    for card in d:
        if card["value"].count("J") != 0 and card["value"].count("J") != len(
            card["value"]
        ):
            # get the max occuring group of the card (excluding j) and replace j with the max group
            max_group = sorted(
                [
                    (i, card["value"].count(str(i)))
                    for i in set(card["value"])
                    if i != "J"
                ],
                key=lambda x: x[1],
                reverse=True,
            )[0][0]
            card["updated_value"] = card["value"].replace("J", str(max_group))
    return d


def process(labels, d):
    for card in d:
        card["groups"] = sorted(
            [card["updated_value"].count(str(i)) for i in set(card["updated_value"])],
            reverse=True,
        )[:2]

    # order all cards by their groups, then by the index of the label of the card
    for card in d:
        card["rank"] = "".join(map(str, card["groups"])) + "".join(
            str(hex(labels.index(i)))[2:] for i in card["value"]
        )

    # sort the cards by their rank
    d = sorted(d, key=lambda x: x["rank"])

    total = 0
    for i, card in enumerate(d):
        total += card["bid"] * (i + 1)

    return total


print("Part 1", process("23456789TJQKA", d))

print("Part 2", process("J23456789TQKA", pre_process(d)))
