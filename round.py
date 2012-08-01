(DRAW_PHASE,
 STRAT_PHASE,
 BAT_PHASE,
 END_PHASE) = range(4)

PLAYER_BOARD = (
"""
[{0}][{1}][{2}]
[{3}][{4}][{5}]
[{6}][{7}][{8}]
""").strip()

BOARD = (
"""
{enemy_board}
---------
{player_board}
""").lstrip()

ROUND_ANNOUNCEMENT = (
"""
==== ROUND {round} ====
Beginning {phase} Phase
""").lstrip()

HELP = (
"""
Available commands are:
    help: Show this message
    d:    Draw card
    b:    Show board
    h:    Show hand
    q:    Quit
""").lstrip()

def name_for_phase(phase):
    return {
        DRAW_PHASE: "Draw",
        STRAT_PHASE: "Strat",
        BAT_PHASE: "Battle",
        END_PHASE: "End"
    }[phase]

def card_name(card):
    return {
        'I': "Imp",
        'P': "Peasant",
        'G': "Golem",
        'K': "Knight"
    }[card]

def start_phase(game, round, phase, player):

    phase_name = name_for_phase(phase)
    enemy = game.next_player(player)

    enemy_board = PLAYER_BOARD.format(*enemy.field)
    player_board = PLAYER_BOARD.format(*player.field)

    print(ROUND_ANNOUNCEMENT.format(round=round, phase=phase_name))

    print(BOARD.format(enemy_board=enemy_board, player_board=player_board))

    while True:
        action = input('Action? (help) ').lower().strip()
        if action in {'help', ''}:
            print(HELP)
            continue
        if action in {'hand', 'h'}:
            if player.hand:
                print(player.hand)
            else:
                print('No cards in hand\n')
            continue
        if action in {'b', 'board'}:
            print(BOARD.format(enemy_board=enemy_board, player_board=player_board))
            continue
        if action in {'q', 'quit', 'exit'}:
            break
        if action in {'d', 'draw'} and phase == DRAW_PHASE:
            drawn_card = player.deck.draw()
            player.hand.add(drawn_card)
            print('Drew {card}'.format(card=card_name(drawn_card)))
            start_phase(game, round, STRAT_PHASE, player)
            return

        print('Unknown command {cmd}'.format(cmd=action))
