import field
import deck

class Player:
    def __init__(self, deck_=None):
        if deck_ is None:
            deck_ = deck.Deck()

        self.field = field.Field(field.FIELD_WIDTH, field.FIELD_HEIGHT)
        self.deck = deck_
        self.hand = deck.Deck()