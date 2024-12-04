import re
from aocd import get_data, submit


def sumproduct(data: str) -> int:
    regex = r"mul\((\d*),(\d*)\)"
    matches = re.finditer(regex, data, re.MULTILINE)
    result = 0
    for match in matches:
        result += int(match.group(1)) * int(match.group(2))
    return result


def part_a(data: str) -> int:
    return sumproduct(data)


def part_b(data: str) -> int:
    result_b = 0
    for substr in data.split("do()"):
        enabled_instructions = substr.split("don't()")[0]
        result_b += sumproduct(enabled_instructions)
    return result_b


test_data_a = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_data_b = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


if __name__ == "__main__":
    assert part_a(test_data_a) == 161
    assert part_b(test_data_b) == 48
    data = get_data(day=3, year=2024)
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=3, year=2024)
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=3, year=2024)
