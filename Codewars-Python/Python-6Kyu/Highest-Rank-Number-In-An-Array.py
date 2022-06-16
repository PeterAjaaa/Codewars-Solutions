# Link to kata: https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004

def highest_rank(arr):
    number = 0
    count = 0
    
    for x in arr:
        if arr.count(x) > count:
            number = x
            count = arr.count(x)
        elif arr.count(x) < count:
            count = count
            number = number
        elif arr.count(x) == count:
            count = count
            if x > number:
                number = x
            elif x < number:
                number = number
                
    return number
