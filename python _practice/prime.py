# it print prime numbers in a certain range
import math   
def IsPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
         if n % i == 0:
            return False
    return True
a = int(input())
b = int(input())
for i in range(a, b):
    if IsPrime(i):
        print(i,end=" ")
