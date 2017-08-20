"""
Trader Profit described in pdf document.

Time Complexity  : O(nk)
Space Complexity : O(n)

This is a slight modification of famous stocks problem.
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Hackerrank.com","goldmansachs"]
__status__  = "Prototype"

def find_max_profit(stock_prices,k):
	""" Returns the maximum profit that can be made after 'k' Transactions.
	Note: A transaction starts after the previous transaction has ended. Two transactions can't overlap or run
	in parallel.
	"""
	eliminated_indices = set()
	total_profit = 0

	
	for i in range(0,k):
		max_profit = float('-inf')
		min_price  = float('inf')
		
		for current_index,current_price in enumerate(stock_prices):
			# This condition takes care of note by making sure that 
			# prices are not used in previous transaction.
			if current_index not in eliminated_indices:
				current_profit = current_price - min_price

				if (current_profit > max_profit):
					buying_price_index = min_price_index
					selling_price_index = current_index
					max_profit = current_profit

				#min_price = min(min_price, current_price)
				if (current_price < min_price):
					min_price = current_price
					min_price_index = current_index


		# This for loop is to take care of Note
		for i in range(buying_price_index,selling_price_index+1):
			eliminated_indices.add(i)

		total_profit += max_profit
		print('buying_price_index :',buying_price_index)
		print("selling_price_index :",selling_price_index)

	return total_profit

if __name__=='__main__':
	stock_prices = [10,22,5,75,65,80]
	print("Total Profit :",find_max_profit(stock_prices,2))
