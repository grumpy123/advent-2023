from textwrap import dedent

from day02.day02 import parse_games, are_possible, Game, Balls, possible_sum, total_power


def test_game_parse():
    game = Game.parse('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert game.num == 1
    assert game.runs == [
        Balls(4, 0, 3),
        Balls(1, 2, 6),
        Balls(0, 2, 0),
    ]


def test_are_possible():
    games = parse_games(dedent('''
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    '''))
    balls = Balls(12, 13, 14)
    assert are_possible(games, balls) == [True, True, False, False, True]


def test_possible_sum():
    games = parse_games(dedent('''
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    '''))
    balls = Balls(12, 13, 14)
    assert possible_sum(games, balls) == 8


def test_possible_sum_for_real():
    with open('test/day02/input.txt') as data_file:
        games = parse_games(data_file.read())
    balls = Balls(12, 13, 14)
    assert possible_sum(games, balls) == 2285


def test_min_set_and_power():
    games = parse_games(dedent('''
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    '''))
    assert games[0].min_set() == Balls(4, 2, 6)
    assert games[0].power() == 48
    assert total_power(games) == 2286


def test_power_for_real():
    with open('test/day02/input.txt') as data_file:
        games = parse_games(data_file.read())
    assert total_power(games) == 77021
