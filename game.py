import scorecard
import dice


MAX_ROUNDS = 13
MAX_ROLLS = 3
current_round_number = 1
current_roll_number = 1
player = scorecard.Scorecard()
player_dice = dice.Dice()


def print_rules():
    print("""
The rules of Yahtzee:
The game consists of 13 rounds. There are up to three dice rolls per round.  Up to 5 dice may be rolled.  There are multiple categories
in which a player is able to score points. The categories are as follows:
Ones - Sum of ones in the current dice
Twos - Sum of twos in the current dice
Threes - Sum of threes in the current dice
Fours - Sum of fours in the current dice
Fives - Sum of fives in the current dice
Sixes - Sum of sixes in the current dice
Three of a Kind - At least three dice must have the same number - sum all dice for points
Four of a Kind - At least four dice must have the same number - sum all dice for points
Full House - Three of the dice must have the same number, and the other two dice must have the same number - 25 points
Small Straight - Four dice must contain consecutive numbers - 30 points
Large Straight - Five dice must contain consecutive numbers - 40 points
Yahtzee - All five dice must contain the same number - 50 points
Chance - Sum of all five dice
Yahtzee Bonus - 100 point bonus for each yahtzee after the first
    
A player is allowed to score in each category only once (except for Yahtzee Bonus). Yahtzee bonus can only be taken if the
player scored a yahtzee previously in the game. A player may take a zero in any category that they wish. For example, if the
only categories left are large straight and yahtzee, and the players fail to get either of those by the end of their turn,
the player make take a zero in either of those categories. A player's total points are calculated by adding all the points 
from each category. There is also an opportunity for the player to gain an additional 35 bonus points if the sum of the ones,
twos, threes, fours, fives, and sixes categories add up to at least 63 points. If a player wishes to end their turn 
before all three rolls have occurred, they must hold all five dice.
    """)


def print_category_codes():
    print("The following table lists each score category followed by the key to enter to enter a score for that category:")
    print("""
ones -> ones
twos -> twos
threes -> threes
fours -> fours
fives -> fives
sixes -> sixes
Three of a kind -> 3k
Four of a kind -> 4k
Full house -> fh
Small straight -> ss
Large straight -> ls
Yahtzee -> yahtzee
Chance -> ch
Yahtzee bonus -> yb

Enter "scoreboard" at any time after the game starts to look at the player's score
""")


def determine_score():
    if chosen_category == "ones":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(1))
    elif chosen_category == "twos":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(2))
    elif chosen_category == "threes":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(3))
    elif chosen_category == "fours":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(4))
    elif chosen_category == "fives":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(5))
    elif chosen_category == "sixes":
        player.update_scorecard(chosen_category, player_dice.add_specific_value(6))
    elif chosen_category == "3k":
        if player_dice.is_valid_three_of_a_kind():
            player.update_scorecard(chosen_category, player_dice.add_all_dice())
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "4k":
        if player_dice.is_valid_four_of_a_kind():
            player.update_scorecard(chosen_category, player_dice.add_all_dice())
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "fh":
        if player_dice.is_valid_full_house():
            player.update_scorecard(chosen_category, 25)
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "ss":
        if player_dice.is_valid_small_straight():
            player.update_scorecard(chosen_category, 30)
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "ls":
        if player_dice.is_valid_large_straight():
            player.update_scorecard(chosen_category, 40)
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "yahtzee":
        if player_dice.is_valid_yahtzee():
            player.update_scorecard(chosen_category, 50)
        else:
            player.update_scorecard(chosen_category, 0)
    elif chosen_category == "chance":
        player.update_scorecard(chosen_category, player_dice.add_all_dice())
    elif chosen_category == "yb":
        player.update_scorecard(chosen_category, 100)


print_rules()
print_category_codes()
input("Enter anything to start the game: ")

while current_round_number <= MAX_ROUNDS:
    player_dice.roll([])

    while current_roll_number <= MAX_ROLLS:
        held_dice = []

        print("Roll #{}: {}".format(current_roll_number, str(player_dice)), flush=True)

        if current_roll_number == 1 or current_roll_number == 2:
            while True:
                print("Select dice to hold (1-5 from left to right). Separate dice with a space. Enter a blank line to roll all dice: ", flush=True, end="")
                held_dice_str = input()
                held_dice_str = held_dice_str.lower()

                if held_dice_str == "scoreboard":
                    player.print_scorecard()
                    continue

                valid_hold = player_dice.are_held_dice_valid(held_dice_str)
                if valid_hold:
                    held_dice = held_dice_str.split()
                    held_dice = list(map(int, held_dice))
                    player_dice.roll(held_dice)
                    break
                else:
                    print("The dice held were invalid", flush=True)
                    continue

        if len(held_dice) == 5:
            break

        current_roll_number += 1

    while True:
        print("Enter the category you wish to score: ", flush=True, end="")
        chosen_category = input()
        chosen_category = chosen_category.lower()

        if chosen_category == "scoreboard":
            player.print_scorecard()
            continue

        valid_category = player.is_category_valid(chosen_category, player_dice)
        if valid_category:
            determine_score()
            break
        else:
            print("Invalid category", flush=True)

    current_round_number += 1
    current_roll_number = 1

player.calculate_final_total()
