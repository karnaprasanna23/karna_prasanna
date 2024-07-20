s = "3-598-21508-x"
s= s.replace("-","")
#s= s.replace("x","10")
print(s)
s1=s
sum = 0
a = 10

for i in s1:
    if i == "x":
        sum+=10
    else:
        sum+= int(i)*a
    a-=1    
if sum%11==0:
    print("valid")
else:
    print("invalid")
    
    
s = "abc"
d={}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
for i in d:
    if d[i] != d[s[0]]:
        print("invalid")
        break
else:
    print("valid")
    
