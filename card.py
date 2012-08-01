"""
The Card class module provides a definition of what cards are.
"""

(CARD_TYPE_ENERGY,
 CARD_TYPE_NATURE,
 CARD_TYPE_SPIRIT) = range(3)

class Card:
    """
    A card has a type (energy/spirit/nature), power, and health,
    but vary greatly in what they do.
    """
    def __init__(self, type_, power, health):
        self.type_ = type_
        self.power = power
        self.health = health