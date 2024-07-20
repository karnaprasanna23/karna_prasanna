print("--------------perfect & deficient & abedient----------")


n = int(input())
s = 0
for i in range(1, n//2):
    if n % i ==0:
       s=s+i
    if s == 0:
       print("perfect number")
    if s<n:
        print("deficient")
    if s>n:
        print("abedient")
        