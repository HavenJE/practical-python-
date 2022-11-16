# Create a loan calculator that calculate how much of our loan has been paid off after a given number of months 

# get the loan details 
# 1. how much do you owe in Dollars 
money_owed =  float(input("How much money do you owe in Dollars:\n")) 
# // Dollars50,000 

# The second value we want is the annual percentage rate % => 3% 
apr = float(input("What is the annual percentage rate?\n"))

# what is your monthly payment in Dollars 
payment = float(input("What is your monthly payment in Dollars?\n")) 
# 1000 per month 

# how many months do you want to see the results for? 
months = int(input("How many months do you want to see the results for?\n"))  # 24 months or 2 years 

# first, we calculate the monthly interest rate - divide 3% by 100, then divide again by 12 months 
monthly_rate = apr/100/12

for i in range(months):
    # now let's calculate the first month interest + the amount of money we owe 
    interest_paid =  monthly_rate * money_owed

    money_owed = interest_paid + money_owed

    # if you happened to have paid all amount you owe shorter than the # of months you chose, 
    if (money_owed - payment < 0):
        print("The last amount you own is:", money_owed)
        print("You have paid what you owe in", i+1, "months")
        break

    # The money we still owe = money_owed - our monthly payment 
    money_owed = money_owed - payment

    # let's print the result 
    print("A monthly payment of", payment, "of which", interest_paid, "was interest...", end=' ')
    print("Now you owe", money_owed)
