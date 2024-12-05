import os
from helpers import Helpers

"-------------------------CREATE CLASS ------------------------------------------------------------------------------"


class ConsoleMain:
    """This class contains methods that are needed to print introduction infos to the game
    and to  structure terminal outputs. The class object is the game itself (no explicit constructor needed),
    with sole purpose of calling the methods."""

    "-------------------- methods for clearance and separations in UI (Pycharm terminal) -----------------------------"

    def print_separating_line(self):
        """Simple method to print a separating line."""
        print('_' * 105)

    def print_request_for_proceeding_then_clear_terminal(self):
        """Simple method to print a separated line, and ask for any user input (+ Enter) to proceed in game."""
        self.print_separating_line()
        input("[Press Enter to continue] >> ")
        self.clear_terminal()

    def clear_terminal(self):
        """Simple method to clear the terminal and create a header, when game is run in terminal."""
        os.system('cls')
        print('\n' + Helpers.formatted_text("POWERPALS - YOUR QUEST TO BEAT MASTER MAX!", bright=True))
        self.print_separating_line()

    "------------------- print-methods for basic game information---------------------------------------------------"

    def print_intro(self):
        """Simple method to print UI-recommendation and game introduction."""
        self.clear_terminal()
        print(Helpers.formatted_text("STRONG RECCOMENDATION: \n"
                    "\t - RUN GAME IN PYTHON TERMINAL (PYCHARM) FOR BETTER USER EXPERIENCE!\n"
                    "\t - Running the game in the console might have graphical side effects\n\n"
                            "WHEN RUNNING IN TERMINAL (PYCHARM):\n"
                     "\t - Undock the terminal window and drag its width to a value such that\n"
                    "\t   the WHITE LINES above and below the red text have no line breaks", "red"))
        self.print_request_for_proceeding_then_clear_terminal()
        print("Welcome, the game begins! Let\'s see, what this game is about:\n\n"
              "\t In this game, you are a "
              + Helpers.formatted_text("wanderer") + " possessing several powerpals.\n"
                "\t As you want to be the best of all, you want to "
              + Helpers.formatted_text("beat Master Max") +
              ", \n\t who is currently the greatest of all wanderers!\n"
              "\t On your way to gather the strength to beat Master Max, you will\n\t "
              + Helpers.formatted_text("encounter other wanderers") +
              "\n\t during the game. " + Helpers.formatted_text("Fight them"), "to become stronger!\n"
                "\t You can fight each wanderer you encounter.\n"
                "\t To find the wanderers, you have to "
              + Helpers.formatted_text("roam a map") + ". \n\tCareful: You only have "
              + Helpers.formatted_text("restricted sight")
              + ",so memorize, where you are going!\n")
        self.print_request_for_proceeding_then_clear_terminal()

    def print_map_introduction(self):
        """Simple method to print an introduction to the game map."""
        print("So far so good: Now let's have a look at what we will find in our little world! \n"
              "\t " + Helpers.formatted_text("???") + "\t This is "
              + Helpers.formatted_text("obscure terrain") + ". You have no sight here.\n"
                "\t " + Helpers.formatted_text("^.^",
                "blue") + "\t This is the symbol for "
              + Helpers.formatted_text("you - the player", "blue") + "!\n"
                "\t " + Helpers.formatted_text("[1]",
                "red") + "\t This is the symbol for an "
              + Helpers.formatted_text("opponent (wanderer)", "red")
              + " with " + Helpers.formatted_text("level 1", "red") + ".\n "
                "\t\t\t -> The number within the brackets shows the level. \n"
                "\t\t\t    Wanderers can have different levels\n"
                "\t\t\t -> Note: a wanderer with higher level will be more difficult to fight! \n"
                "\t\t\t    He has stronger powerpals!\n"
                "\t " + Helpers.formatted_text("Ò.Ó",
                "red") + "\t This is the final boss "
              + Helpers.formatted_text("Master Max", "red")
              + ".\n\t\t\t Don't you dare to fight him "
                "having a low level! He will screw you!\n"
                "\t " + Helpers.formatted_text("[+]",
                "green") + "\t This is the "
              + Helpers.formatted_text("nursery", "green")
              + ". You can heal your powerpal here (their health will be replenished)!\n\n")
        self.print_request_for_proceeding_then_clear_terminal()

    def print_game_rules(self):
        """Simple method to print game rules."""
        input("Ok. Now let's have a look at the game rules.\n"
              "[Press Enter to show the rules] >> ")
        print('\t1. You can roam the world using the keys '
              + Helpers.formatted_text("w", "blue") + ', '
              + Helpers.formatted_text("a", "blue") + ', '
              + Helpers.formatted_text("s", "blue") + ', '
              + Helpers.formatted_text("d", "blue")
              + '\n\t   Each time you move, you will be shown the options.\n'
                '\t2. When encountering an enemy (wanderer), you can choose if you want to '
              + Helpers.formatted_text("fight", "blue") + ' or '
              + Helpers.formatted_text("flight", "blue") + '.\n'
                '\t3. You ' + Helpers.formatted_text("lose") + ' a fight, '
                'when all of your powerpals are ' + Helpers.formatted_text(
            "defeated.")
              + '\n\t   You have to ' + Helpers.formatted_text("heal", "green")
              + ' your powerpals, once you are defeated.\n'
                '\t4. If you ' + Helpers.formatted_text("win") + ' a fight, '
                'you ' + Helpers.formatted_text("level up")
              + '.\n\t   Your powerpal will get higher health, attack and accuracy values.\n'
                '\t5. When you have ' + Helpers.formatted_text("defeated") + ' the final boss ('
              + Helpers.formatted_text("Ò.Ó", "red") + '), you have won the game.\n'
                 '\t6. You only see a small part of the map, so keep track if you find something!\n')
        self.print_request_for_proceeding_then_clear_terminal()

    def print_start_game(self):
        """Simple method to print start of the game."""
        print("We're ready to start the game! Let's play!\n")
        self.print_request_for_proceeding_then_clear_terminal()


"-------------------------CREATE CLASS OBJECT ------------------------------------------------------------------------"

game = ConsoleMain()
