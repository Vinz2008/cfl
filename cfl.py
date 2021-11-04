import sys
sys.path.insert(1, 'operations/')
import main
numbers = "0123456789"
text = "9 + 5"
current_char = 0
characters = []
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
print(characters)
print(result)
