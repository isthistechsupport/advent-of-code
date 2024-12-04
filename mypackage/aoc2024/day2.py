from aocd import get_data, submit


def test_for_safety(values: list[int]) -> bool:
    ascending = values[0] < values[-1]
    for i in range(len(values) - 1):
        diff = abs(values[i] - values[i + 1])
        locally_ascending = values[i] < values[i + 1]
        if diff not in range(1, 4) or (locally_ascending != ascending):
            return False
    return True


def part_a(data: str) -> int:
    result = 0
    for line in data.splitlines():
        values = list(map(int, line.split()))
        result += test_for_safety(values)
    return result


def list_del(l: list, i: int) -> list:
    list_copy = list(l)
    del list_copy[i]
    return list_copy


def test_for_safety_dampened(values: list[int]) -> bool:
    ascending = values[0] < values[-1]
    for i in range(len(values) - 1):
        diff = abs(values[i] - values[i + 1])
        locally_ascending = values[i] < values[i + 1]
        if diff not in range(1, 4) or (locally_ascending != ascending):
            safety_i_removed = test_for_safety(list_del(values, i))
            safety_i_plus_1_removed = test_for_safety(list_del(values, i+1))
            return safety_i_removed or safety_i_plus_1_removed
    return True


def part_b(data: str) -> int:
    result = 0
    for line in data.splitlines():
        values = list(map(int, line.split()))
        result += test_for_safety_dampened(values)
    return result


test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    

if __name__ == "__main__":
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    data = get_data(day=2, year=2024)
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=2, year=2024)
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=2, year=2024)
