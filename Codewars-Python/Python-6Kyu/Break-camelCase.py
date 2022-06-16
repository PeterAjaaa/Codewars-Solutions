# Link to kata: https://www.codewars.com/kata/5208f99aee097e6552000148

def solution(s):
    import string
    y = list(string.ascii_uppercase)
    z = []
    
    for x in s:
        if x not in y: 
            z.append(x)
        elif x in y: 
            z.append(" ")
            z.append(x)
        elif not x: 
            z.append("")
            
    return "".join(z)