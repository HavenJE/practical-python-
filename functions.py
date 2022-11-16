
# some functions examples that we have been using:
# print("String")  # => function that prints out a string

# variable = input("string")  # => function that returns a string

# amount = int(10.6)  # => function that converts a decimal number to integer

# => randint() takes a low and high bound and return a random integer with that range
# roll = random.randint(1, 6)

# now lets make a function the makes a greeting for a given name - function definition

# This part called Function Definition
def greeting(name):
    print("Hi", name)


# main program
input_name = input("Enter your name:\n") # the input_name is a variable where the outcome of the input() function will be stored 

greeting(input_name) # we are passing that variable as a parameter in that function
print("Hi", name) # ✖️ the variable name will not work because it's not a local 

# if a variable has been created in the main body of the program => it's a global variable and has a global scope => can be used anywhere! 
