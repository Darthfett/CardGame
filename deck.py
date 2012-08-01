import random

class Deck:

    def add(self, card):
        self.cards.append(card)

    def __bool__(self):
        return bool(self.cards)

    def __str__(self):
        if self.cards:
            return '[' + ']['.join(map(str, self.cards)) + ']'
        else:
            return ''

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def __init__(self, cards=None):
        if cards is None:
            cards = []

        self.cards = cards

def load_deck(file_path):
    """Given a file path, load and return the deck."""
    with open(file_path, 'r') as deck_file:
        # Remove space from the file
        # Every character in the file excluding whitespace is a card
        cards = list(''.join(deck_file.read().split()))
        return Deck(cards)