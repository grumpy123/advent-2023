from textwrap import dedent

from day03 import Schema, Num


def test_parse():
    schema = Schema.parse(dedent('''
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        '''))
    assert schema.lines[2] == '..35..633.'
    assert schema.at(0, 0) == '4'
    assert schema.at(1, 3) == '*'


def test_find_nums():
    schema = Schema.parse(dedent('''
        467..114..
        ...*......
        .....+.58.
        ..........
        .....+..11
        '''))
    assert schema.nums == [
        Num(0, 0, 3, 467), Num(0, 5, 3, 114),
        Num(2, 7, 2, 58),
        Num(4, 8, 2, 11),
    ]
    assert schema.has_symbol_neighbor(schema.nums[0])
    assert not schema.has_symbol_neighbor(schema.nums[1])
    assert not schema.has_symbol_neighbor(schema.nums[2])


def test_solution():
    schema = Schema.parse(dedent('''
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        '''))
    assert schema.solution() == 4361


def test_solution_for_real():
    with open('test/day03.in') as data_file:
        schema = Schema.parse(data_file.read())
    assert schema.solution() == 525119


def test_gears():
    schema = Schema.parse(dedent('''
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        '''))
    assert schema.gears() == [
        [Num(0, 0, 3, 467), Num(2, 2, 2, 35)],
        [Num(7, 6, 3, 755), Num(9, 5, 3, 598)]]
    assert schema.gear_ratios() == 467835


def test_solution2_for_real():
    with open('test/day03.in') as data_file:
        schema = Schema.parse(data_file.read())
    assert schema.gear_ratios() == 76504829
