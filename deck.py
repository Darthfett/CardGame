import random
import operator as op
import card

class Deck:

    def remove(self, card):
        self.cards.remove(card)

    def add(self, card):
        self.cards.append(card)

    def __bool__(self):
        return bool(self.cards)

    def __str__(self):
        if self.cards:
            return '[' + ']['.join(map(repr, self.cards)) + ']'
        else:
            return ''

    def get(self, card_):
        return next((c for c in self.cards if repr(c) == card_ or repr(c) == card.name_for_card(card_)), None)

    def __contains__(self, card_):
        return any(repr(c) == card_ for c in self.cards)

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

        cards = [card.Card(card.Card[card.name_for_card(card_)]) for card_ in cards]

        return Deck(cards)