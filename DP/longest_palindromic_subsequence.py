# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
def lps_iterative(str):
    n = len(str)
 
    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
 
    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
 
    # Build the table. Note that the lower diagonal values of table are
    # useless and not filled in the process. The values are filled in a
    # manner similar to Matrix Chain Multiplication DP solution (See
    # http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j]);
 
    return L[0][n-1]



def lps_recursive(string,i,j):
	
	if i > j :
		return 0
	
	if i == j:
		return 1

	if string[i] == string[j]:
		return 2 + lps_recursive(string,i+1,j-1)
	else :
		return max(lps_recursive(string,i+1,j),lps_recursive(string,i,j-1))

memo = [[-1 for i in range(0,9)] for i in range(0,9)]

def lps_recursive_memoized(string,i,j):

	if i == j:
		memo[i][j] = 1
		return 1

	if memo[i][j] != -1:
		return memo[i][j]

	if string[i] == string[j]:
		memo[i][j] = 2 + lps_recursive_memoized(string,i+1,j-1)
		return memo[i][j]
	else:
		memo[i+1][j] = lps_recursive_memoized(string,i+1,j)
		memo[i][j-1] = lps_recursive_memoized(string,i,j-1)
		return max(memo[i+1][j], memo[i][j-1])


if __name__=='__main__':
	string = 'ravikiran'
	print(lps_recursive(string,0,len(string)-1))
	print(lps_recursive_memoized(string,0,len(string)-1))
