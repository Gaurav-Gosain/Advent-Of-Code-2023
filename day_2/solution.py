# Day 2, Lets do this! 🎅

games = open(0).read().strip().split("\n")
valid_games = []
part_2 = 0
default_color_counter = {"blue": 0, "red": 0, "green": 0}


def parse_game(game):
    game_id, rounds = game.split(": ")

    game_id = game_id[5:]

    rounds = rounds.split("; ")
    rounds = [r.split(", ") for r in rounds]

    return game_id, rounds


for game in games:
    game_id, rounds = parse_game(game)

    valid_games.append(game_id)

    temp_rounds = []
    color_min = default_color_counter
    found = False

    for idx, subarray in enumerate(rounds):
        color_counter = default_color_counter
        # Iterate through each element in the subarray
        for element in subarray:
            # Split the element into count and color
            count, color = element.split()
            # Update the counter for the corresponding color
            color_counter[color] += int(count)

        if idx == 0:
            color_min = color_counter

        def get_min(color):
            if color_min[color] < color_counter[color]:
                color_min[color] = color_counter[color]
            return color_min[color]

        color_min["blue"] = get_min("blue")
        color_min["red"] = get_min("red")
        color_min["green"] = get_min("green")

        if not found:
            if (
                color_counter["blue"] > 14
                or color_counter["green"] > 13
                or color_counter["red"] > 12
            ):
                valid_games.pop()
                found = True

    part_2 += color_min["blue"] * color_min["red"] * color_min["green"]

part_1 = sum(map(int, valid_games))

print(part_1)
print(part_2)
