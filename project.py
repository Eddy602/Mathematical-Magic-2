n=int(input("enter range limit"))
print("prime numbers from 0 -",n)
for num in range(2, n+1):
    is_prime=True
    for x in range(2,num):
        if num%x ==0: 
            is_prime=False
            break
    if is_prime:
        print(num, end="")    