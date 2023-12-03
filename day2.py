from rich import print
import re


with open("./inputs/day2.txt") as file:
    text = file.read()

# Part 1 test
# text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Part 2 test
# text = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


lines = text.split("\n")


answer = 0

# Part 1


game = 0
for line in lines:
    game += 1
    cubes = {"red": [], "blue": [], "green": []}
    for cube in re.split(r"[;,]", line.split(":")[1]):
        cube = cube.replace(" ", "")
        color = [key for key in cubes if key in cube][0]
        number = int(cube.replace(color, ""))
        cubes[color].append(number)

    if max(cubes["red"]) > 12 or max(cubes["green"]) > 13 or max(cubes["blue"]) > 14:
        continue

    answer += game


print(f"part 1: {answer}")

answer = 0
# Part 2
game = 0
for line in lines:
    game += 1
    cubes = {"red": [], "blue": [], "green": []}
    for cube in re.split(r"[;,]", line.split(":")[1]):
        cube = cube.replace(" ", "")
        color = [key for key in cubes if key in cube][0]
        number = int(cube.replace(color, ""))
        cubes[color].append(number)

    answer += max(cubes["red"]) * max(cubes["green"]) * max(cubes["blue"])

    print(
        max(cubes["red"]),
        max(cubes["green"]),
        max(cubes["blue"]),
        max(cubes["red"]) * max(cubes["green"]) * max(cubes["blue"]),
    )


print(f"part 2: {answer}")
