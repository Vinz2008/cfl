import main
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
    return result
