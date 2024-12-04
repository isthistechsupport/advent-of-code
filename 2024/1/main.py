# Advent of Code 2024, day 1, part A

from aocd import get_data, submit

data = get_data(day=1, year=2024)

list_1 = []
list_2 = []
ordered_lists = []
result_a = 0
for line in data.split('\n'):
    num1, num2 = map(int, line.split())
    list_1.append(num1)
    list_2.append(num2)

list_1.sort()
list_2.sort()

ordered_lists = list(zip(list_1, list_2))

for num1, num2 in ordered_lists:
    result_a += abs(num1 - num2)
print(f"Part A: {result_a}")
submit(result_a, part="a", day=1, year=2024)

# Part B

result_b = 0
for i in list_1:
    count_i = list_2.count(i)
    result_b += i * count_i
print(f"Part B: {result_b}")
submit(result_b, part="b", day=1, year=2024)
