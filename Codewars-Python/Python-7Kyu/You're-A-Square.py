# Link to kata: https://www.codewars.com/kata/54c27a33fb7da0db0100040e

def is_square(n):    
    import math
    
    if n < 0:
        return False

    elif n == 0:
        return True

    elif n % math.sqrt(n) == 0:
        return True

    elif n % math.sqrt(n) != 0:
        return False
