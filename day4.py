from collections import defaultdict
from rich import print, inspect
import re


with open("./inputs/day4.txt") as file:
    text = file.read()


lines = text.split("\n")

# Part 1

points = []
for line in lines:
    line = line.split(":")[1].strip()
    winning, my = (
        [int(val) for val in re.split(r"\s+", line.split("|")[0].strip())],
        [int(val) for val in re.split(r"\s+", line.split("|")[1].strip())],
    )

    score = 0

    for my_number in my:
        if my_number in winning:
            # Score!
            if score == 0:
                score = 1
                continue

            score = score * 2

    points.append(score)


print(f"part 1: {sum(points)}")

# Part 2

cards: dict[int, int] = defaultdict(lambda: 1)
for card, line in enumerate(lines):
    if card not in cards:
        cards[card] = 1

    line = line.split(":")[1].strip()
    winning, my = (
        [int(val) for val in re.split(r"\s+", line.split("|")[0].strip())],
        [int(val) for val in re.split(r"\s+", line.split("|")[1].strip())],
    )

    matches = 0
    for my_number in my:
        if my_number in winning:
            matches += 1

    next_cards = []

    number_of_iterations = cards[card]

    for idx in range(0, matches):
        cards[card + idx + 1] += number_of_iterations

print(f"part 2: {sum(cards.values())}")
