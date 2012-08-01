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

HELP_MSG = (
"""
Available commands are:
    d:    Draw card
    p:    Play card

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

BOARD_ACTIONS = {'b', 'board'}
DRAW_ACTIONS = {'d', 'draw'}
HAND_ACTIONS = {'h', 'hand'}
HELP_ACTIONS = {'', 'help'}
PLAY_ACTIONS = {'p', 'play'}
QUIT_ACTIONS = {'q', 'quit', 'exit'}

ACTIONS_FOR_PHASE = {
    DRAW_PHASE: DRAW_ACTIONS,
    STRAT_PHASE: PLAY_ACTIONS,
    BAT_PHASE: {},
    END_PHASE: {},
}

PHASE_ACTIONS = set.union(*ACTIONS_FOR_PHASE.values())

def start_phase(game, round, phase, player):

    phase_name = name_for_phase(phase)
    enemy = game.next_player(player)

    enemy_board = PLAYER_BOARD.format(*enemy.field)
    player_board = PLAYER_BOARD.format(*player.field)

    print(ROUND_ANNOUNCEMENT.format(round=round, phase=phase_name))

    print(BOARD.format(enemy_board=enemy_board, player_board=player_board))

    while True:
        action = input('Action? (help) ').lower().strip()

        # Validate that action is good for current phase
        if action in PHASE_ACTIONS and action not in ACTIONS_FOR_PHASE[phase]:
            # Invalid action
            phases_for_action = [phase for phase in ACTIONS_FOR_PHASE if action in ACTIONS_FOR_PHASE[phase]]
            print('Must be in {phase} phase to perform this action.\n'.format(phase=' phase OR '.join(map(name_for_phase, phases_for_action))))
            continue

        if action in BOARD_ACTIONS:
            # Display board
            print(BOARD.format(enemy_board=enemy_board, player_board=player_board))
            continue

        if action in DRAW_ACTIONS:
            # Draw card
            drawn_card = player.deck.draw()
            player.hand.add(drawn_card)
            print('Drew {card}\n'.format(card=card_name(drawn_card)))
            start_phase(game, round, STRAT_PHASE, player)
            return

        if action in HAND_ACTIONS:
            # Display hand
            if player.hand:
                print(player.hand,'\n')
            else:
                print('No cards in hand\n')
            continue

        if action in HELP_ACTIONS:
            # Display help message
            print(HELP_MSG)
            continue

        if action in QUIT_ACTIONS:
            # Quit game
            print("Thanks for playing!\n")
            break

        print('Unknown command {cmd}\n'.format(cmd=action))
