# Link to kata: https://www.codewars.com/kata/545cedaa9943f7fe7b000048

import string

def is_pangram(s):
    s = s.casefold()
    chara = string.ascii_lowercase
    j = 0
    check = []
    
    while j <= len(s):
        for x in chara:
            if s.count(x) >= 1:
                check.append(1)
                j += 1 
            else:
                check.append(0)
                j += 1
                
    if check.count(0) >= 1:
        return False
    else: 
        return True
    
    
