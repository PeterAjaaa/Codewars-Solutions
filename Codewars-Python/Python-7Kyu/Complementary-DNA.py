# Link to kata: https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    pair = {"A":"T", "T":"A", "C":"G", "G":"C"} 
    x = ""
    
    for data in dna:
        if data == "A":
            x += pair["A"]
        elif data == "T":
            x += pair["T"]
        elif data == "G":
            x += pair["G"]
        elif data == "C":
            x += pair["C"]
            
    return x
