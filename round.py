PHASE_COUNT = 4

(DRAW_PHASE,
 STRAT_PHASE,
 BAT_PHASE,
 END_PHASE) = range(PHASE_COUNT)

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
    n:    Go to next phase

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
NEXT_ACTIONS = {'n', 'next'}
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
    game.current_round = round
    game.current_phase = phase
    game.current_player = player

    phase_name = name_for_phase(phase)
    enemy = game.next_player(player)

    enemy_board = PLAYER_BOARD.format(*enemy.field)
    player_board = PLAYER_BOARD.format(*player.field)

    print(ROUND_ANNOUNCEMENT.format(round=round, phase=phase_name))

    print(BOARD.format(enemy_board=enemy_board, player_board=player_board))

    while True:
        action = input('Action? (help) ').strip()

        # Commands are case-insensitive, help is default.
        cmd = action.split()
        cmd[0] = cmd[0].lower()
        if not cmd:
            cmd = ['help']

        # Validate that action is good for current phase
        if cmd[0] in PHASE_ACTIONS and cmd[0] not in ACTIONS_FOR_PHASE[phase]:
            # Invalid action
            phases_for_action = [phase for phase in ACTIONS_FOR_PHASE if cmd[0] in ACTIONS_FOR_PHASE[phase]]
            print('Must be in {phase} phase to perform this action.\n'.format(phase=' phase OR '.join(map(name_for_phase, phases_for_action))))
            continue

        if cmd[0] in BOARD_ACTIONS:
            # Display board
            print(BOARD.format(enemy_board=enemy_board, player_board=player_board))
            continue

        if cmd[0] in DRAW_ACTIONS:
            # Draw card
            drawn_card = player.deck.draw()
            player.hand.add(drawn_card)
            print('Drew {card}\n'.format(card=card_name(drawn_card)))
            start_phase(game, round, STRAT_PHASE, player)
            return

        if cmd[0] in HAND_ACTIONS:
            # Display hand
            if player.hand:
                print(player.hand,'\n')
            else:
                print('No cards in hand\n')
            continue

        if cmd[0] in HELP_ACTIONS:
            # Display help message
            print(HELP_MSG)
            continue

        if cmd[0] in NEXT_ACTIONS:
            start_phase(game, round, (phase + 1) % PHASE_COUNT, player)
            return

        if cmd[0] in PLAY_ACTIONS:
            # Play card cmd[1] on field at cmd[2]
            try:
                card = cmd[1]
            except IndexError:
                print('Must select a card name and an empty spot on the field.\n')
                continue

            if card not in player.hand:
                print('No {c} card in hand.\n'.format(c=card_name(card)))
                continue

            try:
                field_cell = int(cmd[2])
            except (IndexError, ValueError):
                print('Must select a card name and an empty spot on the field.\n')
                continue

            try:
                current_field_card = player.field[field_cell]
            except IndexError:
                print('Field cell must be in range 0 <= cell <= 8.\n')
                continue

            if current_field_card != ' ':
                print('Spot on field is not empty.\n')
                continue

            # Successful play
            player.hand.remove(card)
            player.field[field_cell] = card
            player_board = PLAYER_BOARD.format(*player.field)
            print(BOARD.format(enemy_board=enemy_board, player_board=player_board))
            continue

        if cmd[0] in QUIT_ACTIONS:
            # Quit game
            print("Thanks for playing!\n")
            break

        print('Unknown command {cmd}\n'.format(cmd=cmd[0]))
