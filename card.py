"""
The Card class module provides a definition of what cards are.
"""

(ALIGNMENT_NEUTRAL,
 ALIGNMENT_ENERGY,
 ALIGNMENT_NATURE,
 ALIGNMENT_SPIRIT) = range(4)

def name_for_card(card):
    return {
        'I': "Imp",
        'P': "Peasant",
        'G': "Golem",
        'K': "Knight"
    }[card]

class CardType(type):

    def __contains__(cls, item):
        return item in cls.prototypes

    def __getitem__(cls, index):
        if len(index) == 1:
            index = name_for_card(index)
        return cls.prototypes[index]

    def __setitem__(cls, index, value):
        cls.prototypes[index] = value

class Card(metaclass=CardType):
    """
    A card has a type (e.g. Imp or Golem), power, health,
    and alignment in energy/spirit/nature.
    """

    prototypes = {}

    def __repr__(self):
        return self.name[0]

    @property
    def alignment(self):
        alignments = [self.energy, self.nature, self.spirit]
        max_ = max(alignments)
        if alignments.count(max_) > 1:
            return ALIGNMENT_NEUTRAL

    @property
    def name(self):
        return self.prototype.prototype

        return alignments.index(max_) + 1 # Convert to ALIGNMENT_

    def __init__(self, prototype, power=None, health=None, energy=None, nature=None, spirit=None):
        if isinstance(prototype, str):
            if prototype not in Card:
                Card[prototype] = self
            else:
                prototype = Card[prototype]
        elif not isinstance(prototype.prototype, str):
            raise ValueError("Prototype must be an actual prototype")

        if power is None:
            power = prototype.power
        if health is None:
            health = prototype.health
        if energy is None:
            energy = prototype.energy
        if nature is None:
            nature = prototype.nature
        if spirit is None:
            spirit = prototype.spirit

        self.prototype = prototype
        self.power = power
        self.health = health
        self.energy = energy
        self.nature = nature
        self.spirit = spirit