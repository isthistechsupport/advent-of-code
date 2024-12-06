from aocd import get_data, submit


def parse_data(data: str) -> list[list[str]]:
    lines = data.splitlines()
    soup = ["..."+"."*len(lines[0])+"..." for _ in range(3)]
    bottom_padding = list(soup)
    soup.extend(["..."+line+"..." for line in lines])
    soup.extend(bottom_padding)
    return [list(line) for line in soup]


def check_direction(grid: list[list[str]], x: int, y: int, dx: int, dy: int, results: list[tuple[int, int]]) -> bool:
    try:
        char1 = grid[x][y]
        char2 = grid[x+dx][y+dy]
        char3 = grid[x+2*dx][y+2*dy]
        char4 = grid[x+3*dx][y+3*dy]
        string = char1 + char2 + char3 + char4
        if string == "XMAS":
            results.extend([(x, y), (x+dx, y+dy), (x+2*dx, y+2*dy), (x+3*dx, y+3*dy)])
            return True
    except IndexError:
        pass
    return False


def check_around(grid: list[list[str]], x: int, y: int, results: list[tuple[int, int]]) -> int:
    result = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == dy == 0:
                continue
            if check_direction(grid, x, y, dx, dy, results):
                result += 1
    return result


def check_cross(grid: list[list[str]], x: int, y: int, results: list[tuple[int, int]]) -> int:
    result = 0
    diag_1 = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
    diag_2 = grid[x+1][y-1] + grid[x][y] + grid[x-1][y+1]
    diag_1_rev = diag_1[::-1]
    diag_2_rev = diag_2[::-1]
    valid_diags = ["MAS", "SAM"]
    result = diag_1 in valid_diags and diag_1_rev in valid_diags and diag_2 in valid_diags and diag_2_rev in valid_diags
    if result:
        results.extend([(x-1, y-1), (x, y), (x+1, y+1), (x+1, y-1), (x, y), (x-1, y+1)])
    return result


def part_a(data: str) -> int:
    results_coordinates = []
    grid = parse_data(data)
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "X":
                result += check_around(grid, x, y, results=results_coordinates)
    return result


def part_b(data:str) -> int:
    results_coordinates = []
    grid = parse_data(data)
    result = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "A":
                result += check_cross(grid, x, y, results=results_coordinates)
    return result


test_data_a_1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X...."""


test_data_a_2 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


test_data_b_1 = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


def render_cleaned_grid(grid: list[list[str]], results: list[tuple[int, int]]) -> str:
    for x_g in range(len(grid)):
        for y_g in range(len(grid[x_g])):
            if not (x_g, y_g) in results:
                grid[x_g][y_g] = "."
    return "\n".join(["".join(line) for line in grid])


if __name__ == "__main__":
    data = get_data(day=4, year=2024)
    assert part_a(test_data_a_1) == 4
    assert part_a(test_data_a_2) == 18
    result_a = part_a(data)
    print(f"Part A: {result_a}")
    submit(result_a, part="a", day=4, year=2024)
    assert part_b(test_data_a_2) == 9
    assert part_b(test_data_b_1) == 9
    result_b = part_b(data)
    print(f"Part B: {result_b}")
    submit(result_b, part="b", day=4, year=2024)
