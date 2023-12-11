# Day 8, Simple... 🎅

def solution(array, part_1=True):

    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = solution(deltas, part_1=part_1)
    p = -1 if part_1 else 0
    m = 1 if part_1 else -1
    return array[p] + diff * m

p1,p2 = 0,0

for line in open(0):
    nums = list(map(int, line.split()))
    p1 += solution(nums, part_1=True)
    p2 += solution(nums, part_1=False)

print(p1)
print(p2)
