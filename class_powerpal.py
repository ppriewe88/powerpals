import random as rn
import powerpal_art as pk_art
from helpers import Helpers

"-------------------------CREATE CLASS ------------------------------------------------------------------------------"


class powerpal:
    """This class contains a constructor and a string representation for powerpal, as well as an attack method."""

    "------------------------- constructor and string representation----------------------------------"

    # constructor
    def __init__(self,
                 name: str,
                 id: int,
                 level: int,
                 health: int,
                 max_health: int,
                 attack: int,
                 accuracy: float,
                 defeated: bool):
        """This is the constructor for class objects.
        The restrictions for the attributes hold for possible changes to the initial class objects as defined
        at the end of this script. Changing the initial attributes may drastically change the gameplay during fight.
        :param: several parameters to define the attributes.
        For more info on the parameters/attributes, see attributes in code of this constructor.
        :return: class object"""
        self.name = name
        self.id = id
        self.level = level
        if health <= 0 or health > 100:
            print("Health has to be integer between 1 and 100!")
        else:
            self.health = health
        self.max_health = max_health
        if attack <= 0 or attack > 30:
            print("Attack has to be integer between 0 and 1!")
        else:
            self.attack = attack
        if accuracy <= 0 or accuracy > 1:
            print("Accuracy has to be float between 0 and 1!")
        else:
            self.accuracy = accuracy
        self.defeated = defeated

    # string representation
    def __str__(self):
        """This method returns a string representation of a class object.
        :param: self
        :return: str: formatted string with class object data"""
        if self.id > 2:
            output_color = "red"
        else:
            output_color = "blue"
        return (f'name: {Helpers.formatted_text(self.name, output_color).ljust(30, " ")}'
                f'id: {Helpers.formatted_text(str(self.id), output_color)}, '
                f'level: {self.level}, '
                f'health: {self.health}, '
                f'max_health: {self.max_health}, '
                f'accuracy: {self.accuracy}, '
                f'attack: {self.attack} ')

    "--------------------------------------- attack method --------------------------------------------------------"

    # attack method with light and heavy mode
    def attacks(self, attacked_powerpal: "powerpal", attack_mode: str,
                opponent_powerpal_is_attacking: bool = False) -> str:
        """This method executes an attack from one powerpal (param. self) to another (param. attacked_powerpal),
        featuring an attack mode and a check to determine who is attacking.
        It has a light and a heavy attack mode that deals respective damage to the attacked powerpal
        with a mode-specific probability.
        It returns 'hit', 'miss' or 'defeated'.
        :param: self (class object): attacking powerpal; attacked_powerpal (class object): powerpal being attacked;
        attack_mode (str): control parameter for heavy or light attack;
        opponent_powerpal_is_attacking (bool): Needed to distinguish different ascii-arts to be printed.
        :return: str ('hit', 'miss' or 'defeated')"""

        # determine attack specifications depending on attack mode
        if attack_mode == "h":
            attack_type = "heavy"
            required_threshold_for_hit = 0.45
            extra_damage = 2
        else:
            attack_type = "light"
            required_threshold_for_hit = 0.25
            extra_damage = 0

        # calculate attack values
        randomized_hit = rn.uniform(0.1, 1)
        final_randomized_hit = self.accuracy * randomized_hit

        # in case attack hits:
        if final_randomized_hit > required_threshold_for_hit:
            attacked_powerpal.health -= self.attack + extra_damage
            attacked_powerpal.health = max(attacked_powerpal.health, 0)
            print(f"\n{self.name} hit with a {attack_type} attack and dealt "
                  f"{self.attack + extra_damage} damage to {attacked_powerpal.name}!\n"
                  f"{attacked_powerpal.name} has now {attacked_powerpal.health} health left!")
            # print powerpal_art depending on who is attacking
            if opponent_powerpal_is_attacking:
                print(Helpers.formatted_text(pk_art.powerpal_art_opponent_hit, "red"))
                print('health: ', attacked_powerpal.health, '\t\t\t\t health: ', self.health)
            else:
                print(Helpers.formatted_text(pk_art.powerpal_art_player_hit, "green"))
                print('health: ', self.health, '\t\t\t\t health: ', attacked_powerpal.health)
            # defeated-subcase: print art dep. on who is defeated
            if attacked_powerpal.health == 0:
                print(f"{attacked_powerpal.name} was defeated!")
                if opponent_powerpal_is_attacking:
                    print(Helpers.formatted_text(pk_art.powerpal_art_player_dead, "red"))
                else:
                    print(Helpers.formatted_text(pk_art.powerpal_art_opponent_dead, "green"))
                attacked_powerpal.defeated = True
                return "defeated"
            else:
                return "hit"
        # in case attack misses:
        else:
            print(f"\n{self.name}'s {attack_type} attack missed!!\n{attacked_powerpal.name} "
                  f"still has {attacked_powerpal.health} health left!")
            # print powerpal_art depending on who is attacking
            if opponent_powerpal_is_attacking:
                print(pk_art.powerpal_art_opponent_missed)
                print('health: ', attacked_powerpal.health, '\t\t\t\t health: ', self.health)
            else:
                print(pk_art.powerpal_art_player_missed)
                print('health: ', self.health, '\t\t\t\t health: ', attacked_powerpal.health)
            return "miss"


"-------------------------CREATE CLASS OBJECTS------------------------------------------------------------------------"

player_powerpal_1 = powerpal("Dangernoodle", 1, 1, 10, 10, 5, 0.8, False)

player_powerpal_2 = powerpal("Furryfluff", 2, 1, 10, 10, 6, 0.8, False)

powerpal_1_lv_1 = powerpal("Bizzlyboodle", 3, 1, 10, 10, 5, 0.7, False)

powerpal_2_lv_1 = powerpal("Chubbychap", 4, 1, 10, 10, 5, 0.8, False)

powerpal_1_lv_2 = powerpal("Tinywiggle", 5, 2, 14, 14, 7, 0.9, False)

powerpal_2_lv_2 = powerpal("Wobblehead", 6, 2, 16, 16, 5, 1.0, False)

powerpal_1_lv_3 = powerpal("Humptydumpty", 7, 3, 19, 19, 9, 0.9, False)

powerpal_2_lv_3 = powerpal("Holymoly", 8, 3, 18, 18, 13, 1.0, False)

powerpal_1_lv_4 = powerpal("Deconstructor", 9, 4, 35, 35, 15, 0.9, False)

powerpal_2_lv_4 = powerpal("Unholymoly", 10, 4, 25, 25, 18, 0.9, False)
