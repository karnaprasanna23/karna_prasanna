s = input()
c = 0
for i in s:
    if(i.isdigit()):
        c =c+1
print(c)


s = "zebra"
s1 = ""
k = 4
for i in s:
    s1 += chr(ord(i)+k)    # it prints symbols
print(s1)


n = int(input())
c = 0
for i in range(n):
    for j in range(i):
        print(c,end=" ")
        c+=1
    print("")