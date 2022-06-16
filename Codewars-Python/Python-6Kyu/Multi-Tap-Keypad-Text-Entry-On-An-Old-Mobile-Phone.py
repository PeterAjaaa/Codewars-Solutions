# Link to kata: https://www.codewars.com/kata/54a2e93b22d236498400134b

def presses(phrase):
    phrase = phrase.casefold()
   
    one_press = {"a","d","g","j","m","p","t","w"," ","1","*","#"}
    two_press = {"b","e","h","k","n","q","u","x","0"}
    three_press = {"c","f","i","l","o","r","v","y"}
    four_press = {"s","z","2","3","4","5","6","8"}
    five_press = {"7","9"}
    
    chara_dict  = dict.fromkeys(one_press, 1) # Making a 'chara_dict' dict with the initial key:value pair from 'one_press' keys and with the value of 1.
    chara_dict.update(dict.fromkeys(two_press, 2))
    chara_dict.update(dict.fromkeys(three_press, 3))
    chara_dict.update(dict.fromkeys(four_press, 4))
    chara_dict.update(dict.fromkeys(five_press, 5))
    
    count = 0
    
    for x in phrase:
        count += chara_dict[x]
    return count
