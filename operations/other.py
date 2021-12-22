import main
import math
def operations(characters, result):
    a  = 0
    for i in characters:
        
        if i == "+":
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

            #pos_nb1 = pos - 1
            #pos_nb2 = pos + 1
            #nb1 = characters[pos_nb1]
            #nb2 = characters[pos_nb2]
            result = main.add(nb1, nb2)
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
            nb1 = int(nb1.replace("/", ""))
            nb2 = int(nb2.replace("/", ""))
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
        if i == "f":
            pos = characters.index(i)
            nb1 = ''
            nb2 = ''
            if characters[pos+1] == "i":
                if characters[pos+2] == "b":
                    if characters[pos+3] == "o":
                        if characters[pos+4] == "(":
                            pos2 = pos + 5
                            a = pos2 + 1
                            while a <= len(characters):
                                #if characters[a - 1] == ")":
                                    #break
                                if characters[a - 1] == ")":
                                    break
                                nb1 = nb1 + str(characters[a - 1])
                                a+=1
                            nb1 = int(nb1)
                            result = main.fibonacci(nb1)
    return result

