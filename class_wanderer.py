import class_powerpal as pk
import powerpal_art as pk_art
import console
import random as rn
from helpers import (Helpers, input_for_fight_decision,
                     input_for_choose_undefeated_powerpal, input_for_pokeduel_determine_attack_mode,
                     input_for_heal_wanderers_powerpal)

"-------------------------CREATE CLASS ------------------------------------------------------------------------------"


class Wanderer:
    """This class contains:
     - a constructor for wanderers (class objects) and a string representation
     - some basic methods for basic information of the class objects
     - some helping method for a fight between wanderers (the "outer" fight method)
     - the "outer" fight method itself (calling the "inner" fight method pokeduel_main
     - the "inner" fight method and a helping method
     - two "post-fight" methods to level up and heal powerpal at the nursery
    """

    "------------------------ constructor and string representation------------------------------------------------"

    # constructor
    def __init__(self, name: str, id: int, level: int = 0, powerpal_list: list = []):
        """This is the constructor for class objects.
        :param: several parameters to define the attributes.
        For more info on the parameters/attributes, see attributes in code of this constructor.
        :return: class object
        """
        self.name = name
        self.id = id
        self.level = level
        self.powerpal_list = powerpal_list

    # string version of wanderer objects
    def __str__(self):
        """This method returns a string representation of a class object.
        :param: self
        :return: str: formatted string with class object data"""
        if self.id == 1:
            output_color = "blue"
        else:
            output_color = "red"
        wanderer_info = (f'Name: {Helpers.formatted_text(self.name, output_color)}\n'
                        f'Level: {Helpers.formatted_text(str(self.level), output_color)}\n'
                        f'The following powerpals are with {self.name}:\n')
        for powerpal in self.powerpal_list:
            wanderer_info += "\t" + Helpers.formatted_text(str(powerpal)) + '\n'
        return wanderer_info

    "------------------------- Basic methods to set/return basic information on class objects -----------------------"

    # method to get the player's name
    def get_player_name(self):
        """This method gets the player's name via input and stores it in the corresponding class object"""
        self.name = input("Ok! Now, please enter the name for your player >> ")

    # method to print the player's stats
    def print_player_stats(self):
        """This method prints information about the wanderer (class object)"""
        print("Alright, have a look at your player stats:\n")
        print(str(self))
        console.game.print_request_for_proceeding_then_clear_terminal()

    "------------------------- Helping methods for the fight methods------------------------------------------------"
    @staticmethod
    # method to return a wanderer (class object) by his id
    def find_wanderer(input_id: int) -> "Wanderer":
        """This method returns a wanderer object for a given wanderer id (int)
        :param: input_id (int): id, for which we search the wanderer object
        :return: object of class wanderer"""
        for wanderer in wanderer_list:
            if wanderer.id == input_id:
                return wanderer

    # method to decide if fight or flight (when encountering opposing wanderer)
    def fight_decision(self, wanderer_opponent: "Wanderer") -> str:
        """This method generates a printed introduction to a fight.
        It lets the player decide if the fight will start or not.
        If no healthy powerpal (undefeated) are available, return respectively.
        :param: self; wanderer_opponent (object of class wanderer)
        :return: string - ('can not enter'), ('fight') or ('flight')"""

        # no fight possible if no healthy powerpal available
        if self.undefeated_powerpals() == 0:
            return "can not enter fight"

        # intro to opponent
        input(f"\nIt is {Helpers.formatted_text(wanderer_opponent.name, "red")}!\n"
              f"[Press enter to see your and your opponent's stats] >> ")
        console.game.clear_terminal()
        print(str(self), '\n')
        print(str(wanderer_opponent), '\n')

        # get validated user input to decide if fight or flight
        print('Do you want to fight or flight?')
        console.game.print_separating_line()
        fight_or_flight = input_for_fight_decision.validated_input()
        return fight_or_flight

    # method to print intro to fight
    def fight_intro(self, wanderer_opponent: "Wanderer") -> None:
        """This method simply prints a short introduction to the fight
        :param: self (wanderer object), wanderer_opponent (wanderer object)
        :return: None"""
        print(f"You want to fight - that's the spirit!\n\n"
              f"{Helpers.formatted_text(wanderer_opponent.name, "red")}: Wanna fight? I'm gonna CRUSH you!!\n")
        console.game.print_request_for_proceeding_then_clear_terminal()
        print("Rules:"
              "\n - Your powerpal can ALWAYS use a " + Helpers.formatted_text("LIGHT", "blue") + " attack."
                    "\n - Your powerpal can use a " + Helpers.formatted_text(
            "HEAVY", "blue") + " attack only TWICE on each opposing powerpal"
                    "\n\t - This means:\n\t   For each new powerpal the opponent sends to fight, you can use exactly two heavy attacks!"
                    "\n\t - " + Helpers.formatted_text("Careful: You miss more often with heavy attacks!"))
        console.game.print_request_for_proceeding_then_clear_terminal()

    # method to count undefeated powerpal of player
    def undefeated_powerpals(self) -> int:
        """This method counts undefeated powerpals (using the attribute "defeated" of the powerpal
        in the wanderer's attribute powerpal_list), that are still available for fight.
        :param: self
        :return: int"""
        alive_powerpal = 0
        for powerpal in self.powerpal_list:
            if not powerpal.defeated:
                alive_powerpal += 1
        return alive_powerpal

    # method to choose undefeated powerpal
    def choose_undefeated_powerpal(self):
        """This method lets the player choose an undefeated powerpal from the player's wanderer's list of powerpal.
        Undefeated means, that the selected powerpal's attribute "defeated" has to be false.
        :param: self
        :return: powerpal (object of class powerpal) with attribute "defeated" being False"""

        print("\nPrepare: Choose your powerpal! You have the following powerpal with you:\n")
        for powerpal in self.powerpal_list:
            if not powerpal.defeated:
                print(str(powerpal))

        list_of_choosable_powerpals = [str(powerpal.id) for powerpal in self.powerpal_list if not powerpal.defeated]
        chosen_powerpal = self.get_powerpal(
            int(input_for_choose_undefeated_powerpal.validated_input(list_of_choosable_powerpals)))
        console.game.clear_terminal()

        return chosen_powerpal

    # method to return your wanderer's powerpal (objects from other class) for a given id
    def get_powerpal(self, input_id: int) -> pk or None:
        """This method returns a wanderer's powerpal (object) for a given id.
        If the id is not found in list of powerpal (self.powerpal), return is None.
        :param: self, input_id (int)
        :return: powerpal (object of class powerpal) or None"""
        for powerpal in self.powerpal_list:
            if powerpal.id == input_id:
                return powerpal

    '------------------------ "outer" fight method: fight wanderer --------------'

    # method to fight opposing wanderer
    def fight_wanderer(self, wanderer_opponent: "Wanderer") -> str or int:
        """This method allows you (the wanderer) to confront an opponent (wanderer).
        In the function, you can apply your powerpal (class powerpal), until none are left.
        The opposing wanderer keeps doing the same.
        :param: self (wanderer object; the human player's wanderer), wanderer_opponent (opposing wanderer object)
        :return: str ("fight lost", "no fight", "flight", "Master Max defeated") or int (wanderer.id of defeated wanderer)"""

        # step 1 - see opponent's stats and make fight decision
        fight_or_flight = self.fight_decision(wanderer_opponent)
        if fight_or_flight == "flight":
            console.game.clear_terminal()
            print(f"{Helpers.formatted_text(wanderer_opponent.name, "red")} laughs: "
                  f"You want to run away before we even started?? Coward....so be it.")
            return "flight"
        if fight_or_flight == "can not enter fight":
            print("Your powerpals are down and need to be healed. No fight possible...")
            return "no fight"

        # step 2 - if fight is on, print intro
        console.game.clear_terminal()
        self.fight_intro(wanderer_opponent)

        # step 3 - outer loop: runs until all of the player's powerpal are defeated (or fight is fled from within loop)
        while self.undefeated_powerpals() > 0:

            # step 3.1 - player chooses undefeated powerpal
            chosen_powerpal = self.choose_undefeated_powerpal()
            print("Alright, ready to fight!")

            # step 3.2 - inner loop for player's chosen powerpal:
            # runs until player's powerpal is defeated, player flees, or opponent has no more powerpal left
            # opponent keeps deploying his powerpal in inner loop
            your_powerpal_still_alive = True
            while your_powerpal_still_alive and len(wanderer_opponent.powerpal_list) > 0:
                defeated_powerpal = self.pokeduel_main(chosen_powerpal, wanderer_opponent.powerpal_list[0])
                if defeated_powerpal == wanderer_opponent.powerpal_list[0]:
                    wanderer_opponent.powerpal_list.pop(0)
                    if wanderer_opponent.powerpal_list:
                        print(
                        f'{wanderer_opponent.name} sends another powerpal {wanderer_opponent.powerpal_list[0].name} into the fight!')
                elif defeated_powerpal == "no powerpal defeated, flight":
                    print(f"{Helpers.formatted_text(wanderer_opponent.name, "red")} laughs: "
                          f"Am I too strong for you?? Go cry and come back when you are stronger!")
                    return "flight"
                else:
                    your_powerpal_still_alive = False

            # step 3.3 - multiple checks:
            # if opposing wanderer was defeated, print message and return his id (or a string, if final boss)
            # if "regular" opponent, level up player's wanderer
            if len(wanderer_opponent.powerpal_list) == 0:
                print(f'Your opponent has no powerpals left!\n'
                      f'Congratulations! You have won the fight against {wanderer_opponent.name}!\n',
                      Helpers.formatted_text(pk_art.powerpal_art_fight_won, "green"))
                if wanderer_opponent.name == "Master Max":
                    return "Master Max defeated"
                self.level_up()
                input("\n[Press Enter to go back to map] >> ")
                console.game.print_separating_line()
                return wanderer_opponent.id

        # step 4 - if we end up here (still in outer while loop): player's powerpal are dead, we lost the fight!
        print(f"Nooooooo....You lost the fight! Better find a nursery to heal your powerpals!")
        return "fight lost"

    '-----------------------"inner" fight method": pokeduel_main + helper method---------------------------------'

    def pokeduel_determine_attack_mode(self, opponent_wanderer_is_choosing: bool = False) -> str:
        """This method serves to let the player define the attack mode ("l" or "h") for an attack within the
        pokeduel_main fight method ("inner" fight method thas is called from "outer" fight method fight_wanderer),
         or to quit.
        It also determines an arbitrarily chosen mode ("l" or "h"), if the opponent wanderer is choosing.
        :param: self (object of class wanderer); opponent_wanderer_is_choosing (bool)
        :return: str ("l" or "h" or "quit")"""

        if opponent_wanderer_is_choosing:
            heavy_or_light_attack_opponent = rn.randint(0, 10)
            if heavy_or_light_attack_opponent < 8:
                chosen_attack_mode = "l"
            else:
                chosen_attack_mode = "h"
        else:
            # get validated input for chosen attack mode
            chosen_attack_mode = input_for_pokeduel_determine_attack_mode.validated_input()

        console.game.clear_terminal()
        return chosen_attack_mode

    def pokeduel_main(self, player_powerpal: pk, opponent_powerpal: pk) -> pk or str:
        """Fight method for a pair of powerpal (one of player's, one of opposing wanderer's).
        It is the "inner" fight method for pairing powerpal, that is called from the "outer" fight method fight_wanderer.
        :param: self (class object twanderer); player_powerpal (class object powerpal); opponent_powerpal (class object powerpal)
        :return: defeated_powerpal (object of class powerpal) or str ("no powerpal defeated, flight")"""

        print(
            f"\n{player_powerpal.name} ({self.name}\'s powerpal) encounters {opponent_powerpal.name} (your opponents powerpal)!")
        print(pk_art.powerpal_art_confrontation)

        used_heavy_attacks_player = 0
        used_heavy_attacks_opponent = 0

        # loop: runs until player flees, or one of the dueling powerpal is defeated
        while True:
            # step 1 - player's move

            # step 1.1 - get attack_mode
            attack_mode = self.pokeduel_determine_attack_mode()
            if attack_mode == "flight":
                return "no powerpal defeated, flight"

            # step 1.2 - execute attack
            if attack_mode == "h":
                used_heavy_attacks_player += 1
                if used_heavy_attacks_player > 2:
                    print("No heavy attacks left for this encounter!")
                    print(pk_art.powerpal_art_out_of_heavy_attacks)
                else:
                    outcome_attack = player_powerpal.attacks(opponent_powerpal, attack_mode)
            else:
                outcome_attack = player_powerpal.attacks(opponent_powerpal, attack_mode)

            # step 1.3 - check if opponent's powerpal is defeated
            if outcome_attack == "defeated":
                print("Let's see if your opponent sends another powerpal into fight...")
                console.game.print_request_for_proceeding_then_clear_terminal()
                return opponent_powerpal
            console.game.print_request_for_proceeding_then_clear_terminal()

            # step 2 - opponent's move
            input("\nNow it's the opponent's turn! Behold his attack! [Press enter] >> ")
            console.game.clear_terminal()

            # step 2.1 - get attack_mode
            attack_mode = self.pokeduel_determine_attack_mode(opponent_wanderer_is_choosing=True)

            # step 2.2 - execute attack
            if attack_mode == "h":
                used_heavy_attacks_opponent += 1
                if used_heavy_attacks_opponent > 2:
                    print("No heavy attacks left for this encounter! Miss!")
                    print(pk_art.powerpal_art_out_of_heavy_attacks)
                else:
                    outcome_attack = opponent_powerpal.attacks(player_powerpal, attack_mode,
                                                              opponent_powerpal_is_attacking=True)
            else:
                outcome_attack = opponent_powerpal.attacks(player_powerpal, attack_mode,
                                                          opponent_powerpal_is_attacking=True)
            # step 2.3 - check if players's powerpal is defeated, set defeated if neccessary
            if outcome_attack == "defeated":
                return player_powerpal

            console.game.print_request_for_proceeding_then_clear_terminal()

    "-------------------------------------'post-fight' methods to level up and heal powerpals---------------------------"

    # method to level up wanderer (i.e. give powerpal better stats!
    def level_up(self):
        """Method to level up wanderer after won fight. Improves the wanderer's powerpals stats by increasing
         health, attack, and accuracy.
         :param: self
         :return: None"""
        self.level += 1
        print("\nWow! " + Helpers.formatted_text("You leveled up", "green")
              + "! \nYour powerpals have "
              + Helpers.formatted_text("more maximal health, better accuracy, and attack stronger", "green")
              + " now!\nHave a look at your stronger powerpals:\n")
        for powerpal in self.powerpal_list:
            powerpal.level += 1
            powerpal.max_health = int(powerpal.max_health * 1.5)
            powerpal.attack = int(powerpal.attack * 1.5)
            if self.level == 2:
                powerpal.accuracy = 0.9
            elif self.level == 3:
                powerpal.accuracy = 0.95
            else:
                powerpal.accuracy = 1.0
            print(str(powerpal))
        print("\nNote: Your powerpals have " + Helpers.formatted_text("not been healed", "blue") + ", though! \nYou might want to see the "
              + Helpers.formatted_text("nursery", "green") + " before you enter next fights!")

    # method to heal powerpal
    def heal_wanderers_powerpal(self):
        """This method heals the wanderer's powerpal (aka: all powerpal in self.powerpal_list get health = max_health).
        :param: self
        :return: None"""

        # get validated input
        heal_or_not = input_for_heal_wanderers_powerpal.validated_input()
        console.game.clear_terminal()

        # heal or no heal
        if heal_or_not == 'yes':
            print("All of your powerpals have been healed! Their health has been fully replenished again.")
            for single_powerpal in self.powerpal_list:
                single_powerpal.defeated = False
                single_powerpal.health = single_powerpal.max_health
                print(str(single_powerpal))
        else:
            print("As you wish. Your powerpals have not been healed - beware the next fight 0.O!!")


"-------------------------CREATE CLASS OBJECTS------------------------------------------------------------------------"

wanderer_player = Wanderer("player_name", 1, 1, [pk.player_powerpal_1, pk.player_powerpal_2])

opponent_3 = Wanderer("Fabulous Frank", 3, 1, [pk.powerpal_1_lv_1, pk.powerpal_2_lv_1])

opponent_4 = Wanderer("Angry Aretha", 4, 2, [pk.powerpal_1_lv_2, pk.powerpal_2_lv_2])

opponent_5 = Wanderer("Greg the Great", 5, 3, [pk.powerpal_1_lv_3, pk.powerpal_2_lv_3])

opponent_6 = Wanderer("Master Max", 6, 4, [pk.powerpal_1_lv_4, pk.powerpal_2_lv_4])

wanderer_list = [opponent_3, opponent_4, opponent_5, opponent_6]





