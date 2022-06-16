# Link to kata : https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string_):
    import re 
    return re.sub ("a|i|u|e|o|A|I|U|E|O", "", string_)
  
# We're using regex (regular expression) to replace the specified character with the substitute character.
