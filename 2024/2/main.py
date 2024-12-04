# Advent of Code 2024, day 2, part A

from aocd import get_data, submit

data = get_data(day=2, year=2024)


def test_for_safety(values: list[int]) -> bool:
    ascending = values[0] < values[-1]
    for i in range(len(values) - 1):
        diff = abs(values[i] - values[i + 1])
        locally_ascending = values[i] < values[i + 1]
        if diff not in range(1, 4) or (locally_ascending != ascending):
            return False
    return True


result_a = 0
for line in data.splitlines():
    values = list(map(int, line.split()))
    result_a += test_for_safety(values)

print(f"Part A: {result_a}")
submit(result_a, part="a", day=2, year=2024)

# Part B

def test_for_safety_dampened(values: list[int]) -> bool:
    ascending = values[0] < values[-1]
    for i in range(len(values) - 1):
        diff = abs(values[i] - values[i + 1])
        locally_ascending = values[i] < values[i + 1]
        if diff not in range(1, 4) or (locally_ascending != ascending):
            values_copy_1 = list(values)
            values_copy_2 = list(values)
            del values_copy_1[i]
            del values_copy_2[i+1]
            safety_i_removed = test_for_safety(values_copy_1)
            safety_i_plus_1_removed = test_for_safety(values_copy_2)
            return safety_i_removed or safety_i_plus_1_removed
    return True


result_b = 0
for line in data.splitlines():
    values = list(map(int, line.split()))
    safe = test_for_safety_dampened(values)
    result_b += safe
    

print(f"Part B: {result_b}")
submit(result_b, part="b", day=2, year=2024)
