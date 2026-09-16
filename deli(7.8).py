# Name: Michael Ko
# Class: CSCI 1511
# Professor: Travis Burke 
# Date: 09/15/2026 

# List
sandwich_orders = ["PB&J", "Tuna Sandwich", "American Sub", "Chicken Sandwich", "Cheesesteak", "Egg Sandwich"]
# Empty list
finished_sandwiches = []

# Looping as long as orders are left in sandwich_orders
while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    print(f"Your {current_sandwiches} is ready.")
    finished_sandwiches.append(current_sandwiches)

print("\nSandwiches Made: ")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")