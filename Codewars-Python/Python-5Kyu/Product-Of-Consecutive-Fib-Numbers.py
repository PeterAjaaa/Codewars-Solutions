# Link to kata: https://www.codewars.com/kata/5541f58a944b85ce6d00006a

def productFib(prod):
    fibonacci = [0, 1]
    i = 0 
    x = 0 
    fib_number = 0

    while True :
        fib_number = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(fib_number)
        if fib_number >= prod:
            break
            
    while True:
        if i != 0:
            x = fibonacci[i] * fibonacci[i+1]
            i += 1
        elif i == 0:
            i += 1
        if x >= prod:
            return [fibonacci[i-1],fibonacci[i], bool(x == prod)]
            break
# Note : 
# TLDR: An infinite decimal is as accurate as an infinite decimal could be. 
# TLDR 2: Use normal addition instead.

# Explanation : 
# Don't use the 1.618034 (aka the golden ratio) to calculate the fibonacci sequence.
# The reason is because when the numbers gets pretty big, it'll be inaccurate.
# The golden ratio goes in forever for infinite amount of number and thus is not accurate and can not be set as a rock-solid way to calculate the fibonacci sequence.
# Use the normal, usual way to calculate the fibonacci sequence (which is by adding up the last 2 numbers before the current number).
