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
        result = other.operations(characters,result)
    
    return result
