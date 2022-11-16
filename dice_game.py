
# in order to use random package, you have to import it
import random


def roll_dice():
    dic_total = random.randint(1, 6) + random.randint(1, 6)
    return dic_total

# creating a main() function - all variables within are global functions


def main():
    player1 = input("Enter player's 1 name?\n")
    player2 = input("Enter player's 2 name?\n")

    # will create a roll1 variable which will store for player1 first and second dice rolls

    # this assimilates rolling two dice
    roll1 = random.randint(1, 6) + random.randint(1, 6)
    roll2 = random.randint(1, 6) + random.randint(1, 6)  # for player2

    roll1 = roll_dice()
    roll2 = roll_dice()

    # to show players the results of their dice rolling
    print(player1, "rolled", roll1)
    print(player2, "rolled", roll2)

    if roll1 > roll2:
        print(player1, "wins!")
    elif roll2 > roll1:
        print(player2, "wins!")
    else:
        print("TIE!!")


main()
