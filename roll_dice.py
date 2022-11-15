
import random

# To return a random number btw 1 & 6 
roll = random.randint(1,6)

# Because the print is a string here, we need to convert the roll int into t str 
print("The computer rolled a " + str(roll))

# now we create a guess variable and compare it to the roll but before, we need to convert it to an int 
guess = int(input("Guess the dice roll:\n"))

if guess == roll:
    print("Your guess is right WOW! You rolled a " + str(roll))
else:
    print("Wrong guess buddy..you rolled a " + str(roll) + " try next time!")