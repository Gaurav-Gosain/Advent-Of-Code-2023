# Day 24, vectors 🎅

import re

from z3 import BitVec, Solver, sat

lines = open(0).read().strip().split("\n")

eqns = []
minVal = 2e14
maxVal = 4e14

for line in lines:
    nums = [int(i) for i in re.findall(r"-?\d+", line)]
    slope = nums[4] / nums[3]
    intercept = nums[1] - (nums[0] * slope)
    eqns.append([slope, intercept, nums[0], nums[3] > 0])

out = 0
for i, a in enumerate(eqns):
    for b in eqns[i + 1 :]:
        if a[0] != b[0]:
            intersectX = (b[1] - a[1]) / (a[0] - b[0])
            if (a[3] and intersectX < a[2]) or (not a[3] and intersectX > a[2]):
                continue
            elif (b[3] and intersectX < b[2]) or (not b[3] and intersectX > b[2]):
                continue
            intersectY = (a[0] * intersectX) + a[1]
            if (
                intersectX >= minVal
                and intersectX <= maxVal
                and intersectY >= minVal
                and intersectY <= maxVal
            ):
                out += 1

print("Part 1:", out)


def bitVec(n):
    return BitVec(n, 64)


x, y, z = bitVec("x"), bitVec("y"), bitVec("z")
vx, vy, vz = bitVec("vx"), bitVec("vy"), bitVec("vz")
s = Solver()

for i, (px, py, pz, pvx, pvy, pvz) in enumerate(
    [[int(i) for i in re.findall(r"-?\d+", line)] for line in lines]
):
    t = bitVec(f"t_{i}")
    s.add(t >= 0)
    s.add(x + vx * t == px + pvx * t)
    s.add(y + vy * t == py + pvy * t)
    s.add(z + vz * t == pz + pvz * t)

assert s.check() == sat
m = s.model()
x, y, z = m.eval(x).as_long(), m.eval(y).as_long(), m.eval(z).as_long() # type: ignore
print("Part 2:", x + y + z)
