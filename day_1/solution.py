spelled_digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

# recusive solution 🎅
def get_first_matching_digit(string, spelled_digits, part=1):
    for j in range(9):
        if part == 2 and (
            string.startswith(spelled_digits[j]) or string.startswith(str(j + 1))
        ): # if part 2, check if the string starts with the spelled digit or the digit itself
            return str(j + 1)
        elif string.startswith(str(j + 1)): # if part 1, check if the string starts with the digit itself
            return str(j + 1)

    if len(string) == 0:
        return None

    return get_first_matching_digit(
        string=string[1:], spelled_digits=spelled_digits, part=part
    )


def solution(part=1):
    total = 0
    for string in open(0):
        string = string.strip()

        # if empty line, skip
        if string == "":
            continue

        first_and_last_digits = [
            get_first_matching_digit(string, spelled_digits, part),  # forward
            get_first_matching_digit(
                string[::-1], [r[::-1] for r in spelled_digits], part
            ),  # backward
        ]

        total += int(first_and_last_digits[0] + first_and_last_digits[-1])

    return total


print(solution(part=2))
