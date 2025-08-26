# Compound Interest Calculator
# Created as part of Break Through Tech AI 2025
# Calculates account balance growth over time using functions, loops, and containers

balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))

def compound(balance, rate, num_periods):
    print(0, round(balance,2))
    for n in range(1,num_periods+1):
        balance = round( balance * (1 + rate), 2)
        print(n, balance)
    return balance


# Do NOT modify code above this line
# -----------------------

# Below is the function definition for compound_by_period. 
# Remove the comment before the function definition and 
# complete the function 

def compound_by_period(balance, rate, num_periods):
    balances = [round(balance,2)] #Start with initial balance
    for n in range(num_periods):
        balance = round(balance * (1 + rate), 2)
        balances.append(balance)
    return balances
    

# Do NOT modify the change_per_period() function
# -----------------------------
def change_per_period(balances):
    for i in range(0,len(balances)-1):
         balances.append(balances[i+1] - balances[i])
    return balances

# Generate the list of balances
balances = compound_by_period(100, 0.03, 10)
print("Balances:", balances)

# Test the pre_written change_per_period function
changes = change_per_period(balances)
print("Changes: ", changes)


# Wheat on a chessboard problem
wheat = compound_by_period(1,1,63) #Starting with 1 grain, double 63 times
print("Wheat per square: ", wheat)

total_wheat = sum(wheat)
print("Total grains of wheat on the board:", total_wheat)
