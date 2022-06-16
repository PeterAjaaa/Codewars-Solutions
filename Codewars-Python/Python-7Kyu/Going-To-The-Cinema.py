# Link to kata: https://www.codewars.com/kata/562f91ff6a8b77dfe900006e

def movie(card, ticket, perc):
    import math
    i = 0
    sys_a = 0
    sys_b = 0

    while math.ceil(card + sys_b) >= sys_a:
        sys_a += ticket 
        sys_b = (sys_b + ticket) * perc 
        i += 1
    return i
  
# math.ceil() returns the smallest integer greater than or equal to the float value. 
