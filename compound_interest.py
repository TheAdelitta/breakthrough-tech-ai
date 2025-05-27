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

# def compound_by_period(balance, rate, num_periods):
    
    

# Do NOT modify the change_per_period() function
# -----------------------------
def change_per_period(balances):
    for i in range(0,len(balances)-1):
         balances.append(balances[i+1] - balances[i])
    return balances
