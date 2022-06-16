# Link to kata: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

def high(x):
    import string

    x = x.split(" ")
    chara_dict = dict(zip(list(string.ascii_lowercase),[i for i in range(1,27)]))
    word_value = []
    chara_value = 0
    i = 0
    
    while True:
        for y in x[i]:
            chara_value += chara_dict[y]
        word_value.append(chara_value)
        i += 1
        chara_value = 0
        if i >= len(x):
                break
                
    word_dict = dict(zip(x, word_value))
    return max(word_dict, key = word_dict.get) # Return the max value from 'word_dict' dict. Used get() function here.

# Note:
# The key parameter to the max() function is a function that computes a key that is used to determine how to rank items.
# We can use operator.itemgetter() function to replace the get() function, but the syntax on operator.itemgetter() is more complicated than when we're using get() function.
