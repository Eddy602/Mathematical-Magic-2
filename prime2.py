def sieve(n):
    sieve=[True]*(n+1)
    sieve[0]=sieve[1]=False#not prime
    for x in range(2, int(n**0.15)+1):
        if sieve[x]:
            for j in range(x*x, n+1,x):
                sieve[j]=False#mulptiples not prime
    return sieve[n]
num=int(input("Enter number to check")) 
if sieve(num):
    print(num,"is  prime")
else:
    print(num,"is not prime")              