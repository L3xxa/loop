def desk (num):
    if num <= 0:
        return

    for i in range (3):
        print()
        for j in range (4):
            print ("\033[92m*"*3,end = (""))
            print ("\033[94m_"*3,end = (""))
    for i in range(3):
        print()
        for j in range(4):
            print("\033[94m_" * 3, end=(""))
            print("\033[92m*" * 3, end=(""))
