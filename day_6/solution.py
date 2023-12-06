# Day 5, Wow easy much... 🎅

time, distance = open(0).read().strip().split("\n")

process = lambda x: list(map(int, x.split(": ")[1].split()))

time = process(time)
distance = process(distance)

p1 = 1

def get_value(t, d):
    for i in range(t):
        x = (t - i) * i
        if x > d:
            return int((t / 2 - i) * 2) + 1
    return -1


for t, d in zip(time, distance):
    p1 *= get_value(t, d)

print(p1)

fix = lambda x: int("".join(map(str, x)))
p2 = get_value(fix(time), fix(distance))

print(p2)
