

age = int(input("How old are you?\n")) # This has to be wrapped with int( ) to accept an int input from the user 

decades = age // 10  # // refers to a special operator for whole number or int division 

years = age % 10 #  The % sign is called the modulus operator - it will print out the reminder of the int number 

print("You are " + str(decades) + " decades and " + str(years) + " years old!" )

