"""
Implement the "paint fill" function that one might see on many image editing
program. That is, given a screen(represented by a two-dimensional array of 
colors), a point, and a new color, fill in the surrounding area untill the color
changes from the original color"

Time Complexity : O(m*n) i.e product of rows and columns
Space Complexity : O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Cracking The coding interview"]
__status__  = "Prototype"

def paint_fill(screen,x,y,original_color,new_color):
	""" Starting from current pixel, Fills all pixels with original color with 
	new color. Returns true if able to fill all pixels.

	Not handling return with all calls as not needed in current case.
	"""
	if (x < 0 or x >= len(screen[0])) or \
	   (y < 0 or y >= len(screen)):
		return False

	if (screen[y][x] == original_color):
		screen[y][x] = new_color
		paint_fill(screen,x-1,y,original_color,new_color) #Left
		paint_fill(screen,x+1,y,original_color,new_color) #Right
		paint_fill(screen,x,y-1,original_color,new_color) #Top
		paint_fill(screen,x,y+1,original_color,new_color) #Bottom

	return True
	

if __name__=='__main__':

	screen = [ [1,2,3],
			   [2,2,3],
			   [1,2,3]]
	print(paint_fill(screen,1,1,2,4))
	print(screen)
