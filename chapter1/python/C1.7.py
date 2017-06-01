"""
Problem : Write an algorithm such that if an element in an MxN matrix is zero,
		  its entire row and column are set to 0
"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Gayle McDowell","Ravi Kiran Chadalawada"]
__status__  = "Prototype"


def alter_matrix(mat,w,h):
	""" sets the row and column of an zero element to zero
	"""
	visited = [[0 for x in range(w)] for y in range(h)]
	for i in range(0,h):
		for j in range(0,w):
			if mat[i][j] == 0 and visited[i][j] == 0:
				set_row_zero(mat,i,w,visited)
				set_column_zero(mat,j,h,visited)
	return mat

def set_row_zero(mat,i,w,visited):
	"""sets row of zero element to zero
	"""
	for k in range(0,w):
		mat[i][k] = 0
		visited[i][k] = 1


def set_column_zero(mat,j,h,visited):
	"""
	sets column of zero element to zero
	"""
	for k in range(0,h):
		mat[k][j] = 0
		visited[k][j] = 1


if __name__ == "__main__":
	w, h = 3, 3;
	mat = [[x+y for x in range(w)] for y in range(h)]
	print(mat)	
	print(alter_matrix(mat,w,h))
