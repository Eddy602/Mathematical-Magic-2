def findlcm(a ,b):
    def gcd(x,y):
        while y:
            #euclidean algorithm        
            x, y=y, x%y
        return x
    return(a*b) //gcd(a,b) 
num1=int(input("enter  first number")) 
num2=int(input("enter second  number")) 
print(findlcm)