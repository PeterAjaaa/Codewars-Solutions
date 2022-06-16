# Link to kata: https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    return next((x for x in seq if seq.count(x) % 2 != 0), None)
  
# The next () function is to retrieve the next item from the iterator by calling its 
# __next__ method. If default is given, it is returned if the iterator is exhausted, 
# otherwise StopIteration is raised.
