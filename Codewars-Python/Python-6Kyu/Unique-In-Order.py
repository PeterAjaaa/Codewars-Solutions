# Link to kata: https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    if type(iterable) != list:
        start = list(iterable)
    else:
        start = iterable
    previous = 0
    i = 0
    
    for x in start:
        if previous != x:
            start[i] = x
            previous = x
            i += 1

    return start[:i] # Return the 'start' list with list slicing, only returning the item up to the 'i' index.
