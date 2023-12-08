# Day 8, interesting... 🎅

from math import lcm

instructions, _, *network = open(0).read().strip().split("\n")

network_map = {}

for i in network:
    node, connections = i.split(" = ")
    left, right = connections[1:-1].split(", ")
    network_map[node] = {
        "L": left,
        "R": right,
    }


def solution(node, part1):
    s = 0
    while True:
        instruction = instructions[s % len(instructions)]
        node = network_map[node][instruction]
        if node[[-1, 0][part1] :] == "Z" * [1, 3][part1]:
            return s + 1
        s += 1


# Part 1
print(solution("AAA", True))

# Part 2
print(
    lcm(
        *(
            solution(start, part1=False)
            for start in [start for start in network_map.keys() if start[-1] == "A"]
        )
    )
)
