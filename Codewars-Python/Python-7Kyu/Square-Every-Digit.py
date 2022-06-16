# Link to kata: https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    y = []
    z = [y.append(pow(int(x),2)) for x in str(num) if type(x) ==  str]
    
    return int("".join([str(x) for x in y]))
  
# Z is there to generate and append the squared value to Y list.
# I'm using [] in order for the generator to work, although the Z itself is never directly used.
