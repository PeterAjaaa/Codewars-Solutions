# Link to kata: https://www.codewars.com/kata/569d488d61b812a0f7000015

def data_reverse(data):
    import collections
    import itertools
    
    reverse = collections.deque([]) # Make 'reverse' list type a deque (double-ended queue).
    
    while len(data) != 0:
        reverse.appendleft(data[0:8])
        del data[0:8]
    
    return list(itertools.chain(*reverse)) # Use itertools.chain to flatten the lists inside of 'reverse'.

# Note:
# The asterisk (*) operator is used for unpacking a function using positional argument.
# To put it simply, the unpacking operator basically iterates over a sequence.
