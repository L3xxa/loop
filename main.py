# Example 1
def simple_numbers(a,b):
    prime_numbers=[]
    for i in range(a,b+1):
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k==2:
            prime_numbers.append(i)
    print(prime_numbers)

a = int(input( "Enter a number: " ))
b = int(input( "Enter a number: " ))
simple_numbers(a,b)




