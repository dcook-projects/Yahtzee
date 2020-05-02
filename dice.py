import random


class Dice:

    def __init__(self):
        self.player_dice = [0, 0, 0, 0, 0]

    def roll(self, dice_to_hold):
        for i in range(5):
            if i+1 not in dice_to_hold:
                self.player_dice[i] = random.randint(1, 6)

    def __str__(self):
        return self.player_dice.__str__()

    def print_dice(self):
        print(self, flush=True)

    @staticmethod
    def are_held_dice_valid(dice_string):
        held_dice_str_list = dice_string.split()
        for item in held_dice_str_list:
            if not item.isdigit():
                return False

        held_dice_int_list = list(map(int, held_dice_str_list))
        if len(held_dice_int_list) > 5:
            return False

        for value in held_dice_int_list:
            if value < 1 or value > 5:
                return False

        return True

    def add_all_dice(self):
        total = 0
        for die in self.player_dice:
            total += die

        return total

    def create_frequency_dictionary(self):
        freq_dict = {}

        for die in self.player_dice:
            if die not in freq_dict:
                freq_dict[die] = 1
            else:
                freq_dict[die] += 1

        return freq_dict

    def is_valid_three_of_a_kind(self):
        freq_dict = self.create_frequency_dictionary()
        valid = False

        for key, value in freq_dict.items():
            if value >= 3:
                valid = True

        return valid

    def is_valid_four_of_a_kind(self):
        freq_dict = self.create_frequency_dictionary()
        valid = False

        for key, value in freq_dict.items():
            if value >= 4:
                valid = True

        return valid

    def is_valid_full_house(self):
        freq_dict = self.create_frequency_dictionary()

        if len(freq_dict) > 2:
            return False

        # A full house is valid if there are two different dice numbers that appear thrice and twice (Example: three 5s
        # and two 1s), or all five dice are the same.
        freq_list = []
        for key, value in freq_dict.items():
            freq_list.append(value)

        if len(freq_list) == 1:
            if 5 in freq_list:
                return True
        elif len(freq_list) == 2:
            if 3 in freq_list and 2 in freq_list:
                return True

        return False

    def is_valid_yahtzee(self):
        freq_set = set(self.player_dice)
        if len(freq_set) != 1:
            return False

        return True

    def is_valid_small_straight(self):
        sorted_dice = list(self.player_dice)
        sorted_dice.sort()
        continuous_dice = 0

        # Go through the sorted dice list and look for 3 consecutive times where the current die is equal to
        # the previous die + 1
        for i in range(1, 5):
            if sorted_dice[i] == sorted_dice[i - 1]:
                continue
            if sorted_dice[i] == sorted_dice[i - 1] + 1:
                continuous_dice += 1
                if continuous_dice == 3:
                    return True
            else:
                continuous_dice = 0

        return False

    def is_valid_large_straight(self):
        sorted_dice = list(self.player_dice)
        sorted_dice.sort()

        # Go through the sorted dice and check that each die is equal to the previous die + 1
        for i in range(1, 5):
            if sorted_dice[i] != sorted_dice[i - 1] + 1:

                return False

        return True

    def add_specific_value(self, value):
        total = 0
        for die in self.player_dice:
            if die == value:
                total += value

        return total
