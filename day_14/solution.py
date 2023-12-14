# Day 14, rocks 🎅

CYCLES = int(10e9)
data = open(0).read().strip().split("\n")

def part_1():
    dish = data
    nrows = len(dish)
    total_weight = 0
    for row in ("".join(col) for col in zip(*dish)):
        stop = -1
        for pos, rock in enumerate(row):
            if rock == "#":
                stop = pos
            elif rock == "O":
                stop += 1
                total_weight += nrows - stop
    return total_weight


def part_2():
    dish = data
    nrows = len(dish)
    dish = ["".join(col) for col in zip(*dish)]

    def cycle(dish):
        for rev in [True, True, False, False]:
            # Roll and tranpose
            dish = ["".join(col) for col in zip(*[
                "#".join(["".join(sorted(part, reverse=rev)) for part in row.split("#")])
                for row in dish
            ])]
        return dish

    dish_hist = {}
    ncycles = 0
    while True:
        dish = cycle(dish)
        ncycles += 1
        key = "\n".join(dish)
        if key in dish_hist:
            break
        dish_hist[key] = ncycles
    diff = ncycles - dish_hist[key]
    for _ in range((CYCLES - ncycles) % diff):
        dish = cycle(dish)
    return sum([
        nrows - pos
        for row in dish
        for pos, rock in enumerate(row)
        if rock == "O"
    ])


print(part_1())
print(part_2())