import field
import player
import round
import deck
import card

class Game:

    def next_player(self, player):
        index = self.players.index(player)
        index = (index + 1) % len(self.players)
        return self.players[index]

    def start(self):
        self.cur_round = 0
        self.cur_phase = round.DRAW_PHASE
        self.cur_player = self.players[0]
        round.start_phase(self, self.cur_round, self.cur_phase, self.cur_player)

    def __init__(self, players, cur_round=0, cur_phase=None, cur_player=None):
        self.cur_round = cur_round
        self.cur_phase = cur_phase
        self.cur_player = cur_player
        self.players = players

def create_game(num_players):
    card.Card("Imp", 2, 4, 0, 0, 1)
    card.Card("Peasant", 3, 3, 0, 1, 0)
    card.Card("Golem", 1, 7, 1, 0, 0)
    card.Card("Knight", 5, 5, 0, 2, 0)

    deck_ = deck.load_deck('decks/default_deck.txt')
    players = [player.Player(deck_) for _ in range(2)]
    return Game(players)

if __name__ == '__main__':
    game = create_game(2)
    for p in game.players:
        p.deck.shuffle()
    game.start()