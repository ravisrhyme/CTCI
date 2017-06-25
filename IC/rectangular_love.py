"""
Write a function to find the rectangular intersection of two given love rectangles

As with the example above, love rectangles are always "straight" and never 
"diagonal." 
More rigorously: each side is parallel with either the x-axis or the y-axis.

Rectangle is defined as dictionary like below:

  my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,

	}

Time Complexity  = O(1)
Space Complexity = O(1)
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"


def find_intersection(r1,r2):
	""" This problem is solved by decomposing the given problem in to 
	Subproblems in one dimension from two dimensions. 
	interesting Idea it is :)
	"""
	x_left, x_right = x_intersection(r1['left_x'],r1['width'],r2['left_x'],r2['width'])
	y_bottom, y_top = y_intersection(r1['bottom_y'],r1['height'],r2['bottom_y'],r2['height'])
	result = {}	
	result['left_x'] = x_left
	result['bottom_y'] = y_bottom
	result['width'] = (x_right - x_left)
	result['height'] = y_top - y_bottom

	return result

def x_intersection(x1,width1,x2,width2):
	""" Finds the intersection w.r.t X dimension.
	Following are four possible cases:
	
	1.
	-----------
         ----------
	2.
		-----------
			----
	3. --------------
		            -------
	4. -------------
				    ---------------
	#3 and #4 are not intersection and hence can be returned null
	#1 and #2 are handled by taking considering the max of two left ends as that 
	will be left end for intersecting rectangle
	and for right end, considered min of two right ends as intersecting rectangle 
	will have that as right end.
	"""	
	left_end = max(x1,x2)
	right_end = min (x1+width1,x2+width2)
	
	if right_end <= x2: # Handles #3 and #4 cases
		return None, None
	return left_end, right_end

def y_intersection(y1,height1,y2,height2):
	""" Finds the intersection w.r.t Y dimension.
	Follows same logic as that for X dimension to compute
	"""
	
	bottom_end = max(y1,y2)
	top_end    = min(y1+height1,y2+height2)
	
	if top_end <= y2: #Handles #3 and #4 cases
		return None, None
	return bottom_end,top_end


if __name__== "__main__":
	
	r1 = {

    # coordinates of bottom-left corner
	'left_x': 1,
	'bottom_y': 5,

	# width and height
	'width': 10,
	'height': 4,
    }
	
	r2 = {

    # coordinates of bottom-left corner
    'left_x': 6,
    'bottom_y': 7,

    # width and height
    'width': 9,
    'height': 4,
    }

	print(find_intersection(r1,r2))
