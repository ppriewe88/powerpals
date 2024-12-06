from colorama import Fore, Style


"-------------------------CREATE CLASS ------------------------------------------------------------------------------"


class Helpers:
    """This class contains helper methods to format print outputs and validate inputs.
    Class objects contain strings for input requests.
    The class contains a constructor for class objects, a formatting (static) method for texts,
    and a method to validate user inputs (on a given list of possible inputs)"""


    "------------------------constructor---------------------------------------------------------"

    def __init__(self, input_request: str, possible_inputs: list = []):
        """Constructor for class objects."""
        self.input_request = input_request
        self.possible_inputs = possible_inputs

    "------------------------static method for formatting text------------------------------------"

    @staticmethod
    def formatted_text(text: str, color: str = "regular", bright: bool = True) -> str:
        """This method serves as a helper for any text parts that need to be printed in color or bright.
        It has the sole purpose of coloring and styling strings for the game's print outputs and uses colorama functionalities.
        The standard colorama colors are allowed, as well as the style "bright" (which is the default style of this method).
        :param: self; text (str): input to be formatted; color (str): desired color of output, default white;
        bright (bool): bright or not, default True
        :return: (str) colorized and styled text"""

        possible_colors = {'red': Fore.RED, 'green': Fore.GREEN, 'yellow': Fore.YELLOW, 'blue': Fore.BLUE,
                           'black': Fore.BLACK, 'cyan': Fore.CYAN, 'magenta': Fore.MAGENTA}

        if color != "regular" and color not in list(possible_colors.keys()):
            raise ValueError("Wrong color input in formatting function formatted_text!")

        if color == "regular":
            if bright:
                return Style.BRIGHT + text + Style.RESET_ALL
            else:
                return text
        else:
            output_color = possible_colors.get(color.lower())
            if bright:
                return output_color + Style.BRIGHT + text + Style.RESET_ALL
            else:
                return output_color + text + Style.RESET_ALL

    "---------------------------- method to validate user inputs-----------------------------------------"
    def validated_input(self, other_input_criteria: list = []) -> str:
        """This method is called anywhere, where an input has to be validated, i.e. only a fix set of inputs is allowed.
        It returns a validated input validated via the given set, or a message, that input was not valid.
        :param: self (class object)
        :return: (str): validated input"""
        validated_input = ''

        if other_input_criteria:
            input_criteria_to_check = other_input_criteria
        else:
            input_criteria_to_check = self.possible_inputs

        print(self.input_request)
        valid_input = False
        while not valid_input:
            validated_input = input(">> ")
            if validated_input.casefold() in input_criteria_to_check:
                valid_input = True
            else:
                print("No valid input! Try again and see the "
                      + Helpers.formatted_text("colored options", "blue") + " above!")
        return validated_input.casefold()




"-------------------------CREATE CLASS OBJECTS------------------------------------------------------------------------"


input_for_get_movement_directions = Helpers("\nWhere do you want to move next?\n[Type "
                    + Helpers.formatted_text("w", "blue") + ' (up), '
                    + Helpers.formatted_text("a", "blue") + ' (left), '
                    + Helpers.formatted_text("s", "blue") + ' (down), '
                    + Helpers.formatted_text("d", "blue") + ' (right), '
                    + 'or ' + Helpers.formatted_text("quit", "blue")
                    + ' (quit game). Finish by pressing Enter]',
                                            ["w","a","s","d", "quit"])
input_for_fight_decision = Helpers('[Type ' + Helpers.formatted_text("fight", "blue") + ' or '
                        + Helpers.formatted_text("flight", "blue") + ' and press Enter]',
                                   ["fight", "flight"])
input_for_choose_undefeated_powerpal = Helpers("\nEnter the id of the powerpal you want to send into the fight!\n"
              "[Type " + Helpers.formatted_text("id", "blue") + ", press Enter] >> ")

input_for_powerduel_determine_attack_mode = Helpers('\nWhich attack do you want to use?\n[Type '
                                                    + Helpers.formatted_text("l", "blue")
                                                    + ' = light attack, '
                                                    + Helpers.formatted_text("h", "blue")
                                                    + ' = heavy attack or '
                                                    + Helpers.formatted_text("flight", "blue")
                                                    + ' to run for your life, then Enter] >> ',
                                                    ["l", "h", "flight"])
input_for_heal_wanderers_powerpal = Helpers("Do you want to heal your powerpals?\n"
              "[Type " + Helpers.formatted_text("yes", "blue") + " to heal or "
                        + Helpers.formatted_text("no", "blue") + " to not heal, then press Enter] ",
                                          ["yes", "no"])
