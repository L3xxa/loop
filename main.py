def multiplication_table():
    a = int(input( "Enter a number: " ))
    b = int(input( "Enter a number: " ))
    for i in range(a,b+1):
        for j  in range(1,11):
            print(f'{i}*{j}={i*j}', end=" ")
        print()
multiplication_table()