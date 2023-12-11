# Day 11, I like this one... 🎅

space = list(map(list, open(0).read().splitlines()))

# find all the rows and columns with only "." in them
rows = [
    i
    for i in range(len(space))
    if all(space[i][j] == "." for j in range(len(space[i])))
]
cols = [
    j
    for j in range(len(space[0]))
    if all(space[i][j] == "." for i in range(len(space)))
]

# find the positions of each "#"
galaxies = [
    (i, j)
    for i in range(len(space))
    for j in range(len(space[i]))
    if space[i][j] == "#"
]


# Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time.
def find_shortest_path(start, end, distance=1):
    z = distance - 1

    d_row = abs(end[0] - start[0])
    for row in rows:
        if min(start[0], end[0]) < row < max(start[0], end[0]):
            d_row += z

    d_col = abs(end[1] - start[1])
    for col in cols:
        if min(start[1], end[1]) < col < max(start[1], end[1]):
            d_col += z
    return d_row + d_col


def solution(part=1):
    distance = 2 if part == 1 else 1_000_000
    total = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += find_shortest_path(galaxies[i], galaxies[j], distance)
    return total


print(solution(part=1))
print(solution(part=2))
