# Link to kata: https://www.codewars.com/kata/57f8ff867a28db569e000c4a

def kebabize(string):
    import string as module
    upper  = list(module.ascii_uppercase)
    string = list(string)
    num = ["1","2","3","4","5","6","7","8","9","0"]
    kebab = []
    
    for x in string:
        if x not in upper:
            kebab.append(x)
        if x in upper:
            kebab.append("-")
            kebab.append(x.casefold())
        elif x in num:
            del kebab[kebab.index(x)]
            
    try: # Use try:... except:... to get rid of the 'IndexError' caused by line 14 on an "integer-only" string.
        if "-" == kebab[0]:
            del kebab[0]
    except:
        pass # Use pass to let the interpreter know that they don't have to do anything.
        
    return "".join(kebab)
