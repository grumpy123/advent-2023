"""
Will:
 1. Find all numbers in the input and their start and end positions
 2. Calculate their surrounding points as list of coordinates
 3. Find all numbers that are not surrounded by any symbols

To parse the input:
 1. Use regex to find all the numbers and their start and end positions
"""

from collections import namedtuple, defaultdict

Num = namedtuple('Num', ['line', 'col', 'size', 'value'])


class Schema:
    def __init__(self, lines):
        self.lines = lines
        self.nums = self._find_nums()

    def _find_nums(self):
        nums = []
        for line_num, line in enumerate(self.lines):
            n = 0
            for i, c in enumerate(line):
                if c.isdigit():
                    n += 1
                    continue
                if n:
                    nums.append(Num(line_num, i - n, n, int(line[i - n:i])))
                    n = 0
            if n:
                nums.append(Num(line_num, self.width - n, n, int(line[self.width - n:])))

        return nums

    @staticmethod
    def parse(schema):
        return Schema(schema.strip().splitlines())

    def at(self, line, col):
        return self.lines[line][col]

    @property
    def width(self):
        return len(self.lines[0])

    @property
    def height(self):
        return len(self.lines)

    def has_symbol_neighbor(self, num):
        left = max(0, num.col - 1)
        right = min(self.width, num.col + num.size + 1)
        top = max(0, num.line - 1)
        bottom = min(self.height, num.line + 2)
        for line in range(top, bottom):
            for col in range(left, right):
                if self.at(line, col) != '.' and not self.at(line, col).isdigit():
                    return True
        return False

    def solution(self):
        return sum(num.value for num in self.nums if self.has_symbol_neighbor(num))

    def gears(self):
        gears = defaultdict(list)
        for num in self.nums:
            left = max(0, num.col - 1)
            right = min(self.width, num.col + num.size + 1)
            top = max(0, num.line - 1)
            bottom = min(self.height, num.line + 2)
            for line in range(top, bottom):
                for col in range(left, right):
                    if self.at(line, col) == '*':
                        gears[(line, col)].append(num)
        return [nums for coord, nums in gears.items() if len(nums) == 2]

    def gear_ratios(self):
        return sum(g1.value * g2.value for (g1, g2) in self.gears())
