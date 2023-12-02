from textwrap import dedent

from day01.day01 import recover, recover_crc, recover2, recover_crc2


def test_recover():
    scrambled = dedent('''
        1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet
    ''')

    assert recover(scrambled) == [12, 38, 15, 77]
    assert recover_crc(scrambled) == 142


def test_recover2():
    scrambled = dedent('''
        two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen
    ''')

    assert recover2(scrambled) == [29, 83, 13, 24, 42, 14, 76]
    assert recover_crc2(scrambled) == 281


def test_recover_for_real():
    with open('test/day01/input.txt') as data_file:
        scrambled_text = data_file.read()
    assert recover_crc(scrambled_text) == 53334


def test_recover_for_real2():
    with open('test/day01/input.txt') as data_file:
        scrambled_text = data_file.read()
    assert recover_crc2(scrambled_text) == 52834
