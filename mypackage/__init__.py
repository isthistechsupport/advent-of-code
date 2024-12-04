import importlib

def mysolve(year, day, data):
    mod_name = f"mypackage.aoc{year}.day{day}"
    mod = importlib.import_module(mod_name)
    a = mod.part_a(data)
    b = mod.part_b(data)
    return a, b
