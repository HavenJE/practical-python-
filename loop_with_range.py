
# use range() function to generate a sequence of integers matches the argument in the () starting from zero 
# e.g. range(7) => (0,1,2,3,4,5,6)

# You can customize it by adding a start, stop, step values e.g.e range(0, 7, 1) => starts at 0, stop at 7, step by 1 
# // (0,1,2,3,4,5,6)

# another example range(2, 14, 2) => start at 2, stop at 14, step by 2 
# // (2,4,6,8,10,12)

# for i in range(2,14,3):
#     print(i)


# let's create a code that accepts a number of entries of expenses 
total = 0
expenses = []

# This will ask you to enter the number of entries e.g. 5 
num_expenses = int(input("Enter the # of expenses: \n"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense here: ")))


total = sum(expenses)

# This will sum all the entries 
print("Your sum of expenses is: ", total, sep='')