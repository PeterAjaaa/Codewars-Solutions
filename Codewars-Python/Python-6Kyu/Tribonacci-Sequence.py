# Link to kata: https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    tribonacci_sequence = signature
    i = 3
    
    if n == 0: 
            return []
      
    while i < n:  
        tribonacci_sequence.append(tribonacci_sequence[-3] + tribonacci_sequence[-2] + tribonacci_sequence[-1])
        i += 1
        
    return tribonacci_sequence[:n]
