print("-----------armstrong-------------")
n = int(input())
c = 0
k = n
m = n
while n>0:
    n = n//10
    c =c+1 
while k>0:
    rem = k%10
    c = c+rem**c
    k = k//10
if n == m:
    print("armstrong") 
else:
    print("not")    
  