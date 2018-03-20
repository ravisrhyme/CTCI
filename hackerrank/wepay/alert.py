"""
Designing an Alert.

"""

__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Hackerrank.com","wepay"]
__status__  = "Prototype"

def alert(inputs, windowSize,allowedIncrease):
    
    # This list holds the Averages of all windows
    averages = []
    length = len(inputs) # Length of list
    window_sum = 0

    # This block calculates the average of each window.
    # This is computed in O(n).
    for i in range(0,length):
        window_sum += inputs[i]
        
        # Keep adding the elements till windowSize is met
        if (i +1) == windowSize:
            averages.append(window_sum/windowSize)
            
        # After window size, subtract the starting element from previous
        # window from the current window_sum  
        elif (i + 1) > windowSize :
            window_sum -= inputs[i-windowSize]
            averages.append(window_sum/windowSize)

    # Below two sets active() and delete () 
    # helps in meeting #1 condition in the problem description.
    
    # Logic : 
    # For each window, check any element of that window is greater than the 
    # allowedIncrease times average of the window.
    
    # deleted() set helps in knowing whether the same element 
    # failed to be satisy the condition in some other 
    # window. If both conditions are met, add it to active()

    # If an element of window doesn't satisfy the condition,
    #  a) If it is already in active, delete it from active() set
    #     and add it to delete() set. 
    
    # Size of active() finally helps to know whether there is any element that 
    # satisfies the given condition #1
    
    # This runs in O(n^2).
    active = set()
    deleted = set()

    for i in range(0,length - windowSize + 1):
        window = inputs[i:i+windowSize]

        for j in range(0,windowSize):
            if window[j] > allowedIncrease * averages[i] and window[j] not in deleted:
                active.add(window[j])

            elif window[j] <= allowedIncrease * averages[i]:
                if window[j] in active:
                    active.remove(window[j])
                deleted.add(window[j])

    # This logic helps in checking #2 condition mentioned in problem statement i.e checking
    # whether there is any average of a window that is greater than the allowed increase over 
    # average of all previous windows. 
    #
    # It returns true if condition is met. This runs in O(k^2), k being number of windows. i.e n/windowSize
    for i in range(0,len(averages)):
        for j in range(i-1,-1,-1):
            if averages[i] > allowedIncrease * averages[j]:
                return True
            
    if len(active) > 0:
        return True

    else:
        return False
