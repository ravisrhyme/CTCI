"""
Write an algorithm to print all ways of arranging eight queens on an 8x8 chess
board so that none of them share the same row,column or diognal.

In this case "diognal" means all diognals, not the two that bisects the board.

Time Complexity : proportional to O(8^8) 
Space Complexity: O(n) i.e number of rows

Back tracking algorithm it is.. State space : O(8^8)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"


#all_ways = []
def find_all_ways(final_columns,row,all_ways):

	#global all_ways
	if row == 8:
		print(final_columns)
		all_ways.extend(final_columns)
		#all_ways = all_ways + final_columns
		return
	else:
		for column in range(0,8):
			if is_correct_position(final_columns,row,column) == True:
				final_columns[row] = column
				find_all_ways(final_columns, row+1,all_ways)



def is_correct_position(final_columns,row1,column1):
	""" Checks whether a given position is to place the queen
	by checking the columns and diognal. Two queens not being in same row 
	is taken care by caller function.
	"""

	for row2 in range(0, row1):
		column2 = final_columns[row2]
		
		# Checking whether some other queen is present in same column
		if column2 == column1:
			return False

		# Checking for diognal presence
		column_difference = abs(column2 - column1)

		row_difference = row1-row2 

		# If both row_difference and column_difference are equal, then queens 
		# are diognal
		if column_difference == row_difference:
			return False

	return True


if __name__=='__main__':

	final_columns = [-1] * 8
	all_ways = []	
	find_all_ways(final_columns,0,all_ways)
	print(all_ways)

