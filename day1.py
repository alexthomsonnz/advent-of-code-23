from rich import print
import re

file = open("./inputs/day1.txt")
lines = [line.rstrip() for line in file]


# Part 1
sum = 0
for line in lines:
    line = re.sub("[^0-9]", "", line)
    if len(line) == 0:
        continue
    numbersconcat = line[0] + line[-1]

    sum += int(numbersconcat)

print(f"part 1 {sum=}")


sum = 0
map = dict(
    one=1,
    two=2,
    three=3,
    four=4,
    five=5,
    six=6,
    seven=7,
    eight=8,
    nine=9,
)
for line in lines:
    letter_a: int = None
    letter_b: int = None

    # Find first letter
    segment = ""
    for letter in line:
        if letter_a:
            break
        segment += letter

        for key, value in map.items():
            if letter_a:
                break
            if key in segment:
                letter_a = value
            if len(re.findall(r"\d+", segment)):
                letter_a = int(re.findall(r"\d+", segment)[0])

    segment = ""
    for letter in reversed(line):
        if letter_b:
            break
        segment = letter + segment
        for key, value in map.items():
            if letter_b:
                break
            if key in segment:
                letter_b = value
            if len(re.findall(r"\d+", segment)):
                letter_b = int(re.findall(r"\d+", segment)[0])

    if letter_a is None and letter_b is None:
        continue

    numbersconcat = f"{letter_a}{letter_b}"

    print(numbersconcat)

    sum += int(numbersconcat)

print(f"part 2 {sum=}")
