import main
import math
def operations(characters, result):
    for i in characters:
        if i == "*":
            pos = characters.index(i)
            nb1 = ''
            nb2 = ''
            for f in range(pos):
                nb1 = nb1 + str(characters[f])
            a = len(characters) - pos + 1
            
            while a <= len(characters):
                nb2 = nb2 + str(characters[a - 1])
                a+=1
            nb1 = int(nb1)
            nb2 = int(nb2)
            result = main.mult(nb1, nb2)
        if i == "/":
            pos = characters.index(i)
            nb1 = ''
            nb2 = ''
            for f in range(pos):
                nb1 = nb1 + str(characters[f])
            a = len(characters) - pos + 1

            while a <= len(characters):
                nb2 = nb2 + str(characters[a - 1])
                a+=1
            nb1 = int(nb1)
            nb2 = int(nb2)
            result = main.div(nb1, nb2)
        if i == "-":
            pos = characters.index(i)
            nb1 = ''
            nb2 = ''
            for f in range(pos):
                nb1 = nb1 + str(characters[f])
            a = len(characters) - pos + 1

            while a <= len(characters):
                nb2 = nb2 + str(characters[a - 1])
                a+=1
            nb1 = int(nb1)
            nb2 = int(nb2)
            result = main.minus(nb1, nb2)
        if i == "s":
            pos = characters.index(i)
            if characters[pos+1] == "q":
                if characters[pos+2] == "r":
                    if characters[pos+3] == "t":
                        if characters[pos+4] == "(":
                            pos2 = pos + 5
                            nb1 = ''
                            #a = len(characters) - pos2 + 4
                            a = pos2 + 1
                            while a <= len(characters):
                                if characters[a - 1] == ")":
                                    break
                                nb1 = nb1 + str(characters[a - 1])
                                a+=1
                            nb1 = int(nb1)
                            result = main.square(nb1)
    return result

