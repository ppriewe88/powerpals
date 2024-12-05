from console import game
from map import map_basis
import class_wanderer as tr

'-----------Print introduction infos and get player name ----------------------------------------------------------'
game.print_intro()
tr.wanderer_player.get_player_name()
tr.wanderer_player.print_player_stats()
game.print_map_introduction()
game.print_game_rules()
game.print_start_game()

'-----------Game begins. Running until "quit" is returned or boss is defeated -----------'
while True:

    # step 1 -  define next move's directions (or quit)
    next_move = map_basis.get_movement_directions()
    if next_move == "quit":
        print("You quit the game! See you next time!")
        break
    else:
        row_step, column_step = next_move

    # step 2 - move on map according to defined direction. Store outcome of move
    move_outcome = map_basis.move_on_map(stepsize_row=row_step, stepsize_column=column_step)

    # step 3 -Depending on the outcome of the move, act as follows:
    ### case outcome is nursery
    if move_outcome == "nursery (not walkable)":
        tr.wanderer_player.heal_wanderers_powerpal()
        game.print_request_for_proceeding_then_clear_terminal()
    ### case outcome is an opponent (opponent id)
    if type(move_outcome) == int:
        opposing_wanderer_id = move_outcome
        fight_outcome = tr.wanderer_player.fight_wanderer(tr.Wanderer.find_wanderer(opposing_wanderer_id))
        # subcase final boss was defeated
        if fight_outcome == "Master Max defeated":
            print("\nYOU WON THE GAME!")
            break
        # subcase fight was lost, was fled, or could not be entered
        elif fight_outcome in ("fight lost", "no fight", "flight"):
            game.print_request_for_proceeding_then_clear_terminal()
        # subcase "regular" opponent (not final boss) was defeated
        elif type(fight_outcome) == int:
            map_basis.remove_opponent_wanderer_from_map(fight_outcome)
