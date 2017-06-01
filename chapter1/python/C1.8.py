"""
Problem : Given two strings, s1,s2. Write a method to check if s2
		  is a rotation of s1 using only one call to is_substring()
		  Assume you already have definition of is_substring()

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Gayle McDowell"]
__status__  = "Prototype"



""" Following two functions are as per my idea"""
def is_substring(s1,s2):
	""" Returs True if S2 is rotations of S1
	False otherwise
	"""
	length_1 = len(s1)
	length_2 = len(s2)
	if (length_1 != length_2):
		return False
	k = find_position(s1[0],s2)
	for i in range(0,length_1):
		if (s1[i] != s2[k]):
			return False
		k = k+1;
		if (k == length_1):
			k = 0
	return True


def find_position(c,s2):
	""" Returns the index of c in s2 if present
	Else returns -1
	"""
	length = len(s2)
	position = -1
	for i in range(0, length):
		if s2[i] == c :
			position = i
			break
	return position

#Gayle's Idea
def is_rotation(s1,s2):
	""" Gayle's Idea
	Get the rotation point.
	example : s1 = "waterbottle" and s2 = "erbottlewat"
	rotation point : 'w'
	split the strings w.r.t rotation point: i.e
	x = "wat" y = "erbottle"
	now S1 = xy and s2 = yx
	s2 is always a substring of xyxy i.e s1s1 if it is a rotation of s1
	"""
	length_1 = len(s1)
	length_2 = len(s2)
	if (length_1 != length_2):
		return False
	temp = s1 + s1
	found = temp.find(s2)
	if (found == -1):
		return False
	else:
		return True

if __name__=="__main__":
	print(is_substring("waterbottle","erottlewat"))
	print(is_rotation("waterbottle","erottlewat"))
