def primecheck(n):
    if n<=1:
        return False #not prime
    for x in range(2,  n):
        if n%x ==0:
            return False
        return True#prime
num=int(input("Enter number to check"))
if primecheck(num): #true
    print(num,"is a prime number") 
else: #false
    print(num,"is not a prime number")       