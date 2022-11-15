# Create a loan calculator that calculate how much of our loan has been paid off after a given number of months 

# get the loan details 
# 1. how much do you owe in $ 
money_owed =  float(input("How much money do you owe in $:\n")) # // $50,000 

# The second value we want is the annual percentage rate % => 3% 
apr = float(input("What is the annual percentage rate?\n"))

# what is your monthly payment in $ 
payment = float(int("What is your monthly payment in $?\n")) # 1000 per month 

# how many months do you want to see the results for? 
months = int(input("How many months do you want to see the results for?\n"))  # 24 months or 2 years 

# first, we calculate the monthly interest rate - divide 3% by 100, then divide again by 12 months 
monthly_rate = apr/100/12

# now let's calculate the first month interest + the amount of money we owe 
interest_paid =  monthly_rate * money_owed

money_owed = interest_paid + money_owed

# The money we still owe = money_owed - our monthly payment 
money_owed = money_owed - payment

# let's print the result 
print("A monthly payment of", payment, "of a", money_owed, "loan amount of" "And an interest rate of", interest_paid, sep='')
print("")
