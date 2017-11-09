
"""
kraken is board game that contains a rectagular board of size mxn. The objective
is to reach the bottom from the top. Given the size of board, find the number of 
ways of reaching the bottom from top of the board.
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Hackerrank.com","Twitter.com"]
__status__  = "Prototype"

def  krakenCount(m, n):
    
    no_of_ways = find_number_of_ways(1,1,m,n)
    return no_of_ways


def find_number_of_ways(i,j,m,n):
    
    if i > m or j > n:
        return 0
    
    elif i == m and j == n:
        return 1
    
    return find_number_of_ways(i+1,j,m,n) + find_number_of_ways(i,j+1,m,n) + find_number_of_ways(i+1,j+1,m,n)


if __name__ == "__main__":
    print(krakenCount(2,2))
