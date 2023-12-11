# Day 3, Lets goo! 🎅

d = open(0).read().strip().split("\n")


# find all numbers in the matrix
def find_numbers(matrix):
    numbers = []
    for j, row in enumerate(matrix):
        i = 0
        while i < len(row):
            if row[i].isdigit():
                # find the start and end position of the number in the matrix
                start = i
                end = i
                while end < len(row) - 1 and row[i + 1].isdigit():
                    end += 1
                    i += 1
                numbers.append(
                    {
                        "value": row[start : end + 1],
                        "position": ((j, start), (j, end)),
                        "gears": [],
                    }
                )
            i += 1
    return numbers


def check_surrounding(w, h, position, matrix):
    start, end = position

    start_x, start_y = start
    end_x, end_y = end

    gears = []

    # make sure we don't go out of bounds
    a = max(start_x - 1, 0)
    b = min(end_x + 1, h - 1)
    c = max(start_y - 1, 0)
    d = min(end_y + 1, w - 1)

    found_symbol = False
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if matrix[i][j] != "." and not matrix[i][j].isdigit():
                found_symbol = True
            if matrix[i][j] == "*":
                gears.append((i, j))

    return found_symbol, gears


w, h = len(d[0]), len(d)
numbers = find_numbers(d)

part_1 = 0

for number in numbers:
    x, y = number["position"]
    found_symbol, gears = check_surrounding(w, h, number["position"], d)
    if found_symbol:
        part_1 += int(number["value"])
        number["gears"] = gears

print(part_1)

# for each number pair,
# check if they have a gear position in common,
# if they do, multiply them together and add to part 2
part_2 = 0

for i, number in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        if i != j:
            if number["gears"] and number2["gears"]:
                if len(set(number["gears"]).intersection(set(number2["gears"]))) > 0:
                    part_2 += int(number["value"]) * int(number2["value"])

part_2 = part_2 // 2

print(part_2)
