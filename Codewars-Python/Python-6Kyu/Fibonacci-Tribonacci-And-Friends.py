# Link to kata: https://www.codewars.com/kata/556e0fccc392c527f20000c5

def Xbonacci(signature,n):
    lower_limit = 0
    upper_limit = len(signature)
    
    if not n:
        return []
    
    elif n <= len(signature):
        return signature[:n]

    while len(signature) < n:
        signature.append(sum(signature[lower_limit:upper_limit]))
        lower_limit += 1
        upper_limit += 1

    return signature
