def romb():

    for i in range(0,7):
        print("   "*(7-i-1),end=" ")
        for j in range(0,7):
            if i >= j:
                print(f'*',end="     ")
        print()

    for i in range(6,-1,-1):
        print("   "*(7-i-1),end=" ")
        for j in range(6,-1,-1):
            if i >= j:
                print(f'*',end="     ")
        print()