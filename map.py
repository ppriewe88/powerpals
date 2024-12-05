import numpy as np
from functools import reduce
import console
from helpers import Helpers, input_for_get_movement_directions

"-------------------------CREATE CLASS ------------------------------------------------------------------------------"


class Map:
    """This class contains a constructor for the game map (as class object), a method to generate a
    string representation of it, and several methods to change the map object (move player positions, remove wanderers).
    The methods contained either return information from the map (e.g. player's position), change content of the map,
    or print string versions of the map"""

    "------------------------constructor and string representation------------------------------------------------"

    def __init__(self, content: np):
        """This is the constructor for a map object.
        :param: self; content (str): to fill the map;
        row_size as number of rows of the map; column_size as number of columns of the map;
        row_size and column_size are determined using a numpy method when creating the class object.
        :return: class object"""
        self.content = content
        self.row_size, self.column_size = self.content.shape

    def __str__(self):
        """This method creates a string representation of a map object (using the attribute self.content)!
        Within the method's execution, the (human) player's position on the map object is determined.
        The characters of the printed string version of the map will be generated
        according to the entries of the Map object's content (numpy-array in attribute self.content).
        Visible and invisible areas will be determined according to the player's position.
        :param: self
        :return: str: larger string for visually appealing print of the map"""

        # find player position to later determine visible area
        row_player, column_player = self.find_player_position()

        # create row-strings, set chars according to content and visible radius!
        rows_as_strings = []
        for row_number in range(0, self.row_size):
            row_chars = []
            # start mapping integers on characters; if out of visible range, place "???"
            if row_number > row_player + 2 or row_number < row_player - 2:
                row_chars = map(lambda coord: '???', self.content[row_number])
            else:
                for char_idx in range(0, len(self.content[row_number])):
                    if char_idx < column_player - 2 or char_idx > column_player + 2:
                        row_chars.append('???')
                    else:
                        if self.content[row_number, char_idx] in (0, 8):
                            row_chars.append('   ')
                        elif self.content[row_number, char_idx] == 1:
                            row_chars.append('▓▓▓')
                        elif self.content[row_number, char_idx] == 2:
                            row_chars.append(Helpers.formatted_text('^.^', "blue"))
                        elif self.content[row_number, char_idx] == 3:
                            row_chars.append(Helpers.formatted_text('[1]', "red"))
                        elif self.content[row_number, char_idx] == 4:
                            row_chars.append(Helpers.formatted_text('[2]', "red"))
                        elif self.content[row_number, char_idx] == 5:
                            row_chars.append(Helpers.formatted_text('[3]', "red"))
                        elif self.content[row_number, char_idx] == 6:
                            row_chars.append(Helpers.formatted_text('Ò.Ó', "red"))
                        else:
                            row_chars.append(Helpers.formatted_text('[+]', "green"))

            # reduce each row to a single string and append to list of rows (each list element being a string)
            row_string = reduce(lambda string1, string2: str(string1) + str(string2), row_chars)
            rows_as_strings.append('    ' + str(row_string))

        # concatenate all rows of the list
        map_as_string = reduce(lambda row_string1, row_string2: row_string1 + '\n' + row_string2, rows_as_strings)
        return map_as_string

    '-----------------------method to get movement-directions from user------------------------------------------------'

    def get_movement_directions(self) -> tuple or str:
        """This method gets validated userinput from the user: "w", "a", "s", "d" (or "quit")
        for directions of row-wise/column-wise movement on the map (or to leave game).
        Output is a tuple of integers (+-1, +-1) to move in row/column direction.
        If user wants to quit, method returns string "quit"
        :param: self
        :return: tuple (row-step, column-step) or str: directions for movement (int), or "quit" (str) to leave game
        """

        console.game.clear_terminal()
        print('')
        print(str(self))

        # get directions as validated user input
        user_input = input_for_get_movement_directions.validated_input()
        if user_input == "quit":
            return "quit"
        console.game.print_separating_line()

        # transform input to row-wise/column-wise steps
        row_step = 0
        column_step = 0
        if user_input.casefold() == "w":
            row_step -= 1
        elif user_input.casefold() == "a":
            column_step -= 1
        elif user_input.casefold() == "s":
            row_step += 1
        elif user_input.casefold() == "d":
            column_step += 1

        return row_step, column_step

    "--------methods for movement and player positions on map object -------------------------------------------------"

    # method to find player on map by given id
    def find_player_position(self, player_id: int = 2) -> tuple:
        """This method finds a player on the map by the given input id (int) of a wanderer object.
        Default: id = 2 (the human player's wanderer's id). It returns his position.
        :param: self; player_id (int): wanderer's id
        :return: (tuple): position of player"""
        player_position = ()
        for row in range(0, self.row_size):
            for column in range(0, self.column_size):
                if self.content[row, column] == player_id:
                    player_position = (row, column)
        return player_position

    # method to move player's position on map
    def move_on_map(self, stepsize_row: int, stepsize_column: int) -> str or int:
        """This method moves the player on the map.
        It gets a movement as input, and checks, if the position is walkable from the current position
        (i.e. no wall, no opponent wanderer, no nursery on it, destination on map).
        It returns, if the desired position is walkable or not walkable,
        and (if found) the opponent wanderer's id (id of wanderer object)
        :param: self; stepsize_row (int), stepsize_column (int): These define the direction of the step on the map.
        :return: (str or int): containing info about outcome of move (several cases possible)"""

        # find current position of player
        current_row, current_column = self.find_player_position()

        # calc new position of player
        new_row = current_row + stepsize_row
        new_column = current_column + stepsize_column

        # check if desired position is in map (in order to not cross the map's borders)
        # If not, don't walk and return
        if new_row >= self.row_size or new_column >= self.column_size:
            return "out of map"
        else:
            # in this case: desired position IS on map!
            # check the following cases of NON-walkable destinations:
            if self.content[new_row, new_column] == 1:
                # hitting a wall; do not walk
                return "wall (not walkable)"
            elif self.content[new_row, new_column] == 7:
                # nursery found
                print("You reached the " + Helpers.formatted_text("nursery", "green")
                      + "! You can refresh your powerpal's health here.")
                console.game.print_request_for_proceeding_then_clear_terminal()
                return "nursery (not walkable)"
            elif self.content[new_row, new_column] in (3, 4, 5, 6):
                # opponent found
                print("You are facing an " + Helpers.formatted_text("opponent", "red") + "!")
                found_opponent_wanderer = self.content[new_row, new_column]
                return int(found_opponent_wanderer)
            # else-case: destination is walkable
            else:
                # reset current position to 0
                self.content[current_row, current_column] = 0
                # set new position to 2 (player's id)
                self.content[new_row, new_column] = 2
                return "move was made (walkable)"

    # method to remove opponent wanderer (id) from map
    def remove_opponent_wanderer_from_map(self, opponent_wanderer_id: int) -> None:
        """This method removes a wanderer id from the map object's attribute "content" (numpy array)
        (more precisely: it replaces his number with a 0 in self.content of the map object)
        :param: self; opponent_wanderer_id (int): number that has to be removed
        :return: None"""
        opponent_row, opponent_column = map_basis.find_player_position(opponent_wanderer_id)
        map_basis.content[opponent_row, opponent_column] = 0


"-------------------------CREATE CLASS OBJECT-------------------------------------------------------------------------"

# set up rows and columns in array
# 1 = wall; 2 = player (start); 3,4,5,6 = rival, 7 = nursery
map_basis = Map(np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 4, 1, 1, 0, 1, 1, 0, 7, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 3, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1]
]))
