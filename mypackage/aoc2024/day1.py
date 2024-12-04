from aocd import get_data, submit


def parse_data(data: str) -> tuple[list[int], list[int]]:
    list_1, list_2 = [], []
    for line in data.splitlines():
        num1, num2 = map(int, line.split())
        list_1.append(num1)
        list_2.append(num2)
    return list_1, list_2


def part_a(data: str) -> int:
    list_1, list_2 = parse_data(data)
    ordered_lists = list(zip(sorted(list_1), sorted(list_2)))
    result = 0
    for num1, num2 in ordered_lists:
        result += abs(num1 - num2)
    return result


def part_b(data: str) -> int:
    list_1, list_2 = parse_data(data)
    result = 0
    for i in list_1:
        count_i = list_2.count(i)
        result += i * count_i
    return result


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


if __name__ == "__main__":
    assert part_a(test_data) == 11
    assert part_b(test_data) == 31
    data = get_data(day=1, year=2024)
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=1, year=2024)
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=1, year=2024)
