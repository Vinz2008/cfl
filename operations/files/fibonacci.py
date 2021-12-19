def fibonacci(nb1):
    sequence = []
    sequence.append(1)
    sequence.append(1)
    print("1")
    print("1")
    position = 1
    while True:
        result = sequence[position-2] + sequence[position-1]
        sequence.append(result)
        result = str(result)
        position+=1
        print(result)
        time.sleep(0.5)
    return ""
