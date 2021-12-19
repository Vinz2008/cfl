def fibonacci(nb1):
    import time
    sequence = []
    sequence.append(1)
    sequence.append(1)
    print("1")
    print("1")
    position = 2
    a = nb1
    while position < a:
        result = sequence[position-2] + sequence[position-1]
        sequence.append(result)
        result = str(result)
        position+=1
        print(result)
        time.sleep(0.5)
    return ""
