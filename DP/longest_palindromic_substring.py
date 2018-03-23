"""
Longest Palindromic substring in a string.
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["geeksforgeeks"]
__status__  = "Prototype"


def lps(str):
    """ This function returns the length of the longest palindromic substring
    in a given string. Following the approach of bottom-up in dynamic
    programming.

    As with many bottom-up DP solutions, I am varying the length of the
    longest possible substring in this logic. i.e from 1..n. Building the 
    solution for length k basing on the results for length k-2 th substring.

    Hope I made some sense with above explanation :)

    Time Complexity : O(n^2)
    Space Complexity : O(n^2)
    """

    n = len(str)
    # table[i][j] will be true is str[i,j] is a palindrome
    table = [[0 for x in range(n)] for y in range(n)]

    max_length = 1

    # All substrings with length 1 are palindromes
    i = 0
    while i < n:
        table[i][i] = 1
        i += 1


    # Checking for all substrings of length 2
    for i in range(0,n - 1):
        if str[i] == str[i+1]:
            table[i][i+1] = 1
            max_length = 2

    # For substrings of length greater than 2
    for k in range(3,n+1):
        for i in range (0,n-k+1):
            j = i + k -1

            if table[i+1][j-1] and str[i] == str[j]:
                table[i][j] = 1

                if k > max_length:
                    max_length = k
                    start = i

    print("max_length is", max_length)
    print("longest palindrome substring is", str[start:start + max_length])

if __name__ == '__main__':
    lps("malayalam")
