import string

digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def _code_from_line(line):
    digits = [d for d in line if d in string.digits]
    return int(digits[0] + digits[-1])


def recover(scrambled):
    return [_code_from_line(line) for line in scrambled.splitlines() if line]


def recover_crc(scrambled):
    return sum(recover(scrambled))


def digit(text):
    if text[:1].isdigit():
        return int(text[:1])

    for i, digit in enumerate(digit_words):
        if text.startswith(digit):
            return int(i + 1)


def _first_digit2(line):
    for i in range(len(line)):
        v = digit(line[i:])
        if v:
            return v
    return None


def _last_digit2(line):
    for i in range(len(line)):
        start = len(line) - 1 - i
        v = digit(line[start:])
        if v:
            return v
    return None


def _code_from_line2(line):
    return 10 * _first_digit2(line) + _last_digit2(line)


def recover2(scrambled):
    return [_code_from_line2(line) for line in scrambled.splitlines() if line]


def recover_crc2(scrambled):
    return sum(recover2(scrambled))
