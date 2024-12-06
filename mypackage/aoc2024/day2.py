from aocd import get_data, submit
import mypackage.aoc2024.testing_data as testing_data


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
    

if __name__ == "__main__":
    test_data = testing_data.day_2
    assert part_a(test_data) == 2
    assert part_b(test_data) == 4
    data = get_data(day=2, year=2024)
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=2, year=2024)
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=2, year=2024)
