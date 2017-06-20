"""
Your company delivers breakfast via autonomous quadcopter drones. And something
mysterious has happened.Each breakfast delivery is assigned a unique ID, a 
positive integer. When one of the company's 100 drones takes off with a delivery, 
the delivery's ID is added to a list, delivery_id_confirmations. When the drone 
comes back and lands, the ID is again added to the same list.

After breakfast this morning there were only 99 drones on the tarmac. One of the 
drones never made it back from a delivery. We suspect a secret agent from Amazon 
placed an order and stole one of our patented drones. To track them down, we 
need to find their delivery ID.

Given the list of IDs, which contains many duplicate integers and one unique 
integer, find the unique integer.

The IDs are not guaranteed to be sorted or sequential. Orders aren't always 
fulfilled in the order they were received, and some deliveries get cancelled 
before takeoff.

Time complexity = O(n)
Space complexity = O(1)

XOR bitwise operation helps here !! 
"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Interviewcake.com"]
__status__  = "Prototype"

def find_unique(ids):
	
	unique = ids.pop(0)
	for delivery_id in ids:
		unique = (unique ^ delivery_id)
	
	return unique


if __name__=='__main__':
	ids = [1,2,3,45,3,2,1]
	print(find_unique(ids))
