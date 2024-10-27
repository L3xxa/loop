import random

def function1():
    print("Вирішіть 2 задачі =>")
    corect = 0
    for i in range(2):
        a = random.randint(1,3)
        b = random.randint(1,3)
        c = int(input(f'{a} * {b} = '))
        if c == a*b:
            print("Successful!")
            corect += 1

        else:
            print("Idiot")

    if corect == 2:
        print("Ти геній!!!")
    elif corect == 1:
        print("Ти молодець!")
    else:
        print("Loser!")
    return corect

def function2():
    print("Вирішіть 3 задачі=>")
    corect = 0
    for i in range(3):
        a = random.randint(2,6)
        b = random.randint(2,6)
        c = int(input(f'{a} * {b} = '))
        if c == a*b:
            print("Successful!")
            corect += 1

        else:
            print("Idiot")

    if corect == 3:
        print("Ти геній!!!")
    elif corect == 2 or corect == 1:
        print("Ти молодець!")
    else:
        print("Loser!")
    return corect

def function3():
    print("Вирішіть 5 задач=>")
    corect = 0
    for i in range(5):
        a = random.randint(-10,10)
        b = random.randint(-10,10)
        c = int(input(f'{a} * {b} = '))
        if c == a*b:
            print("Successful!")
            corect += 1

        else:
            print("Idiot")

    if corect == 5 or corect == 4:
        print("Ти геній!!!")
    elif corect == 3:
        print("Ти молодець!")
    elif corect == 2 or corect == 1:
        print("Можна і краще!")
    else:
        print("Loser!")
    return corect