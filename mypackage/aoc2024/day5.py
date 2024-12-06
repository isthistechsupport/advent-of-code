from aocd import get_data, submit
import mypackage.aoc2024.testing_data as testing_data


def parse_input(data: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules_str, updates_str = data.split("\n\n")
    rules = [tuple(map(int, rule.split('|'))) for rule in rules_str.splitlines()]
    updates = [list(map(int, update.split(','))) for update in updates_str.splitlines()]
    return rules, updates


def check_rule(rule: tuple[int, int], update: list[int]) -> bool:
    first, second = rule
    if second in update:
        return first not in update[update.index(second):]
    return True


def check_update(rules: list[tuple[int, int]], update: list[int]) -> bool:
    for rule in rules:
        if not check_rule(rule, update):
            return False
    return True


def get_update_median(update: list[int]) -> int:
    return update[len(update) // 2]


def check_page(page: int, rules: list[tuple[int, int]], update: list[int]) -> bool:
    for first, second in rules:
        if page == second:
            if first in update:
                return False
    return True


def reorder_pages(rules: list[tuple[int, int]], update: list[int], pages: list[int]) -> list[int]:
    for i, page in enumerate(update):
        if len(update) == 1:
            pages.append(page)
            return pages
        elif check_page(page, rules, update):
            update.pop(i)
            pages.append(page)
            return reorder_pages(rules, update, pages)


def part_a(data: str) -> int:
    rules, updates = parse_input(data)
    result = 0
    for update in updates:
        if check_update(rules, update):
            result += get_update_median(update)
    return result


def part_b(data: str) -> int:
    rules, updates = parse_input(data)
    result = 0
    for update in updates:
        if not check_update(rules, update):
            result += get_update_median(reorder_pages(rules, update, []))
    return result


if __name__ == "__main__":
    test_data = testing_data.day_5
    data = get_data(day=5, year=2024)
    assert part_a(test_data) == 143, part_a(test_data)
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=5, year=2024)
    assert part_b(test_data) == 123, part_b(test_data)
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=5, year=2024)
