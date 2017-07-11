"""
You are a renowned thief who has recently switched from stealing precious metals 
to stealing cakes because of the insane profit margins. You end up hitting the 
jackpot, breaking into the world's largest privately owned stock of cakes—the 
vault of the Queen of England.
While Queen Elizabeth has a limited number of types of cake, she has an unlimited 
supply of each type.

Each type of cake has a weight and a value, stored in a tuple with two indices:

    *An integer representing the weight of the cake in kilograms
    *An integer representing the monetary value of the cake in British pounds
For example:

  # weighs 7 kilograms and has a value of 160 pounds
	(7, 160)

  # weighs 3 kilograms and has a value of 90 pounds
	(3, 90)

You brought a duffel bag that can hold limited weight, and you want to make off 
with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and
a weight capacity, and returns the maximum monetary value the duffel bag can hold.

For Example:
cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

max_duffel_bag_value(cake_tuples, capacity)
# returns 555 (6 of the middle type of cake and 1 of the last type of cake)


Time complexity : O(n*k) 
Space Complexity : O(k)

where n is the number of cake tuples
k is the maximum_capacity of bag
"""

def max_duffel_bag_value(cake_tuples,max_capacity):
	""" Returns the maximum value that can be filled in bag with maximum 
	capacity of max_capacity
	"""

	max_value_capacities = [0] * (max_capacity + 1) # List to fill max values till max_capacity

	for current_capacity in range(1,max_capacity + 1): # Traversing across all capacities
		for cake_weight,cake_value in cake_tuples: # Checking with each cake tuple for each cacpacity
		
			# Cake weight is 0 and has a value, we can fill our bag with infinite such cakes
			if (cake_weight == 0 and cake_value != 0):
				return float('inf')

			# consider all caked which weigh less than current capacity
			if cake_weight <= current_capacity:
				remaining_capacity = current_capacity - cake_weight

				max_value_capacities[current_capacity] = max(max_value_capacities[current_capacity], \
														 cake_value + max_value_capacities[remaining_capacity])


	return max_value_capacities[max_capacity] # Returns the value for maximum capacity


if __name__=="__main__":
	cake_tuples = [(7, 160), (3, 90), (2, 15)]
	capacity = 20
	print(max_duffel_bag_value(cake_tuples,capacity))
