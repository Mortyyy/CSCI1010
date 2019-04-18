# -*- coding: utf-8 -*-
"""

@author: Alex

"""

inventory = {'apples': 4.00, 'bananas': 2.50, 'oranges': 5.80, 'pears': 3.55, 'peaches': 6.60}

# Part A
del inventory['peaches']
print("\n" "Part A:", inventory)

# Part B: A new shipment of grapes arrived with price per pound twice that of apples.
inventory['grapes'] = inventory['apples']*2
print("\n" "Part B:", inventory)

# Part C: Prices of oranges dropped by a dollar.
inventory['oranges'] = inventory['oranges']-1
print("\n" "Part C:", inventory)

#Part D: Prices of all fruits increased by %15.
def adjustCost(item, amount):
    inventory[item] = inventory[item] - (inventory[item] * amount)
    
adjustCost('apples', 0.15)
adjustCost('bananas', 0.15)
adjustCost('oranges', 0.15)
adjustCost('grapes', 0.15)
adjustCost('pears', 0.15)

print("\n" "Part D:", inventory)