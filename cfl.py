import math
import sys
sys.path.insert(1, 'operations/')
import main
import other
def calc(text):
    numbers = "0123456789"
    #text = "9 + 5"
    result = 0
    current_char = 0
    characters = []
    a = 0
    for i in text:
        if i != ' ':
            if i in numbers:
                characters.append(int(i))
                current_char += 1
            else:  
                characters.append(i)
                current_char += 1
    for i in characters:
        if i == "+":
            pos = characters.index(i)
            pos_nb1 = pos - 1
            pos_nb2 = pos + 1
            nb1 = characters[pos_nb1]
            nb2 = characters[pos_nb2]
            result = main.add(nb1, nb2)
            a -= 1
        else:
            a += 1
    if a == len(characters):
        result = other.operations(characters,result)
    
    return result
