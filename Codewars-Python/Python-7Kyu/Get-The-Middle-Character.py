# Link to kata: https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    x = len(s) / 2 # This is the Python 3 true division. // is used for floor division.
    
    if x.is_integer() == True:
        a = x - 1
        b = x + 1
        return s[int(a):int(b)]
      
    elif x.is_integer() == False:
        a = x - 0.5
        b = x + 0.5
        return s[int(a):int(b)]
