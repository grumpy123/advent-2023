from textwrap import dedent

from day04 import Game, Card


def test_example():
    game = Game.parse(dedent('''
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    '''))
    assert game.cards[0] == Card(1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    assert game.cards[1] == Card(2, {13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19})
    assert game.cards[0].score1() == 8
    assert game.score1() == 13


def test_solution1_for_real():
    with open('test/day04.in') as data_file:
        game = Game.parse(data_file.read())
    assert game.score1() == 21138


def test_solution2():
    game = Game.parse(dedent('''
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    '''))
    assert game.cards[0].score2() == 4
    assert game.cards[1].score2() == 2

    assert game.score2() == 30


def test_solution2_for_real():
    with open('test/day04.in') as data_file:
        game = Game.parse(data_file.read())
    assert game.score2() == 7185540
