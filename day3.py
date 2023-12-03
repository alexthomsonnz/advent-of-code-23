from collections import defaultdict
from rich import print, inspect
import re


with open("./inputs/day3.txt") as file:
    text = file.read()

# Part 1 test
# text = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

# Part 2 test
# text = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""


lines = text.split("\n")


answer = 0

# Part 1

deltas = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0),           (1, 0),
    (-1, 1),  (0, 1),  (1, 1)
]

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter in "1234567890":
            if letter == ".":
                continue
            if line[x - 1] in "1234567890":
                continue

            # It's a number, and it's the first digit. Walk through the line to get the full number
            full_number = letter
            tmp_x = x
            while True:
                try:
                    tmp_x += 1
                    if line[tmp_x] in "1234567890":
                        full_number += line[tmp_x]
                    else:
                        break
                except IndexError:
                    break
            
            # Check if there's a number surrounding it
            end_loop = False
            for idx, _ in enumerate(full_number):
                if end_loop:
                    continue
                for direction in deltas:
                    if end_loop:
                        continue
                    try:
                        delta_letter = lines[y + direction[1]][x + direction[0] + idx]
                        if delta_letter in "1234567890.":
                            continue
                        else: 
                            answer += int(full_number)
                            end_loop = True
                    except IndexError:
                        pass

print(f"part 1: {answer}")
answer = 0


# dict type: (x, y): (count, product)
gears_with_numbers_adjacent: dict[(int, int), (int, int)] = defaultdict(lambda: (0, 1))

for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter in "1234567890":
            if letter == ".":
                continue
            if line[x - 1] in "1234567890":
                continue

            # It's a number, and it's the first digit. Walk through the line to get the full number
            full_number = letter
            tmp_x = x
            while True:
                try:
                    tmp_x += 1
                    if line[tmp_x] in "1234567890":
                        full_number += line[tmp_x]
                    else:
                        break
                except IndexError:
                    break
            
            # Check if there's a number surrounding it
            end_loop = False
            for idx, _ in enumerate(full_number):
                if end_loop:
                    break
                for (delta_x, delta_y) in deltas:
                    if end_loop:
                        break
                    try:
                        local_y = y + delta_y
                        local_x = x + delta_x + idx
                        delta_letter = lines[local_y][local_x]
                        if delta_letter != "*":
                            continue
                        
                        # Found a gear. Store coords, product and the number of times this gear has been found
                        count, product = gears_with_numbers_adjacent[(local_x, local_y)]
                        gears_with_numbers_adjacent[(local_x, local_y)] = (count + 1, product * int(full_number))
                        end_loop = True
                    except IndexError:
                        pass

answer = sum([product for (_, (idx, product)) in gears_with_numbers_adjacent.items() if idx > 1])

print(f"part 2: {answer}")
