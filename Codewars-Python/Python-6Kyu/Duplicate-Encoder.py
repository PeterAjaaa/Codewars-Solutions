# Link to kata: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    word = word.casefold() # Makes the string case-insensitive.
    y = list(word)
    z = []
    
    for x in y:
        if y.count(x) == 1:
            z.append("(")
        elif y.count(x) > 1:
            z.append(")") 
            
    return "".join(z) # Using join() function to "convert" the z list into a string.
  
# Note :
# casefold() is more aggresive than lower() and is best suited if you're working with 
# (or planning to work with) unicode characters. You can use lower() if you're working 
# exclusively with alphabet.
