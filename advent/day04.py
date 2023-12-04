import re


class Card:
    card_re = re.compile(r'^Card\s+(\d+)\:(.+)\|(.+)$')

    def __init__(self, num, winners, numbers):
        self.num = num
        self.winners = set(winners)
        self.numbers = set(numbers)

    @staticmethod
    def parse(card_str):
        m = Card.card_re.match(card_str)
        num = int(m.group(1))
        winners = {int(n) for n in m.group(2).strip().split()}
        numbers = {int(n) for n in m.group(3).strip().split()}

        return Card(num, winners, numbers)

    def score1(self):
        overlap = self.winners.intersection(self.numbers)
        if not overlap:
            return 0
        return pow(2, len(overlap) - 1)

    def score2(self):
        overlap = self.winners.intersection(self.numbers)
        return len(overlap)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.num == other.num and self.winners == other.winners and self.numbers == other.numbers

    def __str__(self):
        return f'Game({self.num}, {self.winners}, {self.numbers})'

    def __repr__(self):
        return str(self)


class Game:
    def __init__(self, cards):
        self.cards = cards

    @staticmethod
    def parse(cards_str):
        cards = []
        for card_str in cards_str.strip().splitlines():
            if not card_str:
                continue
            card = Card.parse(card_str)
            cards.append(card)

        return Game(cards)

    def score1(self):
        return sum(card.score1() for card in self.cards)

    def score2(self):
        mul = [1] * len(self.cards)
        for i, card in enumerate(self.cards):
            for j in range(i + 1, i + 1 + card.score2()):
                mul[j] += mul[i]

        return sum(mul)
