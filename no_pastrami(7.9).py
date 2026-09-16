# Name: Michael Ko
# Class: CSCI 1511
# Professor: Travis Burke 
# Date: 09/14/2026 

print("The deli has run out of pastrami.")
print()

# List + three pastrami
sandwich_orders = ["PB&J", "Tuna Sandwich", "American Sub", "Chicken Sandwich", "Cheesesteak", "Egg Sandwich", "pastrami", "pastrami", "pastrami"]
# Empty list
finished_sandwiches = []

# While loop removing "pastrami" from sandwich orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Looping as long as orders are left in sandwich_orders
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print(f"Your {current_sandwiches} is ready.")
    finished_sandwiches.append(current_sandwiches)

print("\nSandwiches Made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")