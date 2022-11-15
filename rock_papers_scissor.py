
# computer_choice = "scissors"

# To randomize the computer_choice 
import random
computer_choice = random.choice(["scissors", "paper", "rock"])

user_choice = input("What do you choose - rock - paper - scissors?\n")

if computer_choice == user_choice:
    print("That's a TIE😃👍🏼!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Win!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Win!")   
else:
     print("Computer wins and you lose!")