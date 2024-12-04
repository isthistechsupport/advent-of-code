# Advent of Code 2024, day 3, part A

import re
from aocd import get_data, submit

data = get_data(day=3, year=2024)

def sumproduct(data: str) -> int:
    regex = r"mul\((\d*),(\d*)\)"
    matches = re.finditer(regex, data, re.MULTILINE)
    result = 0
    for match in matches:
        result += int(match.group(1)) * int(match.group(2))
    return result

result_a = sumproduct(data)
print(f"Part A: {result_a}")
submit(result_a, part="a", day=3, year=2024)

# Part B

result_b = 0
for substr in data.split("do()"):
    enabled_instructions = substr.split("don't()")[0]
    result_b += sumproduct(enabled_instructions)

print(f"Part B: {result_b}")
submit(result_b, part="b", day=3, year=2024)
