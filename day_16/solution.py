# Day 16, Reflecting grid 🎅

from collections import deque


class direction(tuple):
    def __add__(self, other):
        return direction(x + y for x, y in zip(self, other))


NORTH = direction((-1, 0))
SOUTH = direction((1, 0))
EAST = direction((0, 1))
WEST = direction((0, -1))


def traverse(grid, start, dstart):
    q = deque([(direction(start), direction(dstart))])
    visited = set()

    while q:
        i, di = q.popleft()
        if i not in grid or (i, di) in visited:
            continue
        visited.add((i, di))
        match grid[i]:
            case "/":
                di = -di[1], -di[0]
                q.append((i + di, di))
            case "\\":
                di = di[1], di[0]
                q.append((i + di, di))
            case "|" if di[0] == 0:
                q.append((i + NORTH, NORTH))
                q.append((i + SOUTH, SOUTH))
            case "-" if di[1] == 0:
                q.append((i + EAST, EAST))
                q.append((i + WEST, WEST))
            case _:
                q.append((i + di, di))

    return len(set(p for p, _ in visited))


def p1(data):
    grid = {(i, j): x for i, row in enumerate(data) for j, x in enumerate(row.strip())}
    return traverse(grid, (0, 0), EAST)


def p2(lines):
    grid = {(i, j): x for i, row in enumerate(lines) for j, x in enumerate(row.strip())}
    n, m = len(lines), len(lines[0])

    result = 0
    for i in range(n):
        result = max(result, traverse(grid, (0, i), SOUTH))
        result = max(result, traverse(grid, (n - 1, i), NORTH))
    for i in range(m):
        result = max(result, traverse(grid, (0, i), EAST))
        result = max(result, traverse(grid, (n - 1, i), WEST))

    return result


data = open(0).read().splitlines()

print("Part 1:", p1(data))
print("Part 2:", p2(data))
