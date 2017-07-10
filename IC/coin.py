"""
Write a function that, given an amount of money and a list of coin denominations
computes the number of ways to make the amount of money with coins of the 
available denominations.

Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢), 
your program would output 4—the number of ways to make 4¢ with those 
denominations:

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢

Time Complexity = O(n*m) where n is the amount and m is the size of denominations

Space complexity = varies with each implementation
"""

def find_number_of_ways(amount, coins):

	""" This is my naive and incorrect implementation
	"""
	length = len(coins)
	answer = 0

	for i in range(0,length):
		current = coins[i]
		current_list = [current]
		while (current <= amount):
			if (amount-current) in coins:
				answer += 1
				print(current_list, amount-current)
			current += coins[i]
			current_list.append(coins[i])
	print(answer)


def find_ways_recursive(amount_left, denominations, current_index = 0):
	"""Returns number of ways of representing amount w.r.t given denominations
	Space Complexity = O(n*m)
	"""

	if amount_left == 0:
		return 1
	
	if amount_left < 0 :
		return 0

	if current_index == len(denominations):
		return 0

	current_coin = denominations[current_index]

	number_of_ways = 0

	while amount_left >= 0:
		number_of_ways += find_ways_recursive(amount_left, denominations, current_index+1)
		amount_left -= current_coin

	return number_of_ways


memo = {}

def find_ways_recursive_memoized(amount_left, denominations, current_index = 0):
	"""Returns number of ways of representing amount w.r.t given denominations
	Space Complexity = O(n*m)
	"""

	memo_key = str((amount_left, current_index))

	if memo_key in memo:
		return memo[memo_key]


	if amount_left == 0:
		return 1

	if amount_left < 0:
		return 0
		
	if current_index == len(denominations):
		return 0

	current_coin = denominations[current_index]

	number_of_ways = 0
	
	while amount_left >= 0:
		number_of_ways += find_ways_recursive(amount_left, denominations, current_index+1)
		amount_left -= current_coin

	memo[memo_key] = number_of_ways

	return number_of_ways


def find_number_of_ways_iterative(amount,denominations):
	"""Returns number of ways of representing amount w.r.t given denominations
	Space Complexity = O(n)
	"""
	
	number_of_ways = [0] * (amount + 1)

	number_of_ways[0] = 1

	for coin in denominations:
		for amount_value in range(coin,amount+1):
			amount_remaining = amount_value - coin
			number_of_ways[amount_value] += number_of_ways[amount_remaining]


	return number_of_ways[amount]


if __name__=='__main__':
	amount = 4;
	coins  = [1,2,3,4]
	#number_of_ways(amount, coins)

	print(find_ways_recursive(amount,coins))
	
	print(find_ways_recursive_memoized(amount,coins))

	print(find_number_of_ways_iterative(amount,coins))

