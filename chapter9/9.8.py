"""
Given an infinite number of quarters,dimes,nickels and pennies, write code to
calculate the number of ways of representing n cents.
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


def find_combinations_recursive(coins,amount,index=0):

	if amount == 0:
		return 1

	if amount < 0 or index == len(coins):
		return 0

	current_coin = coins[index]
	number_of_ways = 0

	while amount >=0:
		number_of_ways += find_combinations_recursive(coins,amount,index+1)
		amount -= current_coin

	return number_of_ways

memo = {}
def find_combinations_recursive_memoized(coins,amount,index=0):

	if amount == 0:
		return 1

	if amount < 0 or index == len(coins):
		return 0

	key = str((amount,index))

	if key in memo:
		return momo[key]

	current_coin = coins[index]
	number_of_ways = 0

	while amount >=0:
		number_of_ways += find_combinations_recursive(coins,amount,index+1)
		amount -= current_coin

	memo[key] = number_of_ways
	return number_of_ways


def find_combinations_iterative(coins,amount,index = 0):

	no_of_ways = [0] * (amount + 1)

	no_of_ways[0] = 1
	current_amount = 1

	for coin in coins:
		for current_amount in range(coin,amount+1):
			no_of_ways[current_amount] += no_of_ways[current_amount-coin]


	return no_of_ways[amount]
				
		

if __name__=='__main__':

	coins = [1,5,10,25]
	amount = 10
	print(find_combinations_iterative(coins,amount))
