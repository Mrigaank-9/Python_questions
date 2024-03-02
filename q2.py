import random

def calculate_change(amount_due, amount_given):
    denominations = [('dollars', 1.00), ('quarters', 0.25), ('dimes', 0.10), ('nickels', 0.05)]
    change_due = round(amount_given - amount_due, 2)
    change_in_coins = {}
    
    for denomination, value in denominations:
        if value <= change_due:
            num_coins = int(change_due // value)
            change_in_coins[denomination] = num_coins
            change_due -= num_coins * value
    
    # Round change to the nearest nickel
    change_due = round(change_due / 0.05) * 0.05
    
    # Distribute remaining change using the fewest coins possible
    for denomination, value in sorted(denominations, key=lambda x: x[1], reverse=True):
        while value <= change_due:
            change_in_coins[denomination] = change_in_coins.get(denomination, 0) + 1
            change_due -= value

    return change_in_coins

# Example usage
amount_due = random.randint(0,20) + round(random.randint(0,100)/100,2)
# amount_given = random.randint(0,20) + round(random.randint(0,100)/100,2) # ffor random values 
print(f"Amount Due: {amount_due:.2f}")
amount_given = float(input("Enter the amount to pay : ")) # for user input 
print(f"Amount given: {amount_given:.2f}")
if amount_given < amount_due:
    print("Insufficient amount ")
else:
    change = calculate_change(amount_due, amount_given)
    print("\nChange Returned :")
    for denomination, num_coins in change.items():
        print(f"{num_coins} {denomination}")
