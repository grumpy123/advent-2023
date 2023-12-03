import re
from collections import defaultdict, namedtuple

Balls = namedtuple('Balls', ['red', 'green', 'blue'])


class Game:
    game_re = re.compile(r'^Game (\d+)\:(.*)$')

    def __init__(self, num, runs):
        self.num = num
        self.runs = runs

    @staticmethod
    def parse(game_str):
        m = Game.game_re.match(game_str)
        game_num = int(m.group(1))
        game_runs_str = m.group(2)
        game_runs = [Game.parse_run(run) for run in game_runs_str.split(';') if run and run.strip()]

        return Game(game_num, game_runs)

    @staticmethod
    def parse_run(run_str):
        color_nums = defaultdict(int)
        run_str = run_str.strip()
        for color in run_str.split(','):
            num, name = color.split()
            color_nums[name] = int(num)
        return Balls(color_nums['red'], color_nums['green'], color_nums['blue'])

    def is_possible(self, balls):
        for run in self.runs:
            if run.red > balls.red or run.green > balls.green or run.blue > balls.blue:
                return False

        return True

    def min_set(self):
        red, green, blue = 0, 0, 0
        for run in self.runs:
            red = max(red, run.red)
            green = max(green, run.green)
            blue = max(blue, run.blue)
        return Balls(red, green, blue)

    def power(self):
        min_set = self.min_set()
        return min_set.red * min_set.blue * min_set.green


def parse_games(str_games):
    return [Game.parse(game) for game in str_games.splitlines() if game]


def are_possible(games, balls):
    return [game.is_possible(balls) for game in games]


def possible_sum(games, balls):
    return sum(game.num for game in games if game.is_possible(balls))


def total_power(games):
    return sum(game.power() for game in games)
